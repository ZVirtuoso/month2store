from usl import EmployeeView

# 当前模块是主模块(第一次运行)才执行下列逻辑
if __name__ == '__main__':
    view = EmployeeView() # Controller  []
    view.main()