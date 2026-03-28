import os

base_path = "my_project/data/logs"

os.makedirs(base_path, exist_ok=True)
print("Directories created")

with open("my_project/file1.txt", "w") as f:
    f.write("Hello")

with open("my_project/file2.py", "w") as f:
    f.write("print('Hi')")

print("\nContents of my_project:")
for item in os.listdir("my_project"):
    print(item)

print("\nFinding .txt files:")
for root, dirs, files in os.walk("my_project"):
    for file in files:
        if file.endswith(".txt"):
            full_path = os.path.join(root, file)
            print(full_path)
