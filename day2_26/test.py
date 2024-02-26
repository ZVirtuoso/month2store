class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return self.age != other.age

zwj = Person("张无忌",18)
zm = Person("赵敏",18)
print(zwj == zm)
print(zwj != zm)
