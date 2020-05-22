from pytest框架复习 import testdata
import pytest


@pytest.mark.success
@pytest.mark.print
@pytest.mark.parametrize('data', testdata.su)
def test_PrintHobby(data):
    print('第{}条用例，{}今年{}岁，身高{}，爱好是{}'.format(data['id'],data['name'],
                                      data['age'],data['height'],data['hobby']))


@pytest.mark.success
@pytest.mark.skip(reason='重复')
@pytest.mark.error
@pytest.mark.parametrize('data', testdata.er)
def test_Hobby(data):
    print('第{}条用例，{}今年{}岁，身高{}，爱好是{}'.format(data['id'],data['name'],
                                      data['age'],data['height'],data['hobby']))


if __name__ == '__main__':
    pytest.main()


# pytest -m "print"
# pytest -m "success and not error"
# pytest test_demo.py
