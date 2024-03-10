from PyQt5 import Qt


class Tree:
    # print_flag = True
    def __init__(self, father: 'Tree' = None, index: int = 0):
        self.lay = 0
        self.lay = father.lay + 1 if father else 0
        self.index = index
        self.branches = []  # type:list[Tree]
        self.iter = self.__iter__()
        self.father = father
        self.indent = 0
        self.indent = father.indent + len(father.get_index()) + 3 if father else 0

    def __iter__(self):
        return self.branches.__iter__()

    def get_index(self):
        return f'{self.father.get_index()}.{self.index}' if self.lay else '0'

    # def __str__(self):
    #     indexes = self.get_index()
    #     sons = f'[{('\n' + ' ' * (len(self.get_index()) + 3 )).join(map(str, self.branches))}]' if len(
    #         self.branches) else 'empty'
    #     return indexes + '->' + sons

    def get_str(self, reindent :int = 0):
        indexes = self.get_index()
        if reindent == 0:
            if len(self.branches):
                sons_str_list = []
                for son in self.branches:
                    sons_str_list.append(self.get_str(son,self.get_index()))
        else:
            if len(self.branches):
                sons_str_list = []
                for son in self.branches:
                    sons_str_list.append(self.get_str(son,reindent))
        sons = f'[{('\n' + ' ' * self.branches[0].indent).join(map(str, self.branches))}]' if len(
            self.branches) else 'empty'
        return indexes + '->' + sons
    def __str__(self):
        return self.get_str()


    # @staticmethod
    # def str_wrapper(func):
    #     def wrapper(self,first_time = True):
    #         if first_time:
    #             first_time = False
    #             tmp = self.indent
    #             self.indent = 0
    #             print('首次执行语句')
    #
    #             if len(self.branches):
    #                 sons_str = []
    #                 sons_str = wrapper(self.branches, False)
    #                 sons = f'[{''.join(sons_str)}]'
    #             else:
    #                 sons = 'empty'
    #             result = func(self) + sons
    #
    #             self.indent = tmp
    #             return result
    #         else:
    #             if len(self.branches):
    #                 sons_str = wrapper(self.branches, False)
    #                 sons = f'[{''.join(sons_str)}]'
    #             else:
    #                 sons = 'empty'
    #             result = func(self) + sons
    #
    #             return result
    #
    #     return wrapper
    #
    #
    # def __str__(self):
    #     sep = '\n' + ' ' * self.indent
    #     indexes = self.get_index()
    #     # sons = f'[{''.join(map(str, self.branches))}]' if len(self.branches) else 'empty'
    #     if self.index != 0:
    #         return sep + indexes + '->'
    #     else:
    #         return indexes + '->'
    # __str__ = str_wrapper(__str__)






    def append(self, num: int = 1):
        if num <= 0:
            return False
        else:
            for _ in range(num):
                self.branches.append(Tree(self, len(self.branches)))

    def appends(self, *nums: int):
        if 0 in nums:
            raise ValueError('nums must be positive integers')
        if nums:
            self.append(nums[0])
            if len(nums) > 1:
                sub_nums = nums[1:]
                for sub_tree in self.branches:
                    sub_tree.appends(*sub_nums)
        else:
            self.append(1)
        return self

    def __getitem__(self, item):
        return self.branches[item]


def get_subclass(cls: type, layer: int = 0):
    for subcls in cls.__subclasses__():
        print('\t' * layer, subcls)
        if len(subcls.__subclasses__()) > 0:
            layer += 1
            get_subclass(subcls, layer)


# if __name__ == '__main__':
#     get_subclass(Qt.QWidget)


if __name__ == '__main__':
    tree = Tree()
    tree.appends(2,1,2,3)
    # for item in tree:
    #     item.append(3)
    print(tree)
    # print(tree[1][0][1])
    # print(tree[2][1])