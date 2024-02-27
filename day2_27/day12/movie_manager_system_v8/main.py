"""
        电影信息管理系统V1-面向细节
        从终端录入数据，对电影(电影名、类型、演员、指数)进行增删改查
    电影信息管理系统V2-面向过程
        使用函数封装程序
    电影信息管理系统V3-封装数据
        创建Model类封装数据
    电影信息管理系统V4-面向对象
        使用MVC思想重构系统
            Model      模型:封装数据
            View       视图:处理界面逻辑,例如输入输出
            Controller 控制器:处理核心逻辑,例如存储计算
    电影信息管理系统V5-封装行为
        view除了main函数,隐藏其他成员
    电影信息管理系统V6-重写函数
        view直接打印Model,重写__str__
        controller直接remove删除,重写__eq__
    电影信息管理系统V7-拆分多个模块
    电影信息管理系统V8-异常处理
        view针对所有int(input())代码进行封装
        controller中remove如果报错则异常处理
"""
from usl import MovieView

if __name__ == '__main__':
    view = MovieView()
    view.main()
