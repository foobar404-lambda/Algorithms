#!/usr/bin/python

import sys
import random

global_tracker = {}


def store(tracked_coins, count):
    global global_tracker

    keys = sorted(tracked_coins.keys())

    store_string = ""

    for key in keys:
        store_string += f"{key}:{tracked_coins[key]};"

    if count in global_tracker:
        global_tracker[count].append(store_string)
    else:
        global_tracker[count] = [store_string]


def find(tracked_coins, count):
    global global_tracker

    store_string = ""
    keys = sorted(tracked_coins.keys())

    for key in keys:
        store_string += f"{key}:{tracked_coins[key]};"

    if count in global_tracker:
        return store_string in global_tracker[count]
    else:
        return False


def recursive(amt, coins, count, results, t={}):

    global global_tracker

    if count == amt:
        results += 1
        return results

    if find(t, count):
        return results

    else:
        store(t, count)

    for coin in coins:
        if count + coin <= amt:
            clone = t.copy()

            if coin in clone:
                clone[coin] += 1
            else:
                clone[coin] = 1

            results = recursive(amt, coins, count + coin, results, clone)

    return results


def making_change(amt, coins, count=0, results=0):
    # remove large coins, then sort large to small
    coins = sorted(filter(lambda x: x <= amt, coins), reverse=True)

    return recursive(amt, coins, count, results)


print(making_change(20, [1, 5, 10, 25, 50]))
# print(global_tracker)


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations), amount=amount
            )
        )
    else:
        print("Usage: making_change.py [amount]")

