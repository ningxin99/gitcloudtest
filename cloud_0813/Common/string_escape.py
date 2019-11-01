# coding:utf-8
def string_escape(string):
    strs = string.split('(')
    data = strs[0]
    for i in strs[1:]:
        data += "\(" + i
    string = data
    strs = string.split(')')
    data = strs[0]
    for i in strs[1:]:
        data += "\)" + i
    return data

