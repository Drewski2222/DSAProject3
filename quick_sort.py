def quick_sort(data, key):
    if len(data) <= 1:
        return data
    
    pivot = data[len(data) // 2][key]
    
    left = []
    middle = []
    right = []

    for x in data:
        # if x[key] is less than pivot, append to left list
        if x[key] < pivot:
            left.append(x)
        # if x[key] is equal to pivot, append to middle list
        elif x[key] == pivot:
            middle.append(x)
        # if x[key] is greater than pivot, append to right list
        else:
            right.append(x)

    # recursively sort left and right lists and concatenate results
    return quick_sort(left, key) + middle + quick_sort(right, key)

