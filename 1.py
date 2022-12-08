"""
Filename: 1.py
Author  : Jack Bates (jkb1473@rit.edu)
Created : 12/6/2022

https://adventofcode.com/2022/day/1
"""

infile = open("in1")
cur = []
cal_list = []
for line in infile.readlines():
    if line == "\n":
        if cur == []:
            print("Trying to save a cal list with no elf")
        else:
            cal_list.append(sum(cur))
            cur = []
    else:
        cur.append(int(line.strip()))
cal_list.append(sum(cur))

#Answer to question 1: 69528
print(max(cal_list))
#Answer to question 2: 206152
print(sum(sorted(cal_list)[-3:]))