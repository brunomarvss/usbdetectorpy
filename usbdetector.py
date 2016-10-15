import string
from ctypes import windll
import time
import os

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return drives


if __name__ == '__main__':

    while True:
        before = set(get_drives())
        time.sleep(3)
        after = set(get_drives())
        drives = after - before
        drivelen = len(drives)

        if (drivelen):
            for drive in drives:
                if os.system("cd " + drive + ":") == 0:
                    newMount = drive
                    print "New drive detected: Newly mounted drive letter is %s" % (newMount)
