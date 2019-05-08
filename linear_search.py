def linear_search(search_for, search_in, matches):
    for i in range(len(search_in)):
        if search_for == search_in[i]:
            matches.append(search_for)
            search_list = search_in[i+1:]
            return matches, search_list
        elif search_for < search_in[i]:
            return matches, search_in[i:]
        else:
            pass


def intersection(a1, a2):
    """find all the elements in a1 that are also in a2

    Args:
        a1 (list): sorted list
        a2 (list): sorted list

    Returns:
        list: elements that appear in both a1 and a2
    """
    search_in = a2
    matches = []
    
    for search_for in a1:
        matches, search_in = linear_search(search_for, search_in, matches) 
    return matches


a1 = [1,2,3,4,5]
a2 = [2,4,6]
print(intersection(a1,a2))

