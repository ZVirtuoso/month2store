"""
    s = "ajldjlajfdljfddd",去重并升序输出”adfjl”
    可以利用集合的思想，没有值的字典
"""
s = "ajldjlajfdljfddd"
# hash_dict = set()
# for i,char in enumerate(s):
#     if char not in hash_dict:
#         hash_dict.add(char)

print(''.join(sorted(set(s))))

