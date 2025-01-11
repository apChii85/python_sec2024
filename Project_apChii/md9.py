import os
import time

# Funkcija failu un direktoriju hierarhijas ģenerēšanai ar indentiem
def list(base_path, indent_level=0):
    try:
        entries = os.listdir(base_path)
    except PermissionError:
        print("Permission Denied:", base_path)
        return []
    
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

        # Izmantojam atkāpes atbilstoši līmenim
        indent = "          " * indent_level  # 10 atstarpes katram līmenim
        # Pārbaudām, vai tas ir direktorijs vai fails
        if os.path.isdir(full_path):
            dir_size = saizeris(full_path) / 1024  # gribu lai rāda kilobaitos
            result.append([f"{indent}Folderis", entry, f"{dir_size:.2f} KB", creation_time])
            result.extend(list(full_path, indent_level + 1))  # Rekursīvi pāriet uz apakšfolderiem
        else:
            file_size = os.path.getsize(full_path) / 1024  # Konvertējam uz kilobaitiem
            result.append([f"{indent}Fails", entry, f"{file_size:.2f} KB", creation_time])
    
    return result  # Atgriežam rezultātu pēc pilnīgas apstrādes

# Funkcija direktorija lieluma aprēķināšanai
def saizeris(directory):
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
    base_directory = input("Ievadiet apstrādājamo direktoriju: ").strip()
    print("\nIevadītā foldera saturs:")
    
    # Izgūstam failu un direktoriju hierarhiju un izvadām to
    saturs = list(base_directory)
    
    # rezultātu izvade ar indentiem
    for entry in saturs:
        print(f"{entry[0]:<25} {entry[1]:<80} {entry[2]:<25} {entry[3]:<35}")
