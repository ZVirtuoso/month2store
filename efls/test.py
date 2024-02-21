list = [0,1,2,3,4]
# list[:2] = list[-4::-1]
# print(list)
list_mubiao = [2,1,3,4,0]
def switch(list_name, index01=0, index02=1):
    list_name[index01], list_name[index02] = list_name[index02], list_name[index01]

switch(list,0,2)
list.append(list.pop(2))
print(list)

list = list[1:]+list[:1]
print(list)

num = 100
list[1],num = num , list[1]
print(list);print(num)

print(('绿刀' == '紫刀') & False == False)

"""随机在语音列表中选择一句输出"""
import random
tuple = (1,2,3,4,5,6,7,8,9)
print(random.choice(tuple))