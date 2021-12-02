#!/usr/bin/env python3
# @author      : Echo Echo (Shhhwip@gmail.com)
# @created     : 02/12/2021
# @filename    : day2.py
#
""" Navigate a submarine
"""

def instructions():
    depth = 0
    horizontal = 0
    with open('input', encoding='utf-8') as infile:
        for line in infile:
            if line[0] == 'f':
                horizontal = horizontal + int(line[-2])
            elif line[0] == 'd':
                depth = depth + int(line[-2])
            elif line[0] == 'u':
                depth = depth - int(line[-2])
        print(depth * horizontal)

def main():
    """Main Driver
    """
    instructions()

if __name__ == '__main__':
    main()

