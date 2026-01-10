#5.3
def find_greater(x_list, x_num):
    result = []
    for item in x_list:
        if item > x_num:
            result.append(item)
    return result

print(find_greater([11, 35, 4, 67, 23], 20))
