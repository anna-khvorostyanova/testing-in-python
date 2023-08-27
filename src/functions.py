def find_max_min_value(a_list):
    max_value = a_list[0]
    min_value = a_list[0]
    # если используются сами значения, el (element), item, number
    for item in a_list:
        if item<min_value:
            min_value = item
        if item>max_value:
            max_value = item
    return max_value, min_value