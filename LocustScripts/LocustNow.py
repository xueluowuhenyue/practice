from locust import HttpUser, task, tag, SequentialTaskSet, between, User


class NewTest(SequentialTaskSet):
    headers = {"Content-Type": "application/json;charset=utf-8"}
    token = ''

    def on_start(self):
        pass

    @tag('register')
    @task(1)
    def register(self):
        # TODO:注册接口
        data = {"mobile": "13586349770", "password": "123456", "code": "3367", "platform": "windows"}
        self.client.post('/app/mobile/api/user/register', json=data, headers=self.headers, name="注册")

    @tag('login')
    @task(1)
    def login(self):
        # TODO:登录接口
        data = {"mobile": "18800000009", "password": "123456", "gqid":"4000004"}
        res = self.client.post('/app/mobile/api/user/login', json=data,  headers=self.headers, name="登录")
        global token
        token = res.json()['data']['token']

    @task(1)
    def get_goods_list(self):
        # TODO:获取商品列表
        self.client.get('/app/mobile/api/goods/gettypes', name="获取商品列表")

    @task(1)
    def place_the_order(self):
        # 下订单
        # print(self.token)
        data= {"token": self.token, "getAddrId": 1, "getCarId": 23, "payType": 2,
        "remark": "支付", "price": 8.88, "invoiceTitle": "", "orders": [
        {"getTime": 1450921104000, "goodss": [
            {"goodsId": 93, "count": 1}, {"goodsId": 96, "count": 1}]}]}
        self.client.post('/app/mobile/api/order/addorder', json=data, headers=self.headers, name="下单")

    def on_stop(self):
        pass


class RunClass(HttpUser):
    tasks = [NewTest]
    min_wait = 1
    max_wait = 3
    wait_time = between(min_wait, max_wait)


# if __name__ == '__main__':
#     pass
#     import os
    # os.system(r"locust -f D:\Pycharm\Scripts\LocustScripts\LocustNow.py  --host=http://192.168.31.137:8080")
    # 命令行运行：
    # locust - f LocustNow.py --host = http://192.168.31.137:8080
    # TODO:指定客户端运行端口
    # locust -f LocustNow.py --host = http://192.168.31.137:8080 --web-host 127.0.0.1 -P 8888
    # TODO:设置步长(负载测试)
    # --headless 无界面运行 -t 设置运行时间 -u 并发数 -r 每秒启动用户数 --csv 生成cev文件
    # locust -f LocustNow.py --host = http://192.168.31.137:8080  --headless -t 60s -u 300 -r 5 --csv res


