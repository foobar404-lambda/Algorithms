#!/usr/bin/python

import sys


rock = ["rock"]
paper = ["paper"]
scissors = ["scissors"]
available_options = ["rock", "paper", "scissors"]


def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [rock, paper, scissors]

    return rps_helper(n, rock) + rps_helper(n, paper) + rps_helper(n, scissors)


def rps_helper(n, list):
    if n == 1:
        return [list]

    rockList, paperList, scissorList = list[:], list[:], list[:]
    rockList += rock
    paperList += paper
    scissorList += scissors
    n -= 1
    return (
        rps_helper(n, rockList) + rps_helper(n, paperList) + rps_helper(n, scissorList)
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

