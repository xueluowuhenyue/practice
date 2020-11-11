from locust import HttpUser, TaskSet, task, SequentialTaskSet, HttpLocust


class BestTest(TaskSet):
    @task(1)  # TODO:给task装饰器传一个参数，代表先访问首页
    def index(self):  # 首页
        self.client.get('/')
        # 发get请求

    @task(1)
    def login(self):  # 登录
        data = {'phone': '18684720553', 'password': 'python', 'vcode':'', 'remember_me':1}
        self.client.post('/login', data=data)
        # TODO:发送post请求，第一个是路径，第二个这个接口的入参，账号和密码


class BestTestIndexUser(HttpUser):
    # TODO:这个类继承了HttpUser，代表每个并发里面的每个用户
    tasks = [BestTest]  # 这个是每个用户都去干什么，指定了BestTest这个类，
    # TODO:它就会每个用户去运行besttest这个类里面的方法
    min_wait = 1000
    max_wait = 5000
    # TODO:设置运行时间
    stop_timeout = 60


if __name__ == '__main__':
    import os
    os.system(r"locust -f D:\Pycharm\Scripts\WEB_LX\练习\locust用法.py  --host=http://120.78.128.25:8765/Frontend/Index")