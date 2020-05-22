import pytest
import logging
l=[[1,1,2,3],[2,5,8,13],[3,9,6,15],[4,7,1,8]]
m=[[1,5,2,3],[2,23,8,15],[3,21,6,15],[4,9,1,8]]


@pytest.mark.parametrize('data',l)
def test_add(data):
    logging.info(f"*******开始测试******,第{data[0]}条测试用例")
    expectd = data[1]+data[2]
    try:
        assert (expectd == data[3])
        Testresult = 'Pass'
    except AssertionError as e:
        Testresult = 'FAIL'
        raise e
    logging.info(f"*******开始测试******第{data[0]}条测试用例,测试结果是{Testresult}")
    print(f"第{data[0]}条测试用例,*******测试结束******")


@pytest.mark.parametrize('data',m)
def test_sub(data):
    logging.info(f"*******开始测试******,第{data[0]}条测试用例")
    expectd = data[1]-data[2]
    try:
        assert (expectd == data[3])
        Testresult = 'Pass'
    except AssertionError as e:
        Testresult = 'FAIL'
        raise e
    logging.info(f"*******开始测试******第{data[0]}条测试用例,测试结果是{Testresult}")
    print(f"第{data[0]}条测试用例,*******测试结束******")


if __name__ == '__main__':
    # pytest.main(["-n", "2", "-s", r"D:\pycharm\ResumeTheDelivery\script\pytest并发.py"])
    pytest.main(["-s", r"D:\pycharm\ResumeTheDelivery\script\pytest并发.py"])
    # pytest.main(["-v", "-n", "auto", r"D:\pycharm\ResumeTheDelivery\script\pytest并发.py"])
