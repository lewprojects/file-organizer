from pathlib import Path
from datetime import datetime

user_prompt = input("Paste in the path to the folder you want to organize: ")
my_dir = Path(user_prompt)

files = list(my_dir.iterdir())

for file in files:
    if file.is_file():
        
        #convert mtime to year
        file_mtime = file.stat().st_mtime
        file_dt = datetime.fromtimestamp(file_mtime)
        file_year = file_dt.year
        
        #create a destination
        file_ext = file.suffix
        new_dir = my_dir / str(file_year) / file_ext.removeprefix(".")
        new_dir.mkdir(parents=True, exist_ok=True)
        destination = new_dir / file.name

        #check if that destination is taken
        if destination.is_file():
            i = 1
            new_dest = destination
            while new_dest.is_file():
                new_file = f"{file.stem} ({i}){file_ext}"
                new_dest = new_dir / new_file
                i += 1
            file.rename(new_dest)
        else:        
            file.rename(destination)


