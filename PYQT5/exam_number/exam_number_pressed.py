num = int(input('请输入八位数字：'))

print('合法' if (sum((num // (10 ** i)) % 10 for i in range(8) if i % 2 == 0) + sum([(((num // (10 ** i)) % 10) * 2) % 10 + (((num // (10 ** i)) % 10) * 2) // 10 for i in range(8) if i % 2 != 0])) % 10 == 0 else '不合法')

print("合法" if sum(map((func01 := lambda x: x * 2 % 10 + x * 2 // 10) if b else (lambda y: y), (int(*str(num)[i]),)).__next__() for i, b in enumerate((True, False) * 4)) % 10 == 0 else "不合法")
print(func01(18))