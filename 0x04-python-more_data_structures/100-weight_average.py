#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sum_of_products = sum(score * weight for score, weight in my_list)
    sum_of_weights = sum(weight for _, weight in my_list)

    if sum_of_weights == 0:
        return 0

    return sum_of_products / sum_of_weights


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
