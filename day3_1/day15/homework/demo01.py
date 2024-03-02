"""
    复习-函数式编程
        1. 适用性: 多个函数主体结构相同,但是核心算法不同
        def 功能1():
            共性代码
            个性1代码

        def 功能2():
            共性代码
            个性2代码

        2. 步骤
            def 个性1代码():
                ...
            def 个性2代码():
                ...

        def 通用功能(个性代码):
            共性代码
            # 个性1代码()
            # 个性2代码()
            个性代码()

        通用功能(个性1代码)
        通用功能(个性2代码)
"""


