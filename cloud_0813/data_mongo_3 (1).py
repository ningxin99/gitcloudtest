# coding:utf-8
import uuid
import random
import uuid
import random
import pymongo
import json
from bson import ObjectId
import bson
from datetime import datetime

# 连接数据库服务器，获取客户端对象
conn = pymongo.MongoClient(host='172.18.24.111', port=27017)
# conn = pymongo.MongoClient("mongodb://172.18.24.111:27017/")
# conn = pymongo.MongoClient("mongodb://{macc}:{ma0c#2017#rjma0c#2017#rj}@172.18.24.111:27017")
conn.macc2.authenticate('macc', 'ma0c#2017#rj', mechanism='SCRAM-SHA-1')
# conn.macc2.authenticate("macc", "ma0c#2017#rjma0c#2017#rj", mechanism='MONGODB-CR')
db = conn['macc2']
collection_onofflineUser = db.onofflineUserHistory
collection_oui = db.oui
collection_terminalInfo = db.terminalInfo




ss = {
    "_id" : ObjectId("f70f449890dade33005fb6bc"),
    "mac" : "6453.a9c9.f70f",
    "uploadDate" : bson.int64.Int64("1574762805000"),
    "onlineTime" : datetime(2019,11,1,10,00,29,0),
    "sn" : "G1MQ4Q7068955",
    "updateTime" : datetime(2019,11,1,22,45,4,0),
    "offlineTime" :  datetime(2019,11,1,22,35,56,0),
    "userIp" : "192.168.9.25",
    "rssi" : "0",
    "rssiInt" : 0,
    "ssid" : "1123",
    "wifiUp" : bson.int64.Int64(1800),
    "wifiDown" : bson.int64.Int64(3480),
    "logType" : "off",
    "buildingId" : 33,
    "groupId" : 33,
    "tenantId" : 2,
    "buildingName" : "1029_720L",
    "wifiUpDown" :bson.int64.Int64(8220),
    "groupName" : "1029_720L",
    "deviceName" : "ap130",
    "deviceAliasName" : "ap130",
    "activeTime" : bson.int64.Int64(327000),
    "uplinkRate" : 0,
    "downlinkRate" : 0,
    "updownlinkRate" : 0,
    "band" : "5G",
    "macPrefix" : "6453.a9",
    "rawOffset" : 28800000,
    "utcCode" : 8,
    "systemOffset" : 0,
    "reasonSource" : "rsna",
    "reasonCode" : 1,
    "productType" : "AP"
}





terminalinfo_os_list = ['Android', 'IOS', 'Windows']
terminalinfo_id = '{"_id":"'
# ss_terminalinfo_id = mac
terminalinfo_os = '","termidVersion":"0","hardwareType":"Phone","osType":"'
# ss_terminalinfo_os
ss_terminalinfo = '","osVersion":"0","productModel":"0","termidString":"Phone Android ","capability":"2.4G"}'

oui_organizationEn_list = ['test_a', 'test_b', 'test_c', 'test_d']
oui_id = '{"_id":"'
# mac前6位2484.98
oui_organizationEn = '","organizationEn":"'
# ss_oui_organizationEn
oui_organizationCh = '","organizationCh":"'
ss_oui = '"}'
# {"_id":"001a.a2","organizationEn":"cisco","organizationCh":"思科"}


count_os = {'Andriod': 0, 'IOS': 0, 'Windows': 0}
count_organizationEn = {'test_a':0, 'test_b':0, 'test_c':0, 'test_d':0}
# f = open("bb.txt", 'w')
for _ in range(5000000):
    id = uuid.uuid4().hex
    mac = id[:4] + '.' + id[4:8] + '.' + id[8:12]
    id = id[8:]
    # onlineTime_num = random.randint(0, 19)
    onlineTime = random.randint(0, 19)
    updateTime = random.randint(onlineTime, 23)
    wifiUpDown = random.randint(500000, 99942000)
    offlineTime = updateTime
    dayTime = random.randint(1, 30)
    ss["_id"] = ObjectId(id)
    ss["mac"] = mac
    ss["onlineTime"] = datetime(2019,11,dayTime,onlineTime,00,29,0)
    ss["updateTime"] = datetime(2019,11,dayTime,updateTime,00,29,0)
    ss["offlineTime"] = datetime(2019,11,dayTime,offlineTime,00,29,0)
    #ss["onlineTime"] = "2019-11-" + dayTime + "T" + onlineTime + ":00:29Z"
    #ss["updateTime"] = "2019-11-" + dayTime + "T" + updateTime + ":00:29Z"
    #ss["offlineTime"] = "2019-11-" + dayTime + "T" + offlineTime + ":00:29Z"
    ss["wifiUpDown"] = bson.int64.Int64(wifiUpDown)
    json_user = ss


    # with open('client.txt','w') as f:
    # f.write(json_user)
    # json_user = json.loads(text_user)
    try:
      collection_onofflineUser.insert(json_user, check_keys=False)
    except:
        print('user_eee')
    # finally:
    #     print(json_user)



    # terminalInfo表
    ss_terminalinfo_os = random.choice(terminalinfo_os_list)
    text_terminalInfo = terminalinfo_id +mac+terminalinfo_os+ss_terminalinfo_os+ss_terminalinfo
    json_terminaInfo = json.loads(text_terminalInfo)
    try:
        collection_terminalInfo.insert(json_terminaInfo,check_keys=False)
    except:
        print('eee')
    finally:
        if ss_terminalinfo_os == 'Android':
            count_os['Andriod'] += 1
        elif ss_terminalinfo_os == 'IOS':
            count_os['IOS'] += 1
        elif ss_terminalinfo_os == 'Windows':
            count_os['Windows'] += 1
        # oui表
        ss_oui_organizationEn = random.choice(oui_organizationEn_list)
        # collection_oui .insert("%s%s%s%s%s%s%s\n" % (oui_id,mac[:7],oui_organizationEn,ss_oui_organizationEn,oui_organizationCh,ss_oui_organizationEn,ss_oui))
        text_oui = oui_id+mac[:7]+oui_organizationEn+ss_oui_organizationEn+oui_organizationCh+ss_oui_organizationEn+ss_oui
        json_oui = json.loads(text_oui)
    try:
        collection_oui.insert(json_oui,check_keys=False)
    except:
        print('eee')
    finally:
        if 'a' in ss_oui_organizationEn:
            count_organizationEn['test_a'] += 1
        elif 'b' in ss_oui_organizationEn:
            count_organizationEn['test_b'] += 1
        elif 'c' in ss_oui_organizationEn:
            count_organizationEn['test_c'] += 1
        elif 'd' in ss_oui_organizationEn:
            count_organizationEn['test_d'] += 1


print(count_os)
print(count_organizationEn)