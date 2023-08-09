import os
import shutil

# Get parent directory to access data from
parent_dir = os.path.dirname(os.path.abspath(__file__))[:-8]

# Source and destination directories
source_dir = os.path.join(parent_dir, "data", "dataset", "train")
destination_dir_train = os.path.join(parent_dir, "data", "train")
destination_dir_test = os.path.join(parent_dir, "data", "test")

# Create the destination directoroes if they don't exist
if not os.path.exists(destination_dir_train):
    os.makedirs(destination_dir_train)

if not os.path.exists(destination_dir_test):
    os.makedirs(destination_dir_test)

# List all files in the source directory
file_list = os.listdir(source_dir)

def getType(filename):
    parts = filename.split("_")
    if parts[1] == 'mask.png':
        return [None, 'mask']
    else: return [parts[0], 'sat']

# Copy each file from source to destination, every tenth pair going to the test set
count = 0
for filename in file_list:
    source_path = os.path.join(source_dir, filename)
    [name, which] = getType(filename)
    if which == 'sat':
        matchfile = name + '_mask.png'
        source_path_match = os.path.join(source_dir, matchfile)
        if count%10 == 0:
            destination_path_sat = os.path.join(destination_dir_test, filename)
            destination_path_mask = os.path.join(destination_dir_test, matchfile)
        else:
            destination_path_sat = os.path.join(destination_dir_train, filename)
            destination_path_mask = os.path.join(destination_dir_train, matchfile)
        count += 1
    
        # Copy the file
        shutil.copy(source_path, destination_path_sat)
        shutil.copy(source_path_match, destination_path_mask)
        print(f"Copied {filename} and {matchfile}")

print("File copying completed.")