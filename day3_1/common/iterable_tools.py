class IterableHelper:

    @staticmethod
    def find_single(iterable, condition):
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def find_all(iterable, condition):
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def sum(object_iterable,chose_member):
        """
        :param object_iterable:对象容器
        :param chose_member:返回对象成员的函数
        """
        sum = 0
        for item in object_iterable:
            sum += chose_member(item)
        return sum