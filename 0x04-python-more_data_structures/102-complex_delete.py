#!/usr/bin/python3

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary


def complex_delete(a_dictionary, value):
    # Create a new dictionary without the specified value
    new_dict = {key: val for key, val in a_dictionary.items() if val != value}

    return new_dict


if __name__ == "__main__":
    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}

    # Test case 1
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")

    # Test case 2
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
