#!/usr/bin/python3
"""
Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:

Total file size: File size: <total size>
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
format: <status code>: <number>
status codes should be printed in ascending order
"""


def print_stats(size, status_codes):
    """
    Print statistics including total file size and counts of each status code.

    Args:
        total_size (int): Total file size accumulated so far.
        status_codes (dict): Dictionary containing counts of each status code.

    Returns:
        None
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
