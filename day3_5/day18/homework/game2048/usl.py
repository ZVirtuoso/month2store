from bll import GameController


class GameView:
    def __init__(self):
        self.__controller = GameController()

    def __input_move_direction(self):
        dir = input("请输入移动方向wsad:")
        if dir == "w":
            self.__controller.move_up()
        elif dir == "s":
            self.__controller.move_down()
        elif dir == "a":
            self.__controller.move_left()
        elif dir == "d":
            self.__controller.move_right()

    def __display_map(self):
        for line in self.__controller.list_map:
            for item in line:
                print(item,end = "\t")
            print()

    def main(self):
        while True:
            self.__display_map()
            self.__input_move_direction()
