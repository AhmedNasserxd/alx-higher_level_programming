#!/usr/bin/python3
import sys


def print_statistics(total_size, status_codes):
    """
    Print statistics including total file size and counts of each status code.

    Args:
        total_size (int): Total file size accumulated so far.
        status_codes (dict): Dictionary containing counts of each status code.

    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))


def parse_line(line):
    """
    Parse a line from stdin into size and status code.

    Args:
        line (str): A line of input from stdin.

    Returns:
        tuple: A tuple containing the size (int) and status code (str).
    """
    parts = line.strip().split()
    return int(parts[-1]), parts[-2]


def main():
    """
    Main function to read stdin line by line and compute metrics.

    Returns:
        None
    """
    total_size = 0
    status_codes = {
        '200': 0, '301': 0, '400': 0, '401': 0,
        '403': 0, '404': 0, '405': 0, '500': 0
    }

    try:
        count = 0
        for line in sys.stdin:
            count += 1
            size, code = parse_line(line)
            total_size += size
            if code in status_codes:
                status_codes[code] += 1
            if count % 10 == 0:
                print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
