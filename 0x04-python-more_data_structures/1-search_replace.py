#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return []
    new_list = my_list.copy()
    for i in range(len(my_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list


"""
Alternatives method:
#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list == [] or my_list is None:
        return []
    new = [replace if item is search else item for item in my_list]
    return new
"""
