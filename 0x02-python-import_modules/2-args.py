#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    args_str = "argument" if argc == 1 else "arguments"

    print("{} {}{}".format(argc, args_str, ":" if argc > 0 else "."))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, argv[i]))
