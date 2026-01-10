#3.1
def create_list():
    my_list = ['PlayStation', 'Xbox', 'Steam', 'Ios', 'Google Play']
    return my_list
def get_info(my_list):
    return my_list[0], my_list[-2], len(my_list)
def get_partial(my_list):
    new_list = []
    new_list.append(my_list[1])
    new_list.append(my_list[2])
    new_list.append(my_list[3])
    return new_list
def get_last_three(my_list):
    rev_list = []
    rev_list.append(my_list[-1])
    rev_list.append(my_list[-2])
    rev_list.append(my_list[-3])
    return rev_list
def double_list(my_list):
    db_list = []
    db_list.append(my_list)
    db_list.append(my_list)
    return db_list
def amend(my_list):
    am_list = []
    am_list = my_list[:]
    am_list.append("Bye")
    am_list[1] = "None"
    return am_list
    
if __name__ == "__main__":
    test_list = create_list()
    print(test_list)
    print(get_info(test_list))
    print(get_partial(test_list))
    print(get_last_three(test_list))
    print(double_list(test_list))
    print(amend(test_list))

