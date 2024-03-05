file_str = "test.txt"
sub_str = "es"
if (index := file_str.find(sub_str)) != -1:
    print(f"find {sub_str} at {index}")
