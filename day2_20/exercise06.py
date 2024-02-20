"""
    题目6：编写程序，统计字符串中每个字符出现的次数，并将结果以字典的形式返回。
        message = "string"
    提示：遍历字符串每个字符
         如果字典中没有该字符，则添加，键为字符值为1
         如果字典中已经存在该字符，则将值累加1
"""
message = "string"
message = input("请输入信息")
list_message = list(message)
dict_message = {}
for i in list_message:
    if i not in dict_message:
        dict_message[i] = 1
    else:
        dict_message[i] += 1
print(dict_message)