class Parent:
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(*list(map(lambda x : id(x),(Parent.x, Child1.x, Child2.x))),sep = '\n')
