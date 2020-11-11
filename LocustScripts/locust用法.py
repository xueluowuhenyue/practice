from locust import HttpUser, task, SequentialTaskSet, between, tag


class BestTest(SequentialTaskSet):
    # SequentialTaskSet任务从上到下执行，TaskSet随机执行
    def on_start(self):
        # TODO 开始方法相当于setup
        pass

    @task(1)  # TODO:给task装饰器传一个参数，代表先访问首页
    @tag("home")
    def index(self):  # 首页
        self.client.get('/', name="首页")

    @task(1)
    def login(self):  # 登录
        data = {'phone': '18684720553', 'password': 'python', 'vcode':'', 'remember_me':1}
        self.client.post('/login', data=data, name="登录")
        # TODO:发送post请求，第一个是路径，第二个这个接口的入参，账号和密码

    def on_stop(self):
        # TODO 结束方法相当于teardown
        pass


class BestTestIndexUser(HttpUser):
    # TODO:这个类继承了HttpUser，代表每个并发里面的每个用户
    tasks = [BestTest]  # 这个是每个用户都去干什么，指定了BestTest这个类，
    # TODO:它就会每个用户去运行besttest这个类里面的方法
    min_wait = 1
    max_wait = 3
    wait_time = between(min_wait, max_wait)
    # TODO:设置运行时间
    stop_timeout = 60


if __name__ == '__main__':
    import os
    os.system(r"locust -E home -f D:\Pycharm\Scripts\WEB_LX\练习\locust用法.py --host=http://120.78.128.25:8765/Frontend/Index")