#!/usr/bin/python

import sys


def eating_cookies(n):

    if n <= 1:
        return 1

    one = 1
    two = 1
    three = 2

    for i in range(n - 2):
        temp = three
        three = one + two + three
        one = two
        two = temp

    return three


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies), n=num_cookies
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")

