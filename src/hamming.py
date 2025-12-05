def hamming_distance(list1, list2):
    diffrences = 0
    if len(list1) != len(list2):
        return None
        
    for i in range(len(list1)):
        if list1[i] not in "GCAT":
            return None
        if list1[i] != list2[i]:
            diffrences += 1

    return diffrences

