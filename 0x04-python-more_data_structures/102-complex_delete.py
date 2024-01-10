#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    # Create a new dictionary without the specified value
    new_dict = {key: val for key, val in a_dictionary.items() if val != value}

    # Create a sorted version of the new dictionary
    sorted_new_dict = dict(sorted(new_dict.items()))

    return sorted_new_dict


# Import the print_sorted_dictionary function
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary


# Updated print_sorted_dictionary function to exclude specific keys
def print_sorted_dictionary(a_dictionary):
    excluded_keys = {'lang', 'pref'}  # Add keys you want to exclude here
    for key in sorted(a_dictionary):
        if key not in excluded_keys:
            print("{}: {}".format(key, a_dictionary[key]))


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
