#!/usr/bin/python3
"""program that prints result of addition of all arguments"""


if __name__ == "__main__":
    import sys

    total = 0

    for x in range(len(sys.argv) - 1):
        total += int(sys.argv[x + 1])
    print("{}".format(total))
