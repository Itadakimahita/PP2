import os

# Task 1
def list_contents(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

# Task 2
def check_access(path):
    print("Existence:", os.path.exists(path))
    print("Readability:", os.access(path, os.R_OK))
    print("Writability:", os.access(path, os.W_OK))
    print("Executability:", os.access(path, os.X_OK))

# Task 3
def test_path(path):
    if os.path.exists(path):
        print("Path exists.")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist.")

# Task 4
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))

# Task 5
def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + "\n")

# Task 6
def generate_files():
    for i in range(26):
        filename = chr(65 + i) + ".txt"
        with open(filename, 'w') as file:
            pass

# Task 7
def copy_file(source, d):
    with open(source, 'r') as src_file:
        with open(d, 'w') as dest_file:
            dest_file.write(src_file.read())

# Task 8
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)
        print("File deleted successfully.")
    else:
        print("File not found.")


#Exmaples for the tasks
path = "some/path/idk"
list_contents(path)
check_access(path)
test_path(path)
count_lines("example.txt")
write_list_to_file("output.txt", [1, 2, 3, 4, 5])
# generate_files()
copy_file("source.txt", "des.txt")
delete_file("file_to_delete.txt")
