import random


class GameOverException(Exception):
    pass


class GameController:
    def __init__(self):
        self.__matrix = [[0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]]
        self.__new_count = 2  # 每次生成新元素的个数
        self.__get_zero_coordinates()  # 获取零元素的坐标，首次运行初始化
        for i in range(self.__new_count):
            self.__generate()  # 生成新元素，首次运行初始化
        self.__steps = 0  # 记录移动步数

    def game_over(self):
        """游戏结算"""
        score = 0
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix)):
                score += self.__matrix[i][j]
        return score

    def left(self):
        self.__move_zero()
        self.__combine_same()
        self.__step_progress()

    def right(self):
        self.__reverse()
        self.__move_zero()
        self.__combine_same()
        self.__reverse()
        self.__step_progress()

    def up(self):
        self.__transpose()
        self.__move_zero()
        self.__combine_same()
        self.__transpose()
        self.__step_progress()

    def down(self):
        self.__transpose()
        self.__reverse()
        self.__move_zero()
        self.__combine_same()
        self.__reverse()
        self.__transpose()
        self.__step_progress()

    def get_board(self):
        return self.__matrix

    def __get_zero_coordinates(self):
        # 获取零元素的坐标
        result_list = []
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                if self.__matrix[i][j] == 0:
                    result_list.append((i, j))
        self.__zero_coordinates = result_list

    def __generate(self):
        if len(self.__zero_coordinates) == 1:  # 只剩一个0时在此位置生成新的数，避免random.randint(0,0)报错
            self.__matrix[self.__zero_coordinates[0][0]][
                self.__zero_coordinates[0][1]] = random.randint(1, 2) * 2
            self.__get_zero_coordinates()
        else:
            random_number = random.randint(0, len(self.__zero_coordinates) - 1)  # 不止一个0随机选取位置生成新元素...
            self.__matrix[self.__zero_coordinates[random_number][0]][
                self.__zero_coordinates[random_number][1]] = random.randint(1, 2) * 2
            self.__get_zero_coordinates()

    def __transpose(self):
        # 矩阵转置
        self.__matrix = [[x for x in item] for item in zip(*self.__matrix)]

    def __reverse(self):
        # 矩阵横向翻转
        self.__matrix = [item[::-1] for item in self.__matrix]

    def __move_zero(self):
        # 向左移动零元素
        for line in range(4):
            for i in range(-1, -len(self.__matrix[line]) - 1, -1):
                if self.__matrix[line][i] == 0:
                    del self.__matrix[line][i]
                    self.__matrix[line].append(0)

    def __combine_same(self):
        # 向左合并相同元素
        for line in range(4):
            # 合并相同的相邻数据,仅做一次
            for i in range(3):
                if self.__matrix[line][i] == self.__matrix[line][i + 1]:
                    self.__matrix[line][i] *= 2
                    del self.__matrix[line][i + 1]
                    self.__matrix[line].append(0)

    def __step_progress(self):
        """
        每次向指定方向移动零、合并相同元素后的处理：
        1.更新零的坐标
        2.移动统计增加
        3.生成新的元素,每生成一次检测游戏是否结束
        """
        self.__get_zero_coordinates()
        self.__steps += 1
        for i in range(self.__new_count):
            self.__generate()
            if self.__check_game_over():
                raise GameOverException()

    def __check_game_over(self):
        if len(self.__zero_coordinates) == 0:
            return True
