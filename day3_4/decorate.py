# 现在需要在所有权限认证之前，先执行身份验证
def identity(*args):
    print(f"身份验证逻辑{args}")
    return True


def verify_identity(verify):
    def wrapper(*funcs):
        if identity():
            return verify(*funcs)

    return wrapper


def verify_permission(*funcs):
    def wrapper(*args):
        print("权限验证")
        for func in funcs:
            func(*args)

    return wrapper


verify_permission = verify_identity(verify_permission)


def verify_permission_super(*funcs):  # 权限认证之后选择性进行高级权限认证
    def wrapper(*args):
        verify_permission()()  # 只执行权限认证
        print("高级权限验证")
        for func in funcs:
            return func(*args)

    return wrapper


def verify_permission02(*funcs):
    def wrapper(*args):
        print("权限验证02")
        for func in funcs:
            return func(*args)

    return wrapper


@verify_permission
def insert(data):
    print(f"插入{data}")


@verify_permission
@verify_permission02
def delete(data01, data02):
    print(f"删除{data01},{data02}")


@verify_permission_super
def modify(data):
    print(f"修改{data}")


@verify_identity
def login():
    print("登录")


# login()
#
insert(500)
#
# delete(200, 300)
#
# modify(1001)
