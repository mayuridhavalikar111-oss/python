import os

# a. Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# b. List all files in a directory
print("\nFiles in the directory:")
files = os.listdir(cwd)
for file in files:
    print(file)

# c. Create a new directory
new_dir = "my_new_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print("\nDirectory created:", new_dir)
else:
    print("\nDirectory already exists:", new_dir)