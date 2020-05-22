import pandas as pd

# 方法一：默认读取第一个表
# head()默认读取前5行数据
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.head(1)
# list=[]
# list.append(df.head(10))

# 读取指定表单数据
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx",sheet_name='test')
# data = df.head()

# 方法三：通过表单索引来指定要访问的表单，0表示第一个表单
# 也可以采用表单名和索引的双重方式来定位表单
# 也可以同时定位多个表单，方式都罗列如下所示
# df=pd.read_excel('lemon.xlsx',sheet_name=['python','student']) # 可以通过表单名同时指定多个
# # df=pd.read_excel('lemon.xlsx',sheet_name=0)#可以通过表单索引来指定读取的表单
# # df=pd.read_excel('lemon.xlsx',sheet_name=['python',1])#可以混合的方式来指定
# # df=pd.read_excel('lemon.xlsx',sheet_name=[1,2])#可以通过索引 同时指定多个
# data=df.values # 获取所有的数据，注意这里不能用head()方法哦~
# print("获取到所有的值:\n{0}".format(data)) # 格式化输出


# 读取指定的单行，数据会存在列表里面
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.loc[6].values

# 读取指定的多行数据，数据会存在列表里面
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.loc[[5,9]].values
# data = df.iloc[[5,9]].values

# 读取指定的行列
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.loc[6, 'Method']
# data = df.iloc[6, 9]

# 读取指定的多行多列值
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.iloc[[5,6],[3,4]].values
# data = df.loc[[5,6],['Title','Method']].values

# 获取所有行的指定列
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.iloc[:,[3,4]].values

# 获取行号并打印输出
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")

# 获取列名并打印输出
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# print("输出列名：{}".format(df.columns.values))

# 获取指定行数的值(随机输出指定行数的值）
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# data = df.sample(5)

# 获取指定列的值
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# print(f"输出列的值是{df['Method'].values}")
# print("输出列的值是%s" % (df['Method'].values))

# Excel数据写回
df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
df.read_e
print("测试数据是:{}".format(data))

# 四：pandas处理Excel数据成为字典
# df = pd.read_excel(r"D:\pycharm\API_D\Test_data\data\data.xlsx")
# test_data=[]
# for i in df.index.values: # 获取行号的索引，并对其进行遍历：
#     # 根据i来获取每一行指定的数据 并利用to_dict转成字典
#     row_data=df.loc[i,['CaseId','Module','URL','Title','Method','Params',
#                       'ExpectedResult','ActualResult','TestResult']].to_dict()
#     test_data.append(row_data)
# print("最终获取到的数据是：{0}".format(test_data))
