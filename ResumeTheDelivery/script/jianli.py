from time import sleep
from common.Public.custom_fun import BasePage
from selenium.webdriver import Chrome
from ele_locator import element_loc
from common.Public import project_path
from common.Public.do_excel import DoExcel
from common.Public.read_ini import Configuration


class Janli(BasePage):
    login_name = Configuration(project_path.config_path).read_str('DATA', 'login_name')
    login_pwd = Configuration(project_path.config_path).read_str('DATA', 'login_pwd')
    context = Configuration(project_path.config_path).read_str('DATA', 'context')

    def login(self):
        # 进入登录界面
        self.wait_ele(element_loc.login_choose).click()
        # 获取打开的窗口列表
        window_list = self.driver.window_handles
        self.driver.switch_to_window(window_list[-1])
        # 输入用户名和密码
        self.wait_ele(element_loc.login_user).send_keys(self.login_name)
        self.wait_ele(element_loc.login_pwd).send_keys(self.login_pwd)
        self.wait_ele(element_loc.login_button).click()
        self.wait_ele(element_loc.home_button).click()
        sleep(1)

    def sou_suo(self):
        """
        按条件搜索
        :return: 返回搜索列表
        """
        self.wait_ele(element_loc.input_box).send_keys(self.context)
        self.wait_ele(element_loc.box_button).click()

    def screening(self):
        """筛选招聘信息"""
        self.wait_ele(element_loc.option_button).click()
        sleep(1)
        self.wait_ele(element_loc.release_data).click()
        sleep(1)
        self.wait_ele(element_loc.release_scope).click()
        sleep(1)
        self.wait_ele(element_loc.release_record).click()

    def apply(self):
        """投递简历"""
        page_list = self.wait_list(element_loc.pages_button)
        for page in page_list[1:-1]:
            print(page)
            # page.click()
            # sleep(3)
            # self.wait_ele(element_loc.select_button).click()
            # self.wait_ele(element_loc.job_button).click()

    def job_info(self):
        """保存查询信息"""
        page_list = self.wait_list(element_loc.pages_button)
        for page in page_list:
            job_list = self.wait_list(element_loc.job_number)
            name_list = self.wait_list(element_loc.name)
            addr_list= self.wait_list(element_loc.addr)
            sal_list= self.wait_list(element_loc.salary)
            rel_time= self.wait_list(element_loc.release)
            count = 0
            for job in job_list:
                count += 1
                # 保存职位名称
                DoExcel(project_path.Excel_path).write_back("info", count+1, 1, job.get_attribute('title'))
                # 保存公司名称
                DoExcel(project_path.Excel_path).write_back("info", count+1, 2, name_list[count-1].get_attribute('title'))
                # 保存公司地址
                DoExcel(project_path.Excel_path).write_back("info", count+1, 3, addr_list[count-1].text)
                # 保存薪资信息
                DoExcel(project_path.Excel_path).write_back("info", count+1, 4, sal_list[count-1].text)
                # 保存发布时间
                DoExcel(project_path.Excel_path).write_back("info", count+1, 5, rel_time[count-1].text)


if __name__ == '__main__':
    p = Janli(Chrome())
    p.login()
    p.sou_suo()
    p.screening()
    sleep(3)
    p.apply()
    # p.job_info()
    p.driver.quit()