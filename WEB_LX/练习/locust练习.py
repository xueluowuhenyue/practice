from locust import TaskSet, HttpLocust, task


class Login(TaskSet):

    # @task(1)
    # def home(self):
    #     url = "/Index"
    #     headers = {"User-Agent": "Mozilla/5.0"}
    #     self.client.get(url, headers=headers, name="进入首页")

    @task(1)
    def login(self):
        # url = "/Index/login.html"
        url = "/login"
        # headers = {"User-Agent": "Mozilla/5.0"}
        # data = {"phone": 18684720553, "password": "python", "remember_me": 1}
        data = {'mobilephone': '13541781424', 'pwd': '123456'}
        res = self.client.post(url, data=data, name="登录")
        print(res.text)


class TestData(HttpLocust):
    task_set = Login
    # host = "http://120.78.128.25:8765"
    host = "http://test.lemonban.com/futureloan/mvc/api/member"
    min_wait = 1000
    max_wait = 5000
    # stop_timeout = 60 设置运行时间


if __name__ == '__main__':
    import os
    os.system(r"locust -f D:\pycharm\workspace\test1\venv\locust练习.py --slave --master-host=192.168.163.139")