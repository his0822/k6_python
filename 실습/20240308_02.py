import os
from pathlib import Path

file_path = Path('./aaa')
print(file_path)
dir_path = Path('./a.txt')
print(dir_path)

print(os.path.isdir(dir_path))
print(os.path.isdir(file_path))

for d in os.listdir():
    print(d)
    print(os.path.isdir(d))
    if '.txt' in d:
        print("FOUND!")
    
no_file = Path('./aaa/b.txt')
print(no_file.exists(dir_path)) 
print(file_path.exists(file_path)) 
