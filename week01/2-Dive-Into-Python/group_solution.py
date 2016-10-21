def group(lst):
    res = []
    list_1 = []

    for i in range(len(lst)):
        if i == 0:
            list_1.append(lst[i])
        else:
            if lst[i] == lst[i-1]:
                list_1.append(lst[i])
            else:
                res.append(list_1)
                list_1 = [lst[i]]
    res.append(list_1)

    return res
