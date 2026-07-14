from pathlib import Path
from config import *
from datetime import datetime


curent_time = datetime.now()
print(curent_time)

for x in down_path.iterdir():
    if x.suffix in photo:
        print(x)
        cr_date = datetime.fromtimestamp(x.stat().st_ctime)
        print(cr_date)
        print(" ")




new_dir = dir_path / "photos"
new_dir.mkdir(mode=0o777, parents=True, exist_ok=True)


