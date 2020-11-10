import pytest

if __name__ == '__main__':
    pytest.main(['-s', r'--alluredir=Result\report\allure', '--clean-alluredir', r'--html=Result\report\api.html'])