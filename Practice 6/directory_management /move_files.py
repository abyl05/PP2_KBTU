import shutil
import os

source_file = "my_project/file1.txt"
copy_path = "my_project/data/file1_copy.txt"
move_path = "my_project/data/logs/file1_moved.txt"

os.makedirs("my_project/data/logs", exist_ok=True)

shutil.copy(source_file, copy_path)
print("File copied")

shutil.move(copy_path, move_path)
print("File moved")

print("\nFinal files in logs folder:")
for file in os.listdir("my_project/data/logs"):
    print(file)
