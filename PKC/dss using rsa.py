import random

# gcd
def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)


# multiplicative inverse
def extendedeuclid(a, b):
    r1 = a
    r2 = b
    s1 = int(1)
    s2 = int(0)
    t1 = int(0)
    t2 = int(1)

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 % a

    return (r1, t1)


p = 823
q = 953
n = p * q
phi = (p - 1) * (q - 1)

key = []

for i in range(2, phi):
    gcd = euclid(phi, i)

    if gcd == 1:
        key.append(i)

e = random.choice(key)
print("encryption key : ",e)

r, d = extendedeuclid(phi, e)
if r == 1:
    d = int(d)
    print("decryption key is : ", d)

else:
    print("Multiplicative inverse for the given encryption key does not exist"
          "choose a different key for encryption")

m = 19070
s = (m ** d) % n  # signature is created by A

# A sends message and signature both to B and B generates message using the signature, A's public key and product n

m1 = (s ** e) % n

if m == m1:
    print("signature verified, accept the message sent by A")
else:
    print("signature not verified, message has been tampered with, do not accept")
