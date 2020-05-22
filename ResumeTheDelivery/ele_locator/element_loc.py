# 选择登录
from selenium.webdriver.common.by import By
from common.Public import project_path
from common.Public.read_ini import Configuration
sal = login_name = Configuration(project_path.config_path).read_str('DATA', 'sal')
record_school = Configuration(project_path.config_path).read_str('DATA', 'record_school')
release_time = Configuration(project_path.config_path).read_str('DATA', 'release_time')

# 选择登陆方式
login_choose = (By.XPATH, "//p[@class='goSignIn']/a")

# 定位用户名输入框
login_user = (By.XPATH,"//input[@id='loginname']")

#  定位密码输入框
login_pwd = (By.XPATH,"//input[@id='password']")

# 定位登录按钮
login_button = (By.XPATH,"//button[@id='login_btn']")

# 定位首页按钮
home_button = (By.XPATH,"//p[@class='nlink']/a[text()='首页']")

# 搜索框
input_box = (By.XPATH, "//input[@id='kwdselectid']")

# 搜索按钮
box_button = (By.XPATH, "//button[text()='搜索']")

# 展开选项
option_button = (By.XPATH, "//div[@class='op']/span")

# 发布日期
release_data = (By.XPATH, f"//div[@id='filter_issuedate']//a[text()='{release_time}']")

# 月薪范围
release_scope = (By.XPATH, f"//div[@id='filter_providesalary']//a[text()='{sal}']")
# 多选框
multi_select = (By.XPATH, "//div[@id='filter_providesalary']//span[contains(@class,'dx')]")

# 学历要求
release_record = (By.XPATH, f"//div[@id='filter_degreefrom']//a[text()='{record_school}']")

# 全选框
select_button = (By.XPATH,"//em[contains(@id,'checkbox')]")
# 6-8千
sal6_8 = (By.XPATH, "//div[@id='multichoices_providesalary']//li[@data-value='05']")
sal8_10 = (By.XPATH, "//div[@id='multichoices_providesalary']//li[@data-value='06']")
sal15_20 = (By.XPATH, "//div[@id='multichoices_providesalary']//li[@data-value='08']")
# 确认按钮
determine_button = (By.XPATH, "//div[@id='multichoices_providesalary']//span[@class='p_but']")

# 申请职位
job_button = (By.XPATH, "//span[@class='but_sq']")

# 页数
pages_button = (By.XPATH, "//div[@class='p_in']//li")

# 职位名称
job_number = (By.XPATH,"//div[@id='resultList']//div[@class='el']/p/span/a")

# 公司名称
name = (By.XPATH, "//div[@id='resultList']//div[@class='el']/span/a")

# 公司地址
addr = (By.XPATH, "//div[@id='resultList']//div[@class='el']/span[@class='t3']")

# 薪资
salary = (By.XPATH, "//div[@id='resultList']//div[@class='el']/span[@class='t4']")

# 薪资
release = (By.XPATH, "//div[@id='resultList']//div[@class='el']/span[@class='t5']")
