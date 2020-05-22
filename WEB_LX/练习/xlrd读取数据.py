import xlrd
from xlsxwriter import Workbook


def read_Excel():
    # 打开文件
    xl=xlrd.open_workbook("test.xlsx")
    # 定位表单
    sheet=xl.sheets()[0]
    row=sheet.row_values(0)
    print(row)
    print(sheet.nrows)
    print(sheet.ncols)
    # print(sheet.cell(5,3).value)
    list=[]
    row_unm=sheet.nrows
    for i in range(row_unm):
        row_list=sheet.row_values(i)
        list.append(row_list)
    return list


def writer_excel():
    # 打开文件
    wf=Workbook("test.xlsx")
    # 创建表单
    sheet=wf.add_worksheet('change')
    # bold = wf.add_format({
    #     'bold': True,  # 字体加粗
    #     'border': 1,  # 单元格边框宽度
    #     'align': 'left',  # 水平对齐方式
    #     'valign': 'vcenter',  # 垂直对齐方式
    #     'fg_color': '#F4B084',  # 单元格背景颜色
    #     'text_wrap': True,  # 是否自动换行
    # })
    # 按单元格写入数据
    sheet.write('A1', '天')

    wf.close()


if __name__ == '__main__':
    # writer_excel()
    print(read_Excel())
