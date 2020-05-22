# 字典 dict dictionary 符号 {}
# 特征：
# 1.大括号括起来的都是字典，看类型type
# 2.空字典d={}
# 3.字典里元素存储方式 key：volue的形式 键值对 key不可变 int float tuple str
# True=1 False=0
# 4.字典中可以包含各种类型的数据：整数、浮点数、布尔值....key：volue中间用冒号隔开
# 5.字典无序 取值字典名[key]
# 6.字典嵌套 取值层层取
# 7.字典增删改
d={'name':'hbh',
   'age':18,
   'height':180.12,
   'hobby':['篮球','乒乓','钓鱼'],
   'friend':{'vc':'bvcj'}}
print(d)
print(d['friend']['vc'])
# 增加 字典名[key]不存在既是新增
d['sal']='20k'
print(d)
# 修改 字典名【key】存在既是修改
d['sal']='15k'
print(d)
# 删除 关键字pop 根据key删除
d.pop('friend')
print(d)
# 随机删除 poptem()
d.popitem()
print(d)
# 获取所有key keys（）
# 获取所有value()
print(d.keys())
print(d.values())