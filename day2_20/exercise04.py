"""
题目4：编写程序，按照要求输出字典中的数据
        dict_score = {'张三': 85, '李四': 92, '王五': 78, '赵六': 65}
    输出：
        学生姓名：张三，成绩：85，等级：良好
        学生姓名：李四，成绩：92，等级：优秀
        学生姓名：王五，成绩：78，等级：中等
        学生姓名：赵六，成绩：65，等级：及格
    等级：90以上为优秀
         80以上为良好
         70以上为中等
         60以上为及格
         60以下为不及格
"""


def get_grade(score):
    if score > 90: return "优秀"
    if score > 80: return "良好"
    if score > 70: return "中等"
    if score > 60: return "及格"
    return "不及格"

dict_score = {'张三': 85, '李四': 92, '王五': 78, '赵六': 65}

for key in dict_score:
    print("学生姓名：%s，成绩：%s，等级：%s"%(key, dict_score[key],get_grade(dict_score[key])))