import os
import time
from tabulate import tabulate

def list_files_hierarchy(base_path, indent_level=0):
    try:
        entries = os.listdir(base_path)
    except PermissionError:
        return [["[Permission Denied]", base_path, "", "", ""]]
    result = []
    for entry in entries:
        full_path = os.path.join(base_path, entry)
        try:
            stats = os.stat(full_path)
            creation_time = time.ctime(stats.st_ctime)
            permissions = oct(stats.st_mode)[-3:]
        except PermissionError:
            creation_time = "[Permission Denied]"
            permissions = "---"
        if os.path.isdir(full_path):
            dir_size = get_directory_size(full_path)
            result.append(["Directory", entry, dir_size, creation_time, permissions])
            result.extend(list_files_hierarchy(full_path, indent_level + 4))
        else:
            file_size = os.path.getsize(full_path)
            result.append(["File", entry, file_size, creation_time, permissions])
    return result

def get_file_stats(file_path):
    try:
        stats = os.stat(file_path)
        return {
            "Size (bytes)": stats.st_size,
            "Creation Time": time.ctime(stats.st_ctime),
            "Last Modified": time.ctime(stats.st_mtime),
            "Permissions": oct(stats.st_mode)[-3:],
            "Path": os.path.abspath(file_path)
        }
    except (FileNotFoundError, PermissionError) as e:
        return {"Error": str(e)}

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except (FileNotFoundError, PermissionError):
                pass
    return total_size

if __name__ == "__main__":
    base_directory = input("Enter directory to traverse: ").strip()
    print("\nHierarchical File Listing:")
    hierarchy = list_files_hierarchy(base_directory)
    print(tabulate(hierarchy, headers=["Type", "Name", "Size (bytes)", "Creation Time", "Permissions"], tablefmt="grid"))

    while True:
        filename = input("\nEnter a filename for stats (or 'exit' to quit): ").strip()
        if filename.lower() == 'exit':
            break
        stats = get_file_stats(filename)
        print("\n" + "\n".join(f"{key}: {value}" for key, value in stats.items()))