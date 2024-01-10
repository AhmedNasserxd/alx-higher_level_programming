#!/usr/bin/python3

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary


def update_dictionary(a_dictionary, key, value):
    # Update the value of the existing key or add a new key-value pair
    a_dictionary[key] = value

    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    # Test case 1
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)

    print("--")
    print("--")

    # Test case 2
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
