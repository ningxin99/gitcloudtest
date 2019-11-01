# coding=utf-8
"""
@author: tracy
@mail: zhouxihong@ruijie.com.cn
@date: 2019.04.29
"""
import datetime

"""
基本信息，必填!
"""
 # "https://cloud-as.ruijienetworks.com"
 # "https://cloudtest-as.ruijienetworks.com"
 # "http://172.17.126.124"
login_url_local = "https://cloud-as.ruijienetworks.com"
# 登录cloud账号
# 登陆cloud密码
user_cloud_local = '321162718@qq.com'
password_cloud_local = 'why961113'
# 运行的用例名称，将会运行该文件夹下面的所有用例
run_case_name = "cloud"
# 接收测试报告的邮箱,多个邮箱用;隔开
email_name = "321162718@qq.com;why119613@163.com"

# 添加设备AP SN号
add_device_alert_input_sn = '1234942570026'
add_device_alert_input_sn_710 = 'G1L919900130B'
add_device_alert_input_sn_720 = 'G1LQ68P01315B'
add_device_alert_input_sn_740 = '1234942570014'
# 添加的交换机SN
add_device_alert_input_sn_switch ='G1LL64B000501'
#'1234567897412'
# 添加的EG SN
add_device_alert_input_sn_gateway ='H1M722K000264'
#  'H1K90RR000172'
#  'H1K90RR000172'
#  'H1MSC0M000147'
#  'H1M722K000263'
"""
基本信息，必填!
"""







# 账号，密码
login_user_name_data_11 ="2694707305@qq.com"
login_password_data_11 = "why961113"
# user_cloud = "2694707305@qq.com"
# password_cloud = "why961113"
# 添加分组
add_groups_input_name_data = 'test_00021'
# ssid名称
add_SSID_ssid_name_default = '@test_default'
add_SSID_ssid_name = '@test_wpa'

add_SSID_ssid_name_one_click = "@test_one_click"

# web password
add_SSID_web_password = 'ruijie123'

# telnet password
add_SSID_telnet_password = 'ruijie123'

# 添加的分组数目
group_num = 20

# 添加的SSID数目
ssid_num = 20

# 选择一个分组配置SSID
choose_group_config_ssid = 'test_0617'

# EG密码
add_device_alert_input_password = 'ruijie123'

# wifi名
wifi_name = "cloud_wifi"

# 现在时间
now_time = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
now_time_day = datetime.datetime.now().strftime('%Y-%m-%d')
now_time_s = datetime.datetime.now().strftime('%H-%M-%S')

# 子分组
sub_group_name_data = 'sub_'