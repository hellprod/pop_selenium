def one_list_to_many_list(base_list):
    all_list = []
    list = []
    for i in base_list:
        if len(list) == 0 or list[-1] < i :
            list.append(i)
        else:
            all_list.append(list)
            list = []
            list.append(i)
    all_list.append(list)
    return all_list

