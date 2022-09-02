import os
dir_path = os.getcwd()
curr_dir = os.path.basename(dir_path)
number = curr_dir[-1]
curr_dir.strip(number)
print(f"Hello {curr_dir} {number}")

