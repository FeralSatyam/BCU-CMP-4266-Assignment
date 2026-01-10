#5.4
def sum(list_x, list_y):
    result = []
    for i in range(len(list_x)):
        result.append(list_x[i] + list_y[i])
    return result

print(sum([2, 4, 7], [1, 2, 3]))
