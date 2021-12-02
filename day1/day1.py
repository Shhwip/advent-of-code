#!/usr/bin/env python3
# @author      : Echo Echo (Shhhwip@gmail.com)
# @created     : 02/12/2021
# @filename    : day1.py
#
""" Counts how many times the depth increases in a file
"""


def main():
    """Main Driver
    """
    counter = 0                                     # counts how many times the depth increases
    with open('input', encoding='utf-8') as infile: # opens the file
        previous_depth = int(infile.readline())     # sets the first depth to the first line of file
        for line in infile:                         # iterates through the rest of the lines
            current_depth = int(line)               # sets the current_depth to the current line
            if current_depth > previous_depth:      # if the current_depth is greater than the previous
                counter = counter + 1               # increment the counter
            previous_depth = current_depth          # set the previous_depth to the current_depth
    print(counter)                                  # after the loop, print the counter

if __name__ == '__main__':
    main()
