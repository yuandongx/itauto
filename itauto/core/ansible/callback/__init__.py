import os
import sys


def load_sys_path(target="core"):
    this_path = os.path.abspath(__file__)
    while True:
        ps = os.path.split(this_path)
        if ps[1] == target:
            break
        else:
            this_path = ps[0]
    if this_path not in sys.path:
        sys.path.append(this_path)
        
    print(sys.path)