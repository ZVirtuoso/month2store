"""

"""


def verify_permissions(func):  # 接收旧功能               2
    def wrapper():  # 包装新旧功能
        print("验证权限")  # 4
        func()

    return wrapper


def insert():
    print("插入")


def delete():
    print("删除")


insert = verify_permissions(insert)  # 调用外函数           1
delete = verify_permissions(delete)
insert()  # 调用内函数                                      3
delete()
