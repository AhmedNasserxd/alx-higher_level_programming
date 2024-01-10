#!/usr/bin/python3

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

def multiply_by_2(a_dictionary):
    # Create a new dictionary with values multiplied by 2
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    
    return new_dict

# Example usage
if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    
    new_dict = multiply_by_2(a_dictionary)
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
