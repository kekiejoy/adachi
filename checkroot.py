import os

def check_root():
    if os.geteuid() != 0:
        print("This script must be run as root.")
        exit(1)
    else:
        return True