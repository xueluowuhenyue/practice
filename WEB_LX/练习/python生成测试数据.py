from random import choice
# file = open("练习.txt", "w")
# file.write("name, password, eamil\n")
# i = 1
# while i <= 10:
#     file.write("name"+str(i)+",123456,"+str(i)+"@qq.com\n")
#     i += 1

l = []
with open("test.csv","r") as file:
    for line in file.readlines():
        l.append(line.strip())
# res = choice(l)
# res = res.split(",")
# username = res[0]
# password = res[1]
# print(username)
# print(password)

# for i in l:
#     data = i.split(",")
#     username = data[0]
#     print(username)

def addstr(num):
    st = str(num).zfill(4)
    return st
print(addstr(333))