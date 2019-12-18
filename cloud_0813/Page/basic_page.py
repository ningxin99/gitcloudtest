# coding=utf-8
"""
@author: zhouxihong
@mail: zhouxihong@ruijie.com.cn
@date: 2019.4.29
"""

# 登陆用户名xpath
user_name_xpath = '//input[@id="username"]'
# 登陆密码xpath
password_xpath = '//input[@id="password"]'
# 登陆按钮
# login_btn_xpath = '//button[@id="btnLogin"]'
login_btn_xpath = "//input[@id='J_userLogin_btn']"
# 登陆后有一个关闭页面
# login_close_tips_xpath = '//div[@class="modal-content"]//button[@class="close"]'
login_close_tips_xpath = '//button[@id="maccUpgradeOk"]'

"""配置"""
# 点击配置页面
configuration_page_xpath = '//li[@id="config_menu1"]'
# 点击小组
groups_page_xpath = '//*[@id="config_groups_menu"]'
# 点击添加小组
add_groups_xpath = '//*[@id="addNetwork"]'
# 点击配置里面的基本
configuration_basic_xpath = "//*[@id='config_menu']/li[2]/div/a[@id='config_wireless_basic_menu']"

# 添加小组页面
# 点击输入组名
add_groups_input_name_xpath = '//*[@id="J_network_groupName"]'
# 下一步
add_groups_next_page_xpath = '//*[@id="wifiBtn"]'
# 默认的SSID输入框
add_groups_add_wifi_name_default = "//input[@id='J_netconfig_ssidName_1']"
# 点击添加wifi
add_groups_add_wifi = "//button[@id='addWifiBtn']"
# 输入第2个wifi名
add_groups_add_wifi_name = "//input[@id='J_netconfig_ssidName_2']"
# 点击应用
add_groups_apply_xpath = '//*[@id="applyBtn"]'
# 关闭添加分组页面
add_groups_page_close = "//*[@class='modal fade in']//button[@class='close']"
# 添加AP设备页面
add_group_device_ap = "//ul[@id='changeDeviceType']/li[1]/a"
# 输入AP s/n
add_device_input_sn_xpath = '//*[@id="J_devices_sn_2"]'
# 输入AP别名
add_device_input_alias_xpath = "//input[@id='J_devices_name_2']"
# 添加交换机设备页面
add_group_device_sw = "//ul[@id='changeDeviceType']/li[2]/a"
# 输入交换机SN
add_device_input_sn_sw_xpath = "//*[@id='J_switch_sn_2']"
# 输入交换机别名
add_device_input_alias_sw_xpath = "//input[@id='J_switch_name_2']"
# 添加EG页面
add_group_device_eg = "//ul[@id='changeDeviceType']/li[3]/a"
# 输入EG SN
add_device_input_sn_eg_xpath = "//*[@id='J_devices_GATEWAY_sn_1']"
# 输入EG别名
add_device_input_alias_eg_xpath = "//input[@id='J_devices_name_1']"
# 输入EG 密码
add_device_input_password_eg_xpath = "//*[@id='J_devices_userPassword_1']"
# 添加设备应用界面
add_device_apply_xpath = '//*[@id="btnApplyAdd1"]'
# 关闭添加设备页面(/div[@class='modal-header']/button[@class='close']/span)
add_device_close_xpath = '//*[@class="modal-header"]//*[@class="close"]'


# 选中分组(//svg[@id='svg']/rect[-1])
select_group_xpath = '//*[@id="svg"]//*[text()="{}"]'
select_group_xpath_1 = "//svg[@id='svg']/rect[-1]"
select_group_xpath_2 = "//*[@id='svg']//*[text()={}]"
# 选择设置
select_setting_btn_xpath = '//*[@id="floatConfigDevice"]'
# 选择删除
select_delete_btn_xpath = "//*[@id='floatDeleteGroup']"
# 选择确认删除
select_delete_confirm = "//button[contains(text(),'OK')]"
# 添加SSID
add_group_xpath = '//*[@id="addSSID"]'
# 点击输入SSID
add_SSID_name = '//input[@id="ssidName"]'
# 配置psk认证
add_SSID_open = "//select[@id='encryptionMode']"
add_SSID_WPA2_PSK = "//option[@value='WPA2_PSK']"
add_SSID_WPA2_PSK_1 = "//select[@id='encryptionMode']/option[@value='wpa2-psk']"
add_SSID_WPA2_PSK_password = "//input[@id='password']"
# 配置转发方式
add_SSID_forward = "//select[@id='fowardType']"
add_SSID_forward_1 = "//select[@id='fowardType']//option[@value='nat']"
add_SSID_forward_nat = "//option[@value='nat']"
# 点击使能认证功能
add_SSID_enable_auth = '//*[@id="authSwitch"]//label'
# 点击一键认证
add_SSID_one_click_login = '//label[contains(text(),"One-click Login")]'
# 点击SSID配置ok
add_SSID_save_ssid = '//*[@id="saveSSID"]'
# 点击安全密码配置
add_SSID_security = "//*[@id='securityColse']//*[@class='panel-title color-gray']"
# 输入web password
add_SSID_security_web_password = "//input[@id='webPassword']"
# 输入telnet密码
add_SSID_security_telnet_password = "//input[@id='telnetPassword']"
# 保存SSID配置
add_SSID_save = "//button[@id='toSave']"
# 编辑SSID配置
edit_SSID_config = "//*[@id='ssidTable']//tbody//a[1]"
# 删除SSID
delet_SSID_config = "//*[@id='ssidTable']//tbody//a[2]"
# 确认删除该SSID
delet_SSID_confirm = "//button[contains(text(),'OK')]"


"""
监控
"""
# 点击监控
add_device_monitoring = '//*[@id="monitor_menu1"]'
# 点击选择分组
add_device_select_group = "//*[@id='groupBlock']//*[@class='form-group']//a"
# 选组分组可滚动区域
add_device_select_group_filed = "//section[@class='group-droupdown']"
# 点击新建的分组
add_device_new_group = '//section[@class="group-droupdown"]//*[@name="110"]'
# 点击AP
add_device_access_point = "//*[@id='monitor_device_accesspoint_menu']"
# 点击Switch
add_device_switch = "//*[@id='monitor_device_switch_menu']"
# 点击EG
add_device_gateway = "//*[@id='monitor_device_gateway_menu']"
# 点击添加AP
add_device_add_access_point = "//button[@id='importDev']"
# 点击添加switch
add_device_add_switch = "//*[@id='addSwitch']"
# 点击添加EG
add_device_add_gateway = "//button[@id='addGateway']"
# 弹框，点击添加AP/SW
add_device_alert_add_access_point = "//button[@id='singleImp']"
# 点击添加AP "+"
add_device_alert_add_ap = "//ul[@id='J_devices_List']//span[@class='devices_option item list-option'][2]/span"
# 点击添加SW "+"
add_device_alert_add_sw = "//div[@id='switchPanel']/ul[@id='J_switch_List']//span[@class='switch_option item list-option'][2]/span"
# excel上传AP设备
add_device_AP_excel = "//div[@id='picker']//input"
# driver.findElement(add_device_AP_excel).sendKeys("C:\Users\32116\Downloads\lllllll_14022_template.xls");

# 输入AP SN
add_device_alert_sn = "//input[@id='J_devices_sn_1']"
add_device_alert_sn_12 = "//input[@id='J_devices_sn_2']"
add_device_alert_sn_13 = "//input[@id='J_devices_sn_3']"
add_device_alert_sn_14 = "//input[@id='J_devices_sn_4']"
add_device_alert_sn_15 = "//input[@id='J_devices_sn_5']"
add_device_alert_sn_16 = "//input[@id='J_devices_sn_6']"
add_device_alert_sn_17 = "//input[@id='J_devices_sn_7']"
add_device_alert_sn_18 = "//input[@id='J_devices_sn_8']"
add_device_alert_sn_19 = "//input[@id='J_devices_sn_9']"

# 输入switch SN
add_device_alert_sn_switch = "//input[@id='J_switch_sn_2']"
add_device_alert_sn_3 = "//input[@id='J_switch_sn_3']"
add_device_alert_sn_4 = "//input[@id='J_switch_sn_4']"
add_device_alert_sn_5 = "//input[@id='J_switch_sn_5']"
add_device_alert_sn_6 = "//input[@id='J_switch_sn_6']"
add_device_alert_sn_7 = "//input[@id='J_switch_sn_7']"
add_device_alert_sn_8 = "//input[@id='J_switch_sn_8']"
add_device_alert_sn_9 = "//input[@id='J_switch_sn_9']"
add_device_alert_sn_10 = "//input[@id='J_switch_sn_10']"
# 输入EG SN
add_device_alert_sn_gateway = "//input[@id='J_devices_GATEWAY_sn_1']"
# 输入EG密码
add_device_alert_password = "//input[@id='J_devices_userPassword_1']"
# 输入EG 别名
add_device_alert_eg_alias = "//input[@id='J_devices_name_1']"
# 点击ok保存所添加AP
add_device_alert_save = "//button[@id='J_DevsAdd']"
# 删除AP
add_device_delete_1 = "//*[@id='devicesList_table']//tr[1]/td[15]/i[@class='icon icon-delete']"
add_device_delete_2 = "//*[@id='devicesList_table']//tr[2]/td[15]/i[@class='icon icon-delete']"
# 确认删除
add_device_confirm = "//button[@class='btn btn-default'][1]"
# 点击ok保存所添加switch
add_device_alert_save_switch = "//button[@id='J_SwitchAdd']"
# 点击ok保存所添加EG
add_device_alert_save_gateway = "//button[@id='singleImp']"
# 退出添加设备弹框
add_device_alert_exit = "//div[@class='modal-header']/button[@class='close']/span"
# 找到在线的AP设备
add_device_online_ap ="//table[@id='devicesList_table']//tbody//*[@class='icon icon-determine']"
# add_device_online_ap = "//tr[@data-index=0]//*[@class='columns-minwidth']"
# 找到在线的sw
add_device_online_sw = "//table[@id='switch_table']//tbody//*[text()='Online']"
# 找到在线的EG设备
add_device_online_eg = "//table[@id='gateway_table']//tbody//*[text()='Online']"
# 找到已同步的设备
add_device_synced = "//*[@id='devicesList_table']//tbody//*[text()='synced']"
add_device_Synchronized = "//*[@id='devicesList_table']//tbody//*[text()='Synchronized']"
# 找到同步失败的设备
add_device_Sync_Failed = "//*[@id='devicesList_table']//tbody//*[text()='Sync Failed']"
# 找到设备类别第一行显示同步状态的列
add_device_state = "//*[@id='devicesList_table']//tbody//tr[1]/td[4]"
# 进入设备详情
add_device_device_info = "//table[@id='devicesList_table']//*[text()='{}']"
# 进入配置同步状态页面
add_device_syned = "//text[@id='configStatusWin_0']"
# AP设备详情页面的SSID
add_device_device_info_SSID = "//ul[@id='ssid']/li"
# AP设备详情页面设备SN
add_device_device_info_SN = "//span[@id='sn']"
# AP设备详情页面IP
add_device_device_info_IP = "//span[@id='MGMTIP']"
# model：
add_device_device_info_model = "//span[@id='ApModel']"
# AP设备详情页面软件版本
add_device_device_info_version = "//span[@id='sofrwareVersion']"
# AP设备mac地址
add_device_device_info_mac = "//*[@id='MAC']"
# 硬件版本
add_device_device_info_hardware = "//span[@id='hardwareVersion']"
# 5G信道
add_device_device_info_channel_5G = "//table[@id='radiolist_table']/tbody/tr[1]/td[2]"
# 5G带宽
add_device_device_info_bandwidth_5G = "//table[@id='radiolist_table']/tbody/tr[1]/td[4]"
# 2.4信道
add_device_device_info_channel_2 = "//table[@id='radiolist_table']/tbody/tr[2]/td[2]"
# 2.4带宽
add_device_device_info_bandwidth_2 = "//table[@id='radiolist_table']/tbody/tr[2]/td[4]"
# log条数
add_device_log_list = "//table[@id='deviceconfig_table']/tbody/tr"


# 关闭设备详情页面
add_device_device_info_close = "//*[@class='modal-header']//*[@class='close']"
# 进入SW详情
add_device_SW_info = "//table[@id='switch_table']//*[text()='{}']"
# SW 的model
add_device_SW_info_model = "//*[@id='switch_detail_productClass']"
# SW的SN
add_device_SW_info_SN = "//*[@id='switch_detail_serialNumber']"
# SW的mac
add_device_SW_info_mac = "//*[@id='switch_detail_mac']"
# SW 的软件version
add_device_SW_info_version = "//*[@id='switch_detail_softwareVersion']"




# 点击进入EG详情
add_device_eg_info = "//table[@id='gateway_table']//*[text()='{}']"
# EG 的model
add_device_EG_info_model = "//*[@id='gateway_detail_productClass']"
# EG的SN
add_device_EG_info_SN = "//*[@id='gateway_detail_serialNumber']"
# EG的mac
add_device_EG_info_mac = "//*[@id='gateway_detail_mac']"
# EG的version
add_device_EG_info_version = "//*[@id='gateway_detail_softwareVersion']"





# 断言（添加的SSID）
add_SSID_field = "//*[@id='ssidTableContainer']//*[@class='fixed-table-body']//tbody//tr"

# 断言（添加的设备）
add_device_field = "//table[@id='devicesList_table']//tbody//tr"
# 选中所有设备
device_all_select = "//table[@id='devicesList_table']/thead/tr/th[1]//input"
# 选中设备
device_select = "//table[@id='devicesList_table']/tbody/tr[1]/td[1]/input"
# 点击more
#  device_more = "//div[@class='row COMMON']//button[@class='btn moreOperate dropdown-toggle']"
device_more = "//div[@id='devicesList_container']//button[text()='More']"
# 点击删除
device_delete = "//li[@id='delDev']/a"
# 点击移动分组
device_move = "//li[@id='moveDevTo']/a"
# 点击诊断工具
device_diagnosis = "//li[@id='diagnosisAp']"
# 点击重启
device_restart = "//li[@id='restartAp']/a"
# 点击确定重启
key_OK = "//button[text()='OK']"
ppsk_key_OK = "//*[text()='OK']"
whitelist_key_OK = "//*[text()='OK']"
# 点击running config
device_running_config = "//ul[@class='cli-item']/li[2]"
# 点击Web CLI
device_web_cli = "//span[text()= 'Web CLI']"
# 点击web Cli的二级菜单
device_web_cli_2 = "//ul[@class='cli-item']//span[text()= 'Web CLI'][1]"
# 命令输入框
device_web_cli_cmd = "//input[@id='cli_txt']"
# 点击version
device_running_version = "//ul[@class='cli-item']/li[1]"
# 点击send 命令
device_web_cli_cmd_send = "//button[@id='send_btn']"
# 点击WLAN
device_diagnosis_wlan = "//ul[@class='row-ul clear']/li[1]//li[5]"
# 点击MbSSID
device_diagnosis_wlan_mbssid = "//ul[@class='row-ul clear']/li[2]//li[1]"
# 关闭诊断工具
device_diagnosis_close = "//*[@class='modal fade in']//button[@class='close']"
device_eg_diagnosis_close = "//*[@class='modal fade in'][2]//button[@class='close']"
# 选中交换机设备
sw_select = "//table[@id='switch_table']/tbody/tr[1]/td[1]/input"
# 点击more
sw_more = "//div[@id='switch_container']//button[text()='More']"
# 点击诊断工具
sw_diagnosis = "//li[@id='diagnosisSwitch']/a"
# 点击runningconfig,同AP
# 选中EG设备
eg_select = "//table[@id='gateway_table']/tbody/tr[1]/td[1]/input"
# 点击more
eg_more = "//div[@id='gateway_container']//button[text()='More']"
# 点击诊断工具
eg_diagnosis = "//li[@id='diagnosisGateway']"
# 点击删除(先点击more)
eg_delete = "//li[@id='delGateway']/a"
eg_unauth_delete = "//*[@id='gatewayVerify_table']/tbody/tr/td[6]/a[@class='delverify']"
# 点击running config, 同AP
# 点击关闭命令行窗口
web_cli_close = "//div[@class='modal-header']/button[@class='close']/span"
# 点击维护
maintenance = "//*[@id='maintenance_menu1']"
# 点击配置日志
view_log_config_log = "//*[@id='maintenance_logs_configlog_menu']"
# 点击操作日志
view_log_operation_log = "//*[@id='maintenance_logs_operationlog_menu']"
# 点击升级日志
view_log_upgrade_log = "//*[@id='maintenance_logs_upgradelog_menu']"
# 点击刷新升级日志
view_log_upgrade_log_refresh = "//a[@id='upgradelog_refresh']"
# 日志信息
view_log_upgrade_log_success = "//table[@id='upgradelog_table']/tbody/tr[1]/td[6]/span[1][text()='1']"
view_log_upgrade_log_success_2 = "//table[@id='upgradelog_table']/tbody/tr[2]/td[6]/span[1][text()='1']"
view_log_upgrade_log_success_3 = "//table[@id='upgradelog_table']/tbody/tr[3]/td[6]/span[1][text()='1']"
view_log_upgrade_log_fail = "//table[@id='upgradelog_table']/tbody/tr[1]/td[6]/span[2][text()='1']"
# 定位到设备列表中的搜索框
upgrade_device_search = "//input[@id='devicesList_qs_key']"
# 设备列表长度
upgrade_device_tr_len = "//table[@id='devicesList_table']/tbody/tr"
# 设备列表中设备的SN
upgrade_device_tr1_sn = "//table[@id='devicesList_table']/tbody/tr/td[3]"
# 点击升级
upgrade_upgrade = "//*[@id='maintenance_upgrade_upgrade_menu']"
ap_firmware = "//table[@id='devicesList_table']/tbody/tr[1]/td[8]"
sw_firmware = "//table[@id='devicesList_table']/tbody/tr[2]/td[8]"
eg_firmware = "//table[@id='devicesList_table']/tbody/tr[3]/td[8]"
# 点击设备list当中的第一个设备升级
upgrade_device_01 = "//table[@id='devicesList_table']/tbody/tr[1]/td[11]/a"
upgrade_device_02 = "//table[@id='devicesList_table']/tbody/tr[2]/td[11]/a"
upgrade_device_03 = "//table[@id='devicesList_table']/tbody/tr[3]/td[11]/a"
upgrade_device_AP = "//table[@id='devicesList_table']/tbody//td[6][contains(text() , 'AP')]/following-sibling::td[5]"
upgrade_device_SW = "//table[@id='devicesList_table']/tbody//td[6][not(contains(text() , 'AP')) and not(contains(text() , 'EG'))]/following-sibling::td[5]"
upgrade_device_EG = "//table[@id='devicesList_table']/tbody//td[6][contains(text() , 'EG')]/following-sibling::td[5]"
upgrade_device_AP_v = "//table[@id='devicesList_table']/tbody//td[6][contains(text() , 'AP')]/following-sibling::td[2]"
upgrade_device_SW_v = "//table[@id='devicesList_table']/tbody//td[6][not(contains(text() , 'AP')) and not(contains(text() , 'EG'))]/following-sibling::td[2]"
upgrade_device_EG_v = "//table[@id='devicesList_table']/tbody//td[6][contains(text() , 'EG')]/following-sibling::td[2]"

# 得到设备列表中第一行model
upgrade_device_01_model = "//table[@id='devicesList_table']/tbody//tr[1]/td[6]"
upgrade_device_02_model = "//table[@id='devicesList_table']/tbody//tr[2]/td[6]"
upgrade_device_03_model = "//table[@id='devicesList_table']/tbody//tr[3]/td[6]"

# 选择版本
select_firmware = "//*[@id='border0']//button[@id='reselectVersion0']"
# 选择私有版本
select_firmware_private = "//span[@id='firmwareSelectTab']"
# 得到设备列表的行数
select_firmware_list_length = "//table[@id='firmwareSelect_table']/tbody/tr"
# 得到列表第一行设备的版本
select_firmware_list_tr1_td2 = "//table[@id='firmwareSelect_table']/tbody/tr[1]/td[2]"
# 得到列表所有行设备的版本
select_firmware_tr_td2 = "//table[@id='firmwareSelect_table']/tbody/tr[{}]/td[2]"
select_firmware_tr_td1 = "//table[@id='firmwareSelect_table']/tbody/tr[{}]/td[1]"
# 定位到版本号的哥哥节点
select_firmware_list_tr1_td1 = "//table[@id='firmwareSelect_table']/tbody/tr[1]/td[2]/preceding-sibling::td[1]/input"
select_firmware_list_tr_td1 = "//table[@id='firmwareSelect_table']/tbody/tr[{}]/td[2]/preceding-sibling::td[1]/input"
# 定位到列表第二行的第一列
select_firmware_list_tr2_td1 = "//table[@id='firmwareSelect_table']/tbody/tr[2]/td[1]/input"
select_firmware_list_tr2_td2 = "//table[@id='firmwareSelect_table']/tbody/tr[2]/td[2]"
# 点击开始升级
select_firmware_upgrade = "//div[@id='equipmentSelect_container']//button[@id='J_complete_equipmentSelect_forselect']"
# 点击完成
upgrade_finish = "//button[@id='J_complete_firmwareSelect_forselect']"



# 获取第一行日志的开始时间
view_log_config_log_start_time = '//*[@id="configlog_table"]//tbody//*[@data-index="0"]/td[3]'
# 获取第一行日志的结束时间
view_log_config_log_end_time = '//*[@id="configlog_table"]//tbody//*[@data-index="0"]/td[4]'
# 点击第一行配置日志的“+”
view_log_first_line_log = '//*[@id="configlog_table"]//tbody//*[@data-index="0"]//*[@class="detail-icon"]'
# 点击第一行配置日志的操作
view_log_first_line_action = '//*[@id="configlog_table"]//tbody//*[@class="detail-view"]//*[@class="icon icon-details"]'
# 获得详细日志表格
view_log_config_execution_list = '//*[@id="configlogdetail_table"]'

# 点击保存
key_save = "//button[text()='Save']"
config_ssid_forward_nat_pool_key_save = "//button[@class='btn btn-default pull-right ladda-button'][2]"


# 点击批量升级
upgrade_upgrade_all = "//button[@id='upgrade_all_dev']"
# 点击选择版本
select_firmware_batch = "//button[@id='reselectVersion{}']"
# current 版本
select_firmware_current_firmware = "//div[@id='border{}']/div/div/div[3]/span"