"""

"""


def verify_permissions(func):  # 接收旧功能               2
    def wrapper(*args):  # 包装新旧功能
        print("验证权限")  # 4
        res = func(*args)
        return res

    return wrapper


def insert(data):
    print("插入")


def delete():
    print("删除")
    return True


insert = verify_permissions(insert)  # 调用外函数           1
delete = verify_permissions(delete)
insert("新数据")  # 调用内函数                                      3
print(delete())
