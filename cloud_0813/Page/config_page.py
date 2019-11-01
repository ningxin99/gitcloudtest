# coding=utf-8
"""
@author: Tracy
@mail: zhouxihong@ruijie.com.cn
@date: 2019.07.16
"""
# 删除SSID
config_ssid_delete = "//table[@id='ssidTable']/tbody/tr[1]/td[8]/a[@class='icon icon-delete delSSID']"
# 编辑SSID
config_ssid_edit = "//table[@id='ssidTable']/tbody/tr[1]/td[8]/a[1]"
# 点击hidden下拉框
config_ssid_hidden = "//select[@id='ishidden']"
# 点击yes
config_ssid_hidden_yes = "//select[@id='ishidden']/option[2]"
# 点击转发方式
config_ssid_forward = "//select[@id='fowardType']"
# 选择转发方式为nat
config_ssid_forward_nat = "//select[@id='fowardType']/option[1]"
# 选择转发方式为brideg
config_ssid_forward_bridge = "//select[@id='fowardType']/option[2]"
# 点击NAT address pool configuration
config_ssid_forward_nat_pool_config = "//*[@id='natConfig']"
# 选择common address pool
config_ssid_forward_nat_pool_config_select = "//input[@id='J_nat_devices']"
config_ssid_forward_nat_pool_config_click = "//*[@id='J_natConfig_config_ips_btn']/span"
# 输入nat地址池网段
config_ssid_forward_nat_pool_config_network = "//input[@id='J_natConfig_netSegment']"
# 输入nat地址池掩码
config_ssid_forward_nat_pool_config_submask = "//input[@id='J_natConfig_mask']"
# 选择漫游地址池
config_ssid_forward_nat_pool_roam = "//input[@id='J_nat_network']"
# 输入vlan id
config_ssid_forward_bridge_vlan = "//input[@id='vlanId']"
# 关闭radio 2
config_ssid_radio_2 = "//div[@id='radioInfo2']//div[@class='col-xs-6']/label"
# 关闭radio 1
config_ssid_radio_1 = "//div[@id='radioInfo1']//div[@class='col-xs-6']/label"

# 输入radio 1 支持的最大客户端数
config_ssid_radio_1_max_client = "//input[@id='usersLimit1']"
# 输入radio 2 支持的最大客户端数
config_ssid_radio_2_max_client = "//input[@id='usersLimit2']"


# 点击加密方式
config_ssid_encryption = "//select[@id='encryptionMode']"
# 选中wpa-psk的加密方式
config_ssid_encryption_wpa_psk = "//select[@id='encryptionMode']/option[2]"
config_ssid_encryption_wpa2_psk = "//select[@id='encryptionMode']/option[3]"
config_ssid_encryption_wpa_wpa2_psk = "//select[@id='encryptionMode']/option[4]"
config_ssid_encryption_ppsk = "//select[@id='encryptionMode']/option[6]"
# 输入密码
config_ssid_encryption_wpa_psk_password = "//input[@id='password']"
# 选中802.1x的加密方式
config_ssid_encryption_802x = "//select[@id='encryptionMode']/option[5]"
# 添加802.1x服务器

# 点击5G优先
config_ssid_band = "//div[@id='ssid-panel']/div[@class='col-xs-12 form-group'][1]//label"
# 点击基于客户端限速
config_ssid_rate_client = "//div[@id='ssid-panel']/div[4]//label"
config_ssid_rate_client_upRate = "//input[@id='upRate']"
config_ssid_rate_client_downRate = "//input[@id='downRate']"
# 点击基于SSID限速
config_ssid_rate_ssid = "//div[@id='ssid-panel']/div[@class='col-xs-12 form-group'][3]//label"
config_ssid_rate_ssid_wlan_upRate = "//input[@id='wlanUpRate']"
config_ssid_rate_ssid_wlan_downRate = "//input[@id='wlanDownRate']"

# 点击more
config_ssid_more = "//button[@id='toMore']"
# 点击从其他分组导入配置
config_ssid_more_import = "//li[@id='toCopy']/a"
# SSID列表第一个SSID名称
config_ssid_tr1_name = "//table[@id='ssidTable']/tbody/tr[1]/td[2]"
# 选择从哪个分组导入配置
config_ssid_more_import_select_group = '//*[@id="svg_selectGroup"]//*[text()="{}"]'

# 选择高级
config_basic_advance = "//div[@id='advancedColse']/h3"
# 点击添加白名单
config_basic_advance_add_white = "//span[@id='addWhite']/i"
# 输入白名单ip
config_basic_advance_add_white_ip = "//input[@id='addr']"


"""voucher package"""
# 点击voucher
config_voucher = "//*[@id='config_authentication_voucher_menu']"
# 点击manage package
config_manage_package = "//button[@id='manageProfile']"
# 点击add package
config_add_package = "//button[@id='addProfile']"
# 输入package名称
config_package_name = "//input[@id='profileName']"
# 输入价格
config_package_price = "//input[@id='price']"
# 输入package des
config_package_des = "//input[@id='profileDesc']"
# 点击最大连接终端数为1台
config_package_max_client_1 = "//select[@id='numberOfdevices']/option[2]"
# 点击最大连接终端数为2台
config_package_max_client_2 = "//select[@id='numberOfdevices']/option[3]"
# 选择时长
config_package_period = "//select[@id='timeperiod']"
# 选择时长为1周
config_package_period_week = "//select[@id='timeperiod']/option[7]"
# 选择时长为1天
config_package_period_day = "//select[@id='timeperiod']/option[5]"
# 选择可用流量
config_package_quota = "//select[@id='dataquota']"
# 选择可用流量为500M
config_package_quota_500 = "//select[@id='dataquota']/option[4]"
# 选择可用流量为1G
config_package_quota_G = "//select[@id='dataquota']/option[5]"
# 选择最大下载速度
config_package_max_download_rate = "//select[@id='maxDownload']"
# 选择最大下载速度为2M
config_package_max_download_rate_2M = "//select[@id='maxDownload']/option[5]"
config_package_max_download_rate_256k = "//select[@id='maxDownload']/option[2]"
# 选择最大上传速度
config_package_max_upload_rate = "//select[@id='maxUpload']"
# 选择最大上传速度为2M
config_package_max_upload_rate_2M = "//select[@id='maxUpload']/option[5]"
config_package_max_upload_rate_5M = "//select[@id='maxUpload']/option[6]"
# 点击OK
# 获取package的信息
config_package_list = "//table[@id='profile_table']/tbody/tr/td[{}]"
config_package_list_tr = "//table[@id='profile_table']/tbody/tr"
# 点击删除package list第二行
config_package_tr1_delete = "//table[@id='profile_table']/tbody/tr[1]/td[10]/a[2]"
# 点击编辑package list第一行
config_package_tr1_edit = "//table[@id='profile_table']/tbody/tr[1]/td[10]/a[1]"
# 定位到package搜索框
config_package_search = "//input[@id='profile_qs_name']"

"""voucher"""
# 点击打印voucher
config_voucher_print = "//button[@id='printVoucher']"
# 输入voucher名字
config_voucher_name = "//input[@id='nameRef']"
# 点击multipl voucher
config_voucher_multiple = "//button[@id='multipleVoucher']"
# 输入voucher 数量
config_voucher_multiple_quantity = "//input[@id='quantity']"
# 点击print
config_voucher_key_print = "//button[@id='singleVoucherPrint']"
# 生成多个voucher点击打印
config_voucher_key_print_multiple = "//button[@id='multipleVoucherPrint']"
# 打印出voucher后返回点击voucher
config_voucher_print_return = "//*[@id='printVoucherTitle']/h3"
# 点击刷新
config_voucher_list_refresh = "//*[@id='voucher_js_refresh']/i"
# voucher list列表
config_voucher_list_tr = "//table[@id='voucher_table']/tbody/tr[1]/td[{}]"
# voucher list列表中的生成时间
config_voucher_list_time = "//table[@id='voucher_table']/tbody/tr/td[7][contains(text() , '{}')]"
# 第一个voucher code
config_voucher_code = "//table[@id='voucher_table']/tbody/tr[1]/td[2]"
# 定位voucher搜索框
config_voucher_search = "//input[@id='voucher_qs_name']"
# voucher list长度
config_voucher_tr_len = "//table[@id='voucher_table']/tbody/tr"


"""PPSK"""
# 点击ppsk
config_ppsk = "//a[@id='config_authentication_ppsk_menu']"
# 点击添加ppsk账号
config_ppsk_add_account = "//button[@id='J_ppsk_add_btn']"
config_ppsk_alert_add_account = "//button[@id='singleImp']"
# 输入ppsk账号
config_ppsk_alert_ppsk_name = "//input[@id='J_ppsk_name_1']"
# 点击ok键
# 输入绑定的mac地址
config_ppsk_bind_mac = "//table[@id='ppskList_table']/tbody/tr/td[3]/input"
# 点击bind
config_ppsk_bind_button = "//table[@id='ppskList_table']/tbody/tr/td[3]/button"
# 获取ppsk list的
config_ppsk_list_tr_name = "//table[@id='ppskList_table']/tbody/tr/td[2]"
config_ppsk_list_tr_time = "//table[@id='ppskList_table']/tbody/tr/td[5]"
config_ppsk_list_tr_mac = "//table[@id='ppskList_table']/tbody/tr/td[3]"
# 配置SSID为PPSK认证
config_basic_ppsk = "//select[@id='encryptionMode']/option[6]"
# 查看ppsk同步状态
config_ppsk_list_action_check = "//table[@id='ppskList_table']/tbody/tr/td[6]/a[1]"
config_ppsk_SYNCED = "//table[@id='viewModalList_table']/tbody/tr/td[2]"
# 关闭同步状态页面
config_ppsk_list_check_close = "//div[@class='modal-header']/button[@class='close']/span"


"""group"""
# 进入group页面点击more
config_group_more = "//button[@id='J_more_btns']"
# 点击添加子分组
config_group_more_subgroup = "//li[@id='addSubGroup']/a"
# 输入子分组名称
config_group_subgroup_add = "//input[@id='groupName']"
# 点击保存
config_group_subgroup_add_save = "//button[text()='Save & Next']"
# 点击添加设备
config_group_more_add_device = "//li[@id='addDevice']/a"
# 点击编辑
config_group_more_edit = "//li[@id='editGroup']/a"
# 点击config
config_group_more_config = "//li[@id='configGroup']/a"
# 找到config页面的SSID列表
config_group_more_config_ssid_list = "//table[@id='ssidTable']/tbody/tr"
# 点击删除
config_group_more_delete = "//li[@id='deleteGroup']/a"
# 进入group页面，查看某分组的设备数量
config_group_device_num = '//*[@id="svg"]//*[text()="{}"]/following-sibling::*[1]'
# 进入编辑分组页面,输入分组名称
config_group_edit_name = "//input[@id='J_network_groupName']"
# 进入编辑分组页面,选择时区
config_group_edit_time_zone = "//select[@id='time_zone']/option[1]"
# 进入编辑分组页面,选择位置
config_group_edit_location = "//input[@id='location']"
# 点击保存
config_group_edit_save = "//button[@id='editSave']"
# 点击展开子分组
config_group_subgroup_unfold = "//button[@id='unfold']"
# 点击收起子分组
config_group_subgroup_fold = "//button[@id='fold']"
# 点击搜索
config_group_search = "//span[@id='select2-search_group2-container']"
# 定位搜索框
config_group_search_input = "//span//input"
# 定位到搜索到的元素
config_group_search_ele = '//*[@id="svg"]//*[text()="{}"]/preceding-sibling::*[3][@stroke= "#56b9fd"]'
# 删除
config_group_delete = "//*[@id='floatDeleteGroup']"
config_group_config = "//*[@id='floatConfigDevice']"
config_group_edit = "//*[@id='floatEditDevice']"
config_group_add_device = "//*[@id='floatAddDevice']"
# 点击添加子分组
config_group_subgroup = "//*[@id='floatAddSubGroup']"
# 点击展开子分组
config_group_subgroup_open = '//*[@id="svg"]//*[text()="{}"]/following-sibling::*[2]'
# 点击保存
config_group_sugroup_save = "//button[@id='btnApplyAdd1']"

"""RF planning"""
# 点击RF planning
config_RF_planning_xpath = "//*[@id='config_wireless_rfplanning_menu']"
# 选择2.4G信道
config_RF_radio1_bandwidth_2 = "//select[@id='J_2Gbindwidth']/option[3]"
# 选择5G信道
config_RF_radio2_bandwidth_5 = "//select[@id='J_5Gbindwidth']/option[3]"
# 选择5G信道
config_RF_radio3_bandwidth_5 = "//select[@id='J_5Gbindwidth_radio3']/option[3]"
# 点击保存
config_RF_radio_save = "//button[@id='J_radioCountry_save']"

# 选择AP配置power
config_RF_select_ap = "//table[@id='rfplanList_table']/tbody/tr/td/input"
# 配置radio1 power
config_RF_radio1_power = "//input[@id='J_1_power']"
# 配置radio2 power
config_RF_radio2_power = "//input[@id='J_2_power']"
# 配置radio1 信道
config_RF_radio1_channel_3 = "//select[@id='J_1_channel']/option[4]"
# 配置radio2 信道
config_RF_radio2_channel_157 = "//select[@id='J_2_channel']/option[23]"
# 点击apply
config_RF_radio_power_apply = "//input[@id='J_UpdataPrototyep']"
"""Bluetooth"""
# 点击左边菜单Bluetooth
config_bluetooth_xpath = "//*[@id='config_wireless_bluetooth_menu']"
# 点击添加蓝牙
config_bluetooth_add = "//button[@id='J_bluetooth_add_btn']"
# 输入设备SN
config_bluetooth_add_sn = "//input[@id='J_buletooth_sn']"
# status on
config_bluetooth_add_statue_on = "//div[@id='J_tpl_content']/div/div/div/label"
# 输入UUID
config_bluetooth_add_UUID = "//input[@id='J_buletooth_uuid']"
# 输入major
config_bluetooth_major = "//input[@id='J_buletooth_major']"
# 输入minor
config_bluetooth_minor = "//input[@id='J_buletooth_minor']"
# 点击保存
config_bluetooth_save = "//button[@id='J_saveBluetoothConfig']"
