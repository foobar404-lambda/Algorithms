#!/usr/bin/python

import sys


def recursive(prefix, suffix, results,n):
    # if len(suffix) == 0:
    #     results.append(prefix)
    #     return results

    # for i in range(0, len(suffix)):
    #     newArr = suffix[:i] + suffix[i + 1 :]
    #     recursive(prefix + [suffix[i]], newArr, results)

    # return results

  for i in range(n+1):
    




def rock_paper_scissors(n):
    # rps = ["rock", "paper", "scissor"]
    # results = recursive([], rps, [],n)
    # print(results)


rock_paper_scissors(5)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")

