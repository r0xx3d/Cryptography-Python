
def mod_inverse(a, m):
    inverse = pow(a, -1, m)
    if inverse == 0:
        raise ValueError("The modular inverse does not exist.")
    return inverse

sta = input("Enter the encyrpted statement")
key1 = int(input("enter the first key"))
key2 = int(input("enter the second key"))
stat=sta.lower()
do = mod_inverse(key1, 26)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
list_of_stat = stat.split()
z = 0
p = 0
stat_index = []
new_list = []
new_alpha = []
for i in list_of_stat:
    for j in i:
        new_alpha.append(j)

for k in new_alpha:
    z = alpha.index(k)
    stat_index.append(z)

for x in stat_index:
    p = do * (x - key2)

    if p > 0 and p < 26:
        new_list.append(alpha[p])


    else:
        l=p%26
        new_list.append(alpha[l])

string = " ".join(new_list)

print(new_list)
# print(string)
# print(list_of_stat)

print(stat_index)

print(new_alpha)