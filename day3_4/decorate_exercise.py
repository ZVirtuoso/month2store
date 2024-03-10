import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"执行时间：{end_time - start_time}")
        return result

    return wrapper



def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value

sum_data = print_execute_time(sum_data)


sum_data(10)
sum_data(int(1e6))

