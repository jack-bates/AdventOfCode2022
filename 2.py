"""
Filename: 2.py
Author  : Jack Bates (jkb1473@rit.edu)
Created : 12/6/2022
https://adventofcode.com/2022/day/2
"""

infile = open("in2")
game_list = infile.readlines()

r = "ROCK"
p = "PAPER"
s = "SCISSORS"
d = {
    "A":r,
    "B":p,
    "C":s,
    "X":r,
    "Y":p,
    "Z":s
}
scoring = {
    r:1,
    p:2,
    s:3
}

class Move:
    def __init__(self,c):
        self.move = d[c]

    def __eq__(self, other):
        return self.move == other.move

    def __gt__(self, other):
        if self.move == r and other.move == s:
            return True
        elif self.move == p and other.move == r:
            return True
        elif self.move == s and other.move == p:
            return True
        else:
            return False

    def __str__(self):
        return self.move

score = 0

for gameline in game_list[:15]:
    gameline = gameline.strip().split()
    m1 = Move(gameline[0])
    m2 = Move(gameline[1])
    rscore = scoring[m2.move]
    if m2==m1:
        rscore += 3
    elif m2>m1:
        rscore += 6
    score += rscore

#Answer to problem 1:
print(score)
