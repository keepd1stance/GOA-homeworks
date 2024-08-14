def filter_num(lst):
    result = []
    for item in lst:
        if isinstance(item, int):
            result.append(item)
    return result

input_list = [1, 2.5, 3, 4.0, 5, 6.78]
filtered_list = filter(input_list)

print(filtered_list)
