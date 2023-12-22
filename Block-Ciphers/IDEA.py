
def hex2bin(s):
    mp = {'0': "0000",
          '1': "0001",
          '2': "0010",
          '3': "0011",
          '4': "0100",
          '5': "0101",
          '6': "0110",
          '7': "0111",
          '8': "1000",
          '9': "1001",
          'A': "1010",
          'B': "1011",
          'C': "1100",
          'D': "1101",
          'E': "1110",
          'F': "1111"}
    bin = ""
    for i in range(len(s)):
        bin = bin + mp[s[i]]
    return bin


def bin2hex(s):
    mp = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch = ch + s[i]
        ch = ch + s[i + 1]
        ch = ch + s[i + 2]
        ch = ch + s[i + 3]
        hex = hex + mp[ch]

    return hex

def binary_value(x):
    x = f'{x}'
    x = x[2:]
    return hex2bin(x.upper())



def _mul(x, y):
    assert 0 <= x <= 0xFFFF
    assert 0 <= y <= 0xFFFF

    if x == 0:
        x = 0x10000
    if y == 0:
        y = 0x10000

    r = (x * y) % 0x10001

    if r == 0x10000:
        r = 0

    assert 0 <= r <= 0xFFFF
    return r


def _KA_layer(x1, x2, x3, x4, round_keys):
    assert 0 <= x1 <= 0xFFFF
    assert 0 <= x2 <= 0xFFFF
    assert 0 <= x3 <= 0xFFFF
    assert 0 <= x4 <= 0xFFFF
    z1, z2, z3, z4 = round_keys[0:4]
    assert 0 <= z1 <= 0xFFFF
    assert 0 <= z2 <= 0xFFFF
    assert 0 <= z3 <= 0xFFFF
    assert 0 <= z4 <= 0xFFFF

    y1 = _mul(x1, z1)
    y2 = (x2 + z2) % 0x10000
    y3 = (x3 + z3) % 0x10000
    y4 = _mul(x4, z4)

    return y1, y2, y3, y4


def _MA_layer(y1, y2, y3, y4, round_keys):
    assert 0 <= y1 <= 0xFFFF
    assert 0 <= y2 <= 0xFFFF
    assert 0 <= y3 <= 0xFFFF
    assert 0 <= y4 <= 0xFFFF
    z5, z6 = round_keys[4:6]
    assert 0 <= z5 <= 0xFFFF
    assert 0 <= z6 <= 0xFFFF

    p = y1 ^ y3
    q = y2 ^ y4

    s = _mul(p, z5)
    t = _mul((q + s) % 0x10000, z6)
    u = (s + t) % 0x10000

    x1 = y1 ^ t
    x2 = y2 ^ u
    x3 = y3 ^ t
    x4 = y4 ^ u

    return x1, x2, x3, x4


class IDEA:
    def __init__(self, key):
        self._keys = None
        self.change_key(key)

    def change_key(self, key):
        assert 0 <= key < (1 << 128)
        modulus = 1 << 128

        sub_keys = []
        for i in range(9 * 6):
            sub_keys.append((key >> (112 - 16 * (i % 8))) % 0x10000)
            if i % 8 == 7:
                key = ((key << 25) | (key >> 103)) % modulus

        keys = []

        for i in range(9):
            round_keys = sub_keys[6 * i: 6 * (i + 1)]
            keys.append(tuple(round_keys))
        self._keys = tuple(keys)
        keylist = []
        for i in self._keys:
            for j in i:
                keylist.append(hex(j))
                print("key :",hex(j))

        revkeys = []

        for i in range(9):
            round_revkeys = sub_keys[6 * i: 6 * (i + 1)]
            revkeys.append(tuple(round_revkeys))
            revkeys.reverse()
        self._revkeys = tuple(revkeys)



    def encrypt(self, plaintext):
        assert 0 <= plaintext < (1 << 64)
        x1 = (plaintext >> 48) & 0xFFFF
        x2 = (plaintext >> 32) & 0xFFFF
        x3 = (plaintext >> 16) & 0xFFFF
        x4 = plaintext & 0xFFFF

        for i in range(8):
            round_keys = self._keys[i]

            y1, y2, y3, y4 = _KA_layer(x1, x2, x3, x4, round_keys)
            print("Layer 1 : ",hex(y1),hex(y2),hex(y3),hex(y4))
            x1, x2, x3, x4 = _MA_layer(y1, y2, y3, y4, round_keys)
            print("Layer 2 : ", hex(x1),hex(x2),hex(x3),hex(x4))

            x2, x3 = x3, x2

        # Note: The words x2 and x3 are not permuted in the last round
        # So here we use x1, x3, x2, x4 as input instead of x1, x2, x3, x4
        # in order to cancel the last permutation x2, x3 = x3, x2
        y1, y2, y3, y4 = _KA_layer(x1, x3, x2, x4, self._keys[8])
        print("Last Round : ", hex(y1),hex(y2),hex(y3),hex(y4))

        ciphertext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
        return ciphertext

    """def decrypt(self, ciphertext):

        x1 = (ciphertext >> 48) & 0xFFFF
        x2 = (ciphertext >> 32) & 0xFFFF
        x3 = (ciphertext >> 16) & 0xFFFF
        x4 = ciphertext & 0xFFFF
        y1,y2,y3,y4 = _KA_layer(x1,x2,x3,x4,self._revkeys[0])
        y2, y3 = y3, y2

        for i in range(1,9):
            round_revkeys = self._revkeys[i]
            x1,x2,x3,x4 = _MA_layer(y1,y2,y3,y4,round_revkeys)
            print("Layer 1 : ", hex(x1), hex(x2), hex(x3), hex(x4))
            y1,y2,y3,y4 = _KA_layer(x1,x2,x3,x4,round_revkeys)
            print("Layer 2 : ", hex(y1), hex(y2), hex(y3), hex(y4))

        plaintext = (y1 << 48) | (y2 << 32) | (y3 << 16) | y4
        return plaintext"""



def main():
    # key = 0x00000000000000000000000000000000
    #plain  = 0x8000000000000000
    # cipher = 0x8001000180008000

    key = 0x2BD6459F82C5B300952C49104881FF48
    plain = 0xF129A6601EF62A47

    print ('master key : ', hex(key))
    print('plaintext : ', hex(plain), "   or    ",binary_value(plain))

    my_IDEA = IDEA(key)
    encrypted = my_IDEA.encrypt(plain)

    print('ciphertext : ', hex(encrypted), "    or    ",binary_value(encrypted))

    """decrypted = my_IDEA.decrypt(encrypted)

    print('plaintext : ', hex(decrypted), "   or    ", binary_value(decrypted))"""





if __name__ == '__main__':
    main()