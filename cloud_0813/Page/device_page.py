# coding=utf-8
"""
@author: zhouxihong
@mail: zhouxihong@ruijie.com.cn
@date: 2019.4.29
"""

# device_ap
# 设备列表中第一行设备别名
device_alias = "//table[@id='devicesList_table']/tbody/tr[1]/td[6]/a"
# 输入设备别名
device_alias_input = "//table[@id='devicesList_table']/tbody/tr[1]/td[6]//form//input"
# 点击确定修改设备别名
device_alias_input_confirm = "//table[@id='devicesList_table']/tbody/tr[1]/td[6]//form//button[1]"
# 点击Manually Deliver
device_config_manually_deliver = "//span[@id='downConfig']"
# 点击刷新
device_config_refresh = "//span[@id='downConfig']"
# 弹框点击确定
# device_config_refresh_confirm = "//button[@class='btn btn-default xh-highlight']"
# 第1行的配置同步状态
device_config_state = "//table[@id='apConfigStatus_table']/tbody/tr[1]/td[3]/span"
# 关闭同步状态页面
device_config_state_page_close = "//div[@class='modal fade in']//button[@class='close']/span"
# 刷新设备列表
device_list_refresh = "//a[@id='devicesList_refresh']/i[@class='icon icon-refresh']"
# 设备列表第一行设备在线状态
device_list_tr1_state = "//table[@id='devicesList_table']/tbody/tr[1]/td[2]"
# 选中第一个分组（设备移动到第一个分组）
device_move_first_group = "//*[@id='svg_selectGroup']//*[6]"
# 点击OK，确认移动
device_move_confirm = "//button[@id='selectGroup_check']"
# 点击OK，确认移动
# 设备列表
device_list_tr = "//table[@id='devicesList_table']/tbody/tr"
# AP详情页面，CPU图形/memory/traffic
device_ap_detail_memory = "//*[@id='memoryUsage']/div/canvas"
device_ap_detail_cpu = "//*[@id='CPUUsage']/div/canvas"
device_ap_detail_traffic = "//*[@id='trafficStatistics']//canvas"



# device_SW
# 设备列表中第一行交换机别名
device_sw_alias = "//table[@id='switch_table']/tbody/tr[1]/td[5]/a"
# 输入设备别名
device_alias_sw_input = "//table[@id='switch_table']/tbody/tr[1]/td[5]//form//input"
# 点击确定修改设备别名
device_alias_sw_input_confirm = "//table[@id='switch_table']/tbody/tr[1]/td[5]//form//button[1]"
# 点击重启交换机
sw_restart = "//li[@id='restartSwitch']/a"
# 点击移动分组
device_sw_move = "//li[@id='changeSwitchGroup']/a"
# 交换机列表
device_sw_list_tr = "//table[@id='switch_table']/tbody/tr"

# 刷新交换机列表
device_sw_list_refresh = "//a[@id='switch_refresh']/i[@class='icon icon-refresh']"
# 交换机列表第一行的在线状态
device_sw_list_tr1_state = "//table[@id='switch_table']/tbody/tr/td[2]"
# 交换机详情页面cpu/memory/speed summary
device_sw_detail_memory = "//*[@id='memoryUsage']/div/canvas"
device_sw_detail_cpu = "//*[@id='cpuUsage']/div/canvas"
device_sw_detail_speed = "//*[@id='switch_detail_interface_Trend']//canvas"
# 交换机详情页面点击port
device_sw_detail_port = "//ul[@id='switch_detail_tab']/li[2]"
# 交换机详情页面点击config
device_sw_detail_config = "//ul[@id='switch_detail_tab']/li[3]"
# 点击添加vlan
device_sw_detail_vlan_add = "//button[@id='J_switch_vlan_add']"
# 输入vlan id
device_sw_detail_vlan_id = "//input[@id='J_switch_addVlanID']"
# 点击add
device_sw_detail_vlan_add_confirm = "//button[@id='J_save_switchVlan']"
# 点击last到最后一页
device_sw_detail_vlan_page_last = "//div[@id='vlan_container']//li[@class='last']/a"
# 删除添加的vlan
device_sw_detail_vlan_delete = "//table[@id='vlan_table']/tbody/tr/td[1][text()= '{}']/../td[3]/a"
# 定位到开启了RLDP的交换机接口
device_sw_detail_rldp_green = "//div[@id='rldp_SwitchPanel']//table/tbody/tr/td/div[contains(@class, 'green')]"
# 定位到没有up的交换机接口
device_sw_detail_int_down = "//div[@id='switchPanel']//table/tbody/tr/td/div[not(contains(@class, 'yellow')) and not(contains(@class, 'green'))][1]"
# 修改接口为trunk口
device_sw_detail_int_trunk = "//div[@id='switchPort_Config']/div/div/div[2]/div[2]/select/option[2]"
device_sw_detail_int_access = "//div[@id='switchPort_Config']/div/div/div[2]/div[2]/select/option[1]"
# 修改 trunk口native vlan id
device_sw_detail_int_trunk_native_vlan_id = "//div[@id='switchPort_Config']/div/div/div[2]/div[4]/input"
# 修改 access口vlan id
device_sw_detail_int_accesss_vlan_id = "//div[@id='switchPort_Config']/div/div/div[2]/div[3]/input"
# 点击保存端口配置
device_sw_detail_int_save = "//button[@id='savePortConfig']"
# 获取修改配置的端口名称
device_sw_detail_int_name = "//div[@id='switchPort_Config']/div/span"


