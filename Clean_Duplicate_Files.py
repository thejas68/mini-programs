"""This Python program checks all files in a folder and finds duplicates.
It does this by creating a unique “fingerprint” (called a hash) for each file.

If two files have the same fingerprint → they are duplicates
The program keeps one copy and deletes the extra ones

In short: It automatically cleans up repeated files and saves space."""

import os
import hashlib

def get_file_hash(filepath):
    """Generate a hash for a file"""
    hasher = hashlib.md5()
    with open(filepath, 'rb') as file:
        buffer = file.read()
        hasher.update(buffer)
    return hasher.hexdigest()

def remove_duplicates(folder_path):
    seen_files = {}
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_hash = get_file_hash(file_path)
            
            if file_hash in seen_files:
                print(f"Duplicate found: {filename} → Deleting...")
                os.remove(file_path)
            else:
                seen_files[file_hash] = filename

# Change this to your folder path
folder = "your_folder_path_here"

remove_duplicates(folder)
print("✅ Cleanup complete!")




