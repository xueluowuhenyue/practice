# -*- coding:utf-8 -*-
import xlsxwriter
# 新建Excel表
file=xlsxwriter.Workbook('test.xlsx')
# 创建表单
sheet = file.add_worksheet('login')
# 设置表头
headings = ['Number','module','title','result']     # 设置表头
# 数据准备
# data=[[1,2,3,4],
#       ['login','resister','bid','logout'],
#       ['登录','注册','投资','退出'],
#       ['pass','feild','pass','pass']]
# 写入数据
# sheet.write_row('A1', headings)
# sheet.write_column('A2', data[0])
# sheet.write_column('B2', data[1])
# sheet.write_column('C2', data[2])
# sheet.write_column('D2', data[3])
# # 按单元格写入数据
# sheet.write('E1','language')
# list=[['python','java','js','php']]
# for i in list:
#     sheet.write_column('E2',list[0])
data=[['1','login','登录','pass'],
      ['2','resister','注册','pass'],
      ['3','bid','投资','filed'],
      ['4','logout','退出','pass']]
sheet.write_column('A1', headings)
sheet.write_column('B1', data[0])
sheet.write_column('C1', data[1])
sheet.write_column('D1', data[2])
sheet.write_column('E1', data[3])
# 关闭文件
file.close()