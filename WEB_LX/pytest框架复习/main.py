import pytest

if __name__ == '__main__':
    pytest.main(['-s','--reruns','5'])
    # pytest.main(['-s', '--reruns', '5', r'--alluredir=Result\report\allure', r'--html=Result\report\web.html'])