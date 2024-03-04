import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print("执行时间：{}秒".format(time.time() - start))
        return res

    return wrapper
 

@print_execute_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
# 16:03 上课
