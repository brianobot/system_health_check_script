from network import check_connectivity, check_localhost
import shutil
import psutil


def check_disk_usage(disk) -> bool:
    du = shutil.disk_usage(disk)
    free = (du.fre / du.total) * 100
    return free > 20


def cpu_usuage() -> bool:
    usuage = psutil.cpu_percent()
    return usage < 75


if __name__ == "__main__":
    if  not check_disk_usuage("/") or not cpu_usuage():
        print("ERROR!")
    elif check_localhost() and check_connectivity():
        print("Network Connection is OK!")  
    else:
        print("Something is Wrong!")
    
