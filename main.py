import time
import covid
from merge_sort import merge_sort
from quick_sort import quick_sort

def main():
    # load COVID data
    report = covid.get_report()

    # available keys to sort by: cases, deaths, rate
    sort_key = 'Cases'

    # print first item in loaded report for debugging
    '''
    if report:
        print("First item in the dataset:", report[0])
    else:
        print("Dataset is empty or not loaded correctly")
    '''

    # start timer
    time1 = time.time()

    # merge sort
    merge_sort(report, sort_key)

    time2 = time.time()
    time3 = time2 - time1

    print(f"Merge sort completed in {time3} seconds")

    # print first 10 items of sorted data
    print("First 10 items in sorted result:")
    for item in report[:10]:
        print(item)

    sorted_report = quick_sort(report, sort_key)

    for item in sorted_report[:10]:
        print(item)

if __name__ == "__main__":
    main()