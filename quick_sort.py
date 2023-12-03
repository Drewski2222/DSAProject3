def quick_sort(data, key):
    if len(data) <= 1:
        return data

    stack = [(0, len(data) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(data, low, high, key)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return data

def partition(data, low, high, key):
    pivot = data[low]['Data'][key]
    up = low + 1
    down = high

    while up <= down:
        while up <= down and data[up]['Data'][key] <= pivot:
            up += 1
        while data[down]['Data'][key] > pivot:
            down -= 1
        if up < down:
            data[up], data[down] = data[down], data[up]

    data[low], data[down] = data[down], data[low]

    return down