# RLDP部分
# 点击使能RLDP
device_sw_RLDP_enable = "//div[@id='rldp_container']//span[@class='switch_Box']/label"
# 点击auto config
device_sw_RLDP_auto_config = "//input[@id='switch_rldp_onekeysavebtn']"



# device_EG
# 未认证EG列表SN
device_eg_un_sn = "//table[@id='gatewayVerify_table']/tbody/tr/td[1]"
device_eg_un_alias = "//table[@id='gatewayVerify_table']/tbody/tr/td[2]"
device_eg_un_state = "//table[@id='gatewayVerify_table']/tbody/tr/td[3]"
device_eg_un_group = "//table[@id='gatewayVerify_table']/tbody/tr/td[4]"
# 点击重新认证
device_eg_re_auth = "//table[@id='gatewayVerify_table']/tbody/tr/td[6]/a[1]"
# 输入密码
device_eg_re_password = "//div[@class='modal-content']/div[@class='modal-body']/div/input"
# 认证的EG列表第一行
device_eg_list_tr = "//table[@id='gateway_table']/tbody/tr"
# 点击EG的列表第一行的别名
device_eg_list_alias = "//table/tbody/tr/td[4]/a"
# 输入设备别名
device_eg_list_alias_input = "//table[@id='gateway_table']/tbody/tr[1]/td[4]//form//input"
# 确定输入设备别名
device_eg_list_alias_input_confirm = "//table[@id='gateway_table']/tbody/tr[1]/td[4]//form//button[1]"
# eg的日志信息列表
device_eg_list_log_tr = "//table[@id='deviceconfig_table']/tbody/tr"
# eg的应用排名列表
device_eg_list_application = "//div[@id='egTopAppFlowListContent']/div"
# eg的users排名列表
device_eg_list_users = "//div[@id='egTopUserFlowListContent']/div"
# 点击eg的诊断工具
device_eg_diagnosis_tool = "//button[@id='J_gateway_webCli']"
# 关闭EG的诊断工具
device_eg_diagnosis_tool_close = "//*[@class='modal fade in'][2]//button[@class='close']"
# 点击eg的EWEB
device_eg_EWEB = "//button[@id='J_gateway_apweb']"
# 点击eg的Telnet
device_eg_telnet = "//button[@id='J_gateway_tunnel_telnet']"
# eweb 连接成功web
device_eg_EWEB_logo_success = "//div[@id='diaglogContent']//i"
# 点击click here to open
device_eg_EWEB_click_here = "//div[@id='diaglogContent']/div/ul[@class='causeList']/li[5]/a"
# EGweb创建失败
devic_eg_EWEb_fail = "//div[@id='diaglogContent']//p[1]"
# EG web页面的元素
device_eg_EWEB_element = "//div[@id='view_area']"
# EG 登录页面元素
device_eg_EWEB_login_element = "//*[@id='reset_pass_div']"

# EG telnet 创建成功
device_eg_telnet_success = "//div[@id='diaglogContent']/div[1]/ul[@class='telnetInfo']/li[1]/p"
# 点击EG详情，more
device_eg_detail_more = "//button[@class='btn gatewayTileMoreOprate dropdown-toggle']"
# 点击EG重启
device_eg_restart = "//li[@id='J_gateway_restart']"
# 点击SSH
device_eg_ssh = "//li[@id='J_gateway_tunnel_ssh']/a"
# SSH内容
device_eg_ssh_content = "//div[@id='diaglogContent']/div/ul[@class='telnetInfo']/li[1]/p"
# 关闭SSH内容
device_eg_ssh_close = "//div[@class='modal-dialog modal-dialog-sm']/div[@class='modal-content']/div[@class='modal-header']/button[@class='close']/span"
# EG设备列表第一行设备在线状态
eg_list_tr1_state = "//table[@id='gateway_table']/tbody/tr[1]/td[2]"
# 点击编辑EG别名
device_eg_detail_alias_edit = "//i[@id='J_Dev_aliasEdit_btn']"
device_eg_detail_alias_input = "//input[@id='J_Dev_alias_input']"
device_eg_detail_alias_ok = "//i[@id='J_Dev_aliasOk_btn']"
# 点击编辑EG描述信息
device_eg_detail_des_edit = "//i[@id='J_edit_devRemark']"
device_eg_detail_des_input = "//input[@id='J_devRemark']"
device_eg_detail_des_ok = "//i[@id='J_save_devRemark']"
# eg别名
device_eg_detail_alias = "//span[@id='gateway_detail_aliasName']"
# eg描述信息
device_eg_detail_des = "//span[@id='gateway_detail_remark']"
# 点击修改EG密码
device_eg_detail_password = "//i[@id='J_edit_managePassword']"
device_eg_detail_password_input = "//input[@id='J_managePassword']"
device_eg_detail_password_ok = "//i[@id='J_save_managePassword']"
# 操作日志第一行描述信息
device_eg_operation_log_des = "//table[@id='operate_table']/tbody/tr[1]/td[4]"
# 操作日志第一行结果信息
device_eg_operation_log_result = "//table[@id='operate_table']/tbody/tr[1]/td[5]"
# 刷新操作日志
device_eg_operation_log_refresh = "//a[@id='operate_refresh']/i[@class='icon icon-refresh']"
# EG详情页面cpu/memory/rate summary
device_eg_detail_cpu = "//div[@id='cpuUsage']/div/canvas"
device_eg_detail_memory = "//div[@id='memoryUsage']/div/canvas"
device_eg_detail_rate_summary = "//div[@id='gatewayFlowALLTrend_chart']//canvas"