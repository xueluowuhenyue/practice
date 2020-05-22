l=[[1,2],[2,3],[1,5],[2,3],[1,2]]
    # list.append(tuple(set(i)))

mm=set()
for i in l:
    mm.add(tuple(i))
print(list(mm))
# print(list(set(tuple(a) for a in l)))

# lists=list
# kk=set()
# for i in l:
#     kk.add(tuple(i))
#
# lists=kk
# print(lists)
ml=list()
ml.append(1)
print(ml)

l=[2,6,4,89,7,2,1]

m=set()
for i in l:
    m.add(i)
print(m)