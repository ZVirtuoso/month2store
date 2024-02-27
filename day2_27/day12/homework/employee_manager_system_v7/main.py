from usl import EmployeeView

# 快捷键 main+回车
if __name__ == '__main__':
    view = EmployeeView()
    view.main()
# 问题：如何保障程序只能在当前文件运行?
# 答：当变量__name__是"__main__"时,说明当前模块是主模块
