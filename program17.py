


s=input("Enetr a string:")
l=[]
for i in s.split():
    if i==i[::-1]:
        l.append(i)
print()
for i in range(len(l)):
    print(l[i])
print()
print(" the total{}palindrome:{}".format(len(l),l))
