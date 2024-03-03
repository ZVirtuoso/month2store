from PyQt5.Qt import *
import sys

# 0.获取启动参数
args = sys.argv
# print(args)

# 1. 创建应用程序对象
app = QApplication(args)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件

# 2.3 展式控件
window.show()  # 刚创建好一个控件后（这个控件没有父控件），默认情况下是不显示的，需要显示，必须调用show()方法
# 3.应用程序执行，进入消息循环


# exec_()让整个程序开始执行，并且进入到消息循环（无限循环），直到结束并将结束码传递给系统
sys.exit(app.exec_())
