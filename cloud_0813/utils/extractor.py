# coding=utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.06.03
"""
import jmespath
import json
"""
抽取器，从响应结果中抽取部分数据,对于json格式的数据实现简单方式的抽取
"""



class JMESPathExtractor(object):
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.load(body))
        except Exception as e:
            raise ValueError("Invalid query:" + query + ":" + str(e))


if __name__ == '__main__':
    """
    假如json格式为：
    {"data":{
        "forecast":[
            {
                "123"
            }
            {
                "456"
            }
        ]
        "ganmao":"123456"
    }
        
    }
    JMESPathExtractor().extract(query="data.forecast[1]", body=res.text)
    
    """

    from utils.client import HTTPClient
    res = HTTPClient(url="http://123").send()
    j_1 = JMESPathExtractor().extract(query="data.forecast[1]", body=res.text)
    j_2 = JMESPathExtractor().extract(query="data.ganmao", body=res.text)
    print (j_1, j_2)