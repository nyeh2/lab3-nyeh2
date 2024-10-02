#!/usr/bin/env python3

# Author ID: nyeh2

import subprocess

def free_space():
    space = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    space = space.communicate()
    space_strip = space[0].decode('utf-8').strip()
    return(space_strip)

if __name__ == '__main__':
    print(free_space())