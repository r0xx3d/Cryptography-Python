
stat = input("Enter the statement")
key1 = int(input("enter the first key"))
key2 = int(input("enter the second key"))


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
    p = x*key1 + key2

    if p<26:
        new_list.append(alpha[p])

    else:
        new_list.append(alpha[p%26])



string = " ".join(new_list)

print(string)
print(new_alpha)

# print(list_of_stat)
print(stat_index)
print(new_list)
