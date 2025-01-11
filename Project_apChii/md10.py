import threading
import os
import time
from tabulate import tabulate

def list_files_hierarchy(base_path, result):
    try:
        entries = os.listdir(base_path)
    except PermissionError:
        result.append(["[Permission Denied]", base_path, "", "", ""])
        return
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
            list_files_hierarchy(full_path, result)
        else:
            file_size = os.path.getsize(full_path)
            result.append(["File", entry, file_size, creation_time, permissions])

def get_file_stats(file_path, result):
    try:
        stats = os.stat(file_path)
        result.append({
            "Size (bytes)": stats.st_size,
            "Creation Time": time.ctime(stats.st_ctime),
            "Last Modified": time.ctime(stats.st_mtime),
            "Permissions": oct(stats.st_mode)[-3:],
            "Path": os.path.abspath(file_path)
        })
    except (FileNotFoundError, PermissionError) as e:
        result.append({"Error": str(e)})

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
    file_to_analyze = input("Enter file path for stats: ").strip()

    # Results will be collected here
    hierarchy_result = []
    file_stats_result = []

    # Create threads
    t1 = threading.Thread(target=list_files_hierarchy, args=(base_directory, hierarchy_result))
    t2 = threading.Thread(target=get_file_stats, args=(file_to_analyze, file_stats_result))

    # Start threads
    t1.start()
    t2.start()

    # Wait for threads to finish
    t1.join()
    t2.join()

    # Display results
    print("\nHierarchical File Listing:")
    print(tabulate(hierarchy_result, headers=["Type", "Name", "Size (bytes)", "Creation Time", "Permissions"], tablefmt="grid"))

    print("\nFile Stats:")
    if file_stats_result:
        for key, value in file_stats_result[0].items():
            print(f"{key}: {value}")