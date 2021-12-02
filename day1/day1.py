#!/usr/bin/env python3
# @author      : Echo Echo (Shhhwip@gmail.com)
# @created     : 02/12/2021
# @filename    : day1.py
#
""" Counts how many times the depth increases in a file
"""

def sliding_window():
    """Counts how many times the three measurement sliding window increases
    """
    counter = 0
    index = 0
    with open('input', encoding='utf-8') as infile:
        lines = infile.readlines()
        previous_window = int(lines[0]) + int(lines[1]) + int(lines[2])
        for i in range(1, len(lines) - 2):
            current_window = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
            if current_window > previous_window:
                counter = counter + 1
            previous_window = current_window
        print(counter)

def simple_increase():
    """Counts how many times each depth increases in a file
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

def main():
    """Main Driver"""
    simple_increase()
    sliding_window()

if __name__ == '__main__':
    main()
