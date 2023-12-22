homophonic_equivalents={
    'A':'H',
    'B':'P',
    'C':'U',
    'D':'T',
    'E':'F',
    'F':'E',
    'G':'J',
    'H':'R',
    'I':'L',
    'J':'Y',
    'K':'Q',
    'L':'V',
    'M':'X',
    'N':'M',
    'O':'D',
    'P':'B',
    'Q':'W',
    'R':'N',
    'S':'C',
    'T':'I',
    'U':'A',
    'V':'Z',
    'W':'G',
    'X':'K',
    'Y':'O',
    'Z':'S',
    ' ':'$'
}

user_input=input('Enter text: ')
user_input=user_input.upper()
encrpted_text=""
for char in user_input:
    for key,value in homophonic_equivalents.items():
        if(char==key):
            encrpted_text+=value

# print('Encrypted text:',encrpted_text)

decrypted_text='';
for char in user_input:
    for key,value in homophonic_equivalents.items():
            if(char==value):
                 decrypted_text+=key;

# print('Decrypted text: ',decrypted_text)
b=int(input("What do you want to do \n1.Encrypt\n2.Decrypt\n?? :"))
if b == 1 :
    print('Encrypted text:', encrpted_text)
if b==2:
    print('Decrypted text: ', decrypted_text)
else:
    print("xxx----xxxx----xx---x")