from usl import EmployeeView

# 快捷键main+回车
if __name__ == '__main__':
    view = EmployeeView()
    view.main()  # main(view)
# 当变量__name__是"__main__"时，说明是在当前模块运行
# 否则是被导入到别的模块运行
