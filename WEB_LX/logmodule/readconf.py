from configparser import ConfigParser


class configfile:
    def __init__(self,filename):
        self.cf=ConfigParser()
        self.cf.read(filename,encoding='utf-8')

    def readfile(self,section,option):
        value=self.cf.get(section,option)
        return value

    def readdata(self,section,option):
        value=self.cf.get(section,option)
        return eval(value)


if __name__ == '__main__':
    cf = ConfigParser()
    cf.read('log.ini',encoding='utf-8')
    # p.readfile('LOG','filename')
    # 读取所有section
    # print(cf.sections())
    # 读取所有option
    # print(cf.options('LOG'))
    # 添加section
    # cf.add_section('test')
    # cf.write(open('log.ini','w+',encoding='utf-8'))
    # 添加option
    # cf.set('test','name','xiaoming')
    # cf.write(open('log.ini', 'w+'))
    # 修改option
    # cf.set('test','age','18')
    # cf.write(open('log.ini', 'w+',encoding='utf-8'))
    # 删除option
    # cf.remove_option('test','age')
    # cf.write(open('log.ini', 'w+'))
    # 删除section
    cf.remove_section('test')
    cf.write(open('log.ini', 'w+'))