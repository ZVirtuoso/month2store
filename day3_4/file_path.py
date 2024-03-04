from pathlib import Path

print((Path.cwd().parent / Path("day3_2/test.py")).exists())

print(Path("./day17/demo01.py").exists())
p1 = Path().cwd().joinpath("repeat.py")
print(p1.is_absolute())

p2 = Path("./decorate_exercise.py")
print(p2.is_absolute())
print(p2.stat().st_ctime)  # create
print(p2.stat().st_atime)  # access
print(p2.stat().st_mtime)  # modify
print(p2.stat().st_mtime_ns)  # nanoseconds

month02 = Path("../")
# for i in month02.iterdir():
#     print(i)

# for item in month02.glob("day2*1"):
#     print(item)

for item in month02.rglob("*.jpg"):
    print(f"{item}的大小是{item.stat().st_size / 1000000:.3f}Mb")
print({item.name: f"{item.stat().st_size / 1000000:.3f}Mb" for item in month02.rglob("*.jpg")})

print([item for item in month02.rglob("*demo*")])
