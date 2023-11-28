def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[len(data) // 2]
    
    left = []
    middle = []
    right = []

    for x in data:
        # if x is less than pivot, append to left list
        if x < pivot:
            left.append(x)
        # if x is equal to pivot, append to middle list
        elif x == pivot:
            middle.append(x)
        # if x is greater than pivot, append to right list
        else:
            right.append(x)

    # recursively sort left and right lists and conncatenate results
    return quick_sort(left) + middle + quick_sort(right) 


