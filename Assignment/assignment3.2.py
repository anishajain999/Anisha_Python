import os

path = r"/python_Assignment"
# print(file_path)
os.chdir(path)

def read_text_file(file_path):
    with open (file_path, 'r') as f:
        print(f.read())

