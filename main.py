from pathlib import Path
from config import *
from datetime import datetime

# #get curent day
# curent_time = datetime.now()
# print(curent_time)
#
# #get all files into dir + detect whether it is photo or not (just testing for now)
# for x in down_path.iterdir():
#     if x.suffix in photo:
#         print(x)
#         cr_date = datetime.fromtimestamp(x.stat().st_ctime)
#         print(cr_date)
#         print(" ")
#
#
#
# #creating new dir named photos if it wasn`t created b4
# new_dir = dir_path.joinpath("photos")
# new_dir.mkdir(mode=0o777, parents=True, exist_ok=True)
# #----------------------------


def sorted_dirs():
    for name in sorting:
        if dir_path.joinpath(name).exists():
            pass
        else:
            new_dir = dir_path.joinpath(name)
            new_dir.mkdir()

def down_sort():
    for file in down_path.iterdir():
        if file.is_dir():
            continue
        moved = False
        for name, ext in data_sort.items():
            if file.suffix in ext:
                dest = dir_path.joinpath(name).joinpath(file.name)
                file.rename(dest)
                moved = True
                break
        if not moved:
            print(file)
            print("error")




def creator_back():
    for item in down_path.iterdir():
        if item.is_dir() and item.name in sorting:
            path = dir_path.joinpath(item.name)
            for files in path.iterdir():
                dest = down_path.joinpath(files.name)
                files.replace(dest)


down_sort()