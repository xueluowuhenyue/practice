# -*- coding:utf-8 -*-

l=[6, 4, 2, 8, 7, 9, 5, 10, 0, 54, 24, 14, 44]

k=0
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]
        k+=1
print(l)
print(k)

for i in range(len(l)-1):
    for j in range(len(l)-1):
        if l[j] < l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
        k+=1
print(l)
print(k)

