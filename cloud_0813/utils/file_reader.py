# coding:utf-8
"""
@author: Tracy
@mail: wanghongyu@ruijie.com.cn
@date: 2019.05.29
"""
import yaml
import os
import xlrd
from config import LOG_PATH


class YamlReader:
    def __init__(self, yamlf_path):
        if os.path.exists(yamlf_path):
            self.yamlf_path = yamlf_path
        else:
            raise IOError("文件不存在")
        self._data = None

    @property
    def data(self):
        # 如果第一次调用data,读取yaml文档，否则之际返回之前并保存的数据
        if not self._data:
            with open(self.yamlf_path, "rb") as f:
                self._data = list(yaml.safe_load_all(f))
                # load方法会将文件内容生成迭代器
                return self._data

    def get(self, element, index=0):
        return self.data[index].get(element)


class ExcelReader:
    """
    读取excel文件中的内容。返回list
    用于批量数据的读取

    如：excel的内容为：
    |A|B|C|
    |A1|B1|C1|
    |A2|B2|C2|

    print(ExcelReader(excel_path,title_line=True).data)
    输出结果：
    [{A: A1, B: B1, C:C1}, {A:A2, B:B2, C:C2}]

    print(ExcelReader(excel_path,title_line=False).data)
    [[A,B,C], [A1,B1,C1], [A2,B2,C2]]

    可以指定sheeet，通过index或者name

    ExcelReader(excel_path,sheet=2)
    ExcelReader(excel_path,sheet='test_1')

    """
    def __init__(self, excel_path, sheet=0, title_line=True):
        if os.path.exists(excel_path):
            self.excel_path = excel_path
        else:
            raise IOError(u"文件不存在")
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()


    @property
    def data(self):
        if not self._data:
            workbook = xlrd.open_workbook(self.excel_path)
            if type(self.sheet) not in [int, str]:
                raise IOError(u"sheet不存在")
            # 根据sheet索引或名称获取sheet内容
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                # 获取第一行内容
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))

            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))
        return self._data




# if __name__ == "__main__":
    # e = os.path.join(LOG_PATH, "test.xlsx")
    # reader = ExcelReader(e, title_line=False)
    # datas = reader.data
    # for d in datas:
    #      print (d)

    # y = os.path.join(LOG_PATH, "test.yaml")
    # reader = YamlReader(y)
    # da = reader.get(1, "url")
    # print (da)

















