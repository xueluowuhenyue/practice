import  os
import time
path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
device_path=os.path.join(path,'Data','devices_info.yaml')
# print(device_path)