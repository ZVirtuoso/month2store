"""
    可迭代对象工具集
"""


class IterableHelper:
    """
       对可迭代对象常用高阶函数的封装
    """

    @staticmethod  # 静态方法，可以省略self
    def find_all(iterable, condition):
        """
            在可迭代对象中查找满足条件的所有元素
        :param iterable: 可迭代对象
        :param condition: 函数类型,搜索条件
        :return: 生成器对象,推算满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def find_single(iterable, condition):  # 2
        """
            在可迭代对象中查找满足条件的第一个元素
        :param iterable: 可迭代对象
        :param condition: 函数类型,搜索条件
        :return: 满足条件的第一个元素
        """
        for item in iterable:
            if condition(item):  # 3
                return item

    @staticmethod
    def sum(iterable, condition):  # 2
        """
            根据条件对可迭代对象中的元素进行累加
        :param iterable: 可迭代对象
        :param condition: 函数类型,搜索条件
        :return: 数值类型,累加和
        """
        sum_value = 0
        for item in iterable:
            sum_value += condition(item)  # 3
        return sum_value

    @staticmethod
    def select(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def delete_single(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        for i, item in enumerate(iterable):
            if condition(item):
                del iterable[i]
                return True
        return False

    @staticmethod
    def get_max(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_value) < condition(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def get_min(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if condition(min_value) > condition(iterable[i]):
                min_value = iterable[i]
        return min_value

    @staticmethod
    def ascending_order(iterable, condition):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) > condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def descending_order(iterable, condition):
        """

        :param iterable:
        :param condition:
        :return:
        """
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if condition(iterable[r]) < condition(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]
