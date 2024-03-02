"""
    2048 用户显示层
"""
from dll import *


class GameView:
    def __init__(self):
        self.controller = GameController()
        self.new_zero_co = []

    @staticmethod
    def __show_menu():
        print("4.左划", end=' ')
        print("6.右划", end=' ')
        print("8.上划", end=' ')
        print("2.下划", end=' ')
        print("0.结算")

    def __select_order(self):
        order = input("请输入您要执行的操作: ")
        if order == "0":
            if input("请再次输入0以结算游戏，否则游戏继续:") == "0":
                print(f"您主动结束了游戏，您的得分是{self.controller.game_over()}")
                return False
            else:
                print("您选择了游戏继续！")
                return True
        else:
            if order == "4":
                self.new_zero_co = self.controller.left()
            elif order == "6":
                self.new_zero_co = self.controller.right()
            elif order == "8":
                self.new_zero_co = self.controller.up()
            elif order == "2":
                self.new_zero_co = self.controller.down()
            else:
                print("请输入正确的操作！")
            return True

    # def __show_board(self):
    #     board_matrix = self.controller.get_board()
    #     for i in range(4):
    #         for j in range(4):
    #             if (i,j) in self.new_zero_co:
    #                 print(f"<{board_matrix[i][j]}>", end=' ')
    #             else:
    #                 print(board_matrix[i][j], end=' ')
    #         print()
    #     self.new_zero_co = []
    def __show_board(self):
        board_matrix = self.controller.get_board()
        s_matrix = [[str(x) for x in row] for row in board_matrix]
        for i in range(4):
            print("+------+------+------+------+")
            print("|",end ='')
            for j in range(4):
                if (i,j) in self.new_zero_co:
                    print(f"<{s_matrix[i][j]}>".center(6,' '), end='|')
                else:
                    print(s_matrix[i][j].center(6,' '), end='|')
            print()
        print("+------+------+------+------+")
        self.new_zero_co = []

    def main(self):
        try:
            while True:
                try:
                    print("当前分数为{0}".format(self.controller.game_over()))
                    self.__show_board()
                    self.__show_menu()
                    if not self.__select_order():
                        break
                except NotMovedException:
                    print("无效步骤！")

        except GameOverException:
            self.__show_board()
            print(f"游戏结束！你的得分是{self.controller.game_over()}")
