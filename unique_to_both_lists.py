def unique_to_both_lists(list_1, list_2):
    list_1 
    list_2 

    set_1, set_2 = set(list_1), set(list_2)
    unique_elements = (set_1 - set_2) | (set_2 - set_1)

    return list(unique_elements)

