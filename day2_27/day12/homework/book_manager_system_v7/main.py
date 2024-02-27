from usl import BookView

# 防止功能模块导入当前启动代码
if __name__ == '__main__':
    view = BookView()
    view.main()
    # 10:07 上课