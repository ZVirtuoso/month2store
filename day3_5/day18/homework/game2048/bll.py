class GameController:
    def __init__(self):
        self.__list_merge = None

        self.list_map = [
            [2, 64, 2, 2],
            [2, 2, 0, 0],
            [2, 0, 128, 0],
            [2, 8, 0, 4],
        ]

    def move_right(self):
        for item in self.list_map:
            self.__list_merge = item[::-1]
            self.__merge()
            item[::-1] = self.__list_merge

    def move_left(self):
        for item in self.list_map:
            self.__list_merge = item
            self.__merge()

    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def move_up(self):
        self.__transpose()
        self.move_left()
        self.__transpose()

    def move_down(self):
        self.__transpose()
        self.move_right()
        self.__transpose()

    def __transpose(self):
        self.list_map[:] = [list(item) for item in zip(*self.list_map)]
