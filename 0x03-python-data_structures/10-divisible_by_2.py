#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list."""
    return [num % 2 == 0 for num in my_list]


if __name__ == "__main__":
    my_list = [0, 1, 2, 3, 4, 5, 6]
    list_result = divisible_by_2(my_list)

    i = 0
    while i < len(list_result):
        value = my_list[i]
        is_divisible = "is" if list_result[i] else "is not"
        print("{:d} {:s} divisible by 2".format(value, is_divisible))

        i += 1
