# -*- coding:utf-8 -*-
import pytest
import requests
from Common.Public.Read_Excel import DoExcel
from Common.Public import Project_path
Data=DoExcel(Project_path.Excel_path).read_data('login')


@pytest.mark.parametrize('data', Data)
def test_case(data):
    id = data[0]
    url = data[2]
    param = data[5]
    exceptresult = data[6]
    headers = {'user-agent': 'Mozilla/5.0', 'Connection': 'keep-alive'}
    try:
        res=requests.post(url, data=param, headers=headers)
    except Exception as e:
        raise e

    try:
        assert (eval(exceptresult) == res.json())
        testresult='PASS'
    except AssertionError as e:
        testresult = 'FAILLED'
        print('断言错误')
        raise e

    finally:
        DoExcel(Project_path.Excel_path).write_data('login', id+1, 8, res.text)
        DoExcel(Project_path.Excel_path).write_data('login', id+1, 9, testresult)


if __name__ == '__main__':
    pytest.main()