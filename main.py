import time
import covid
from merge_sort import merge_sort
from quick_sort import quick_sort

def main():
    sort_key = ''

    # load COVID data
    report = covid.get_report()

    # available keys to sort by: Cases, Deaths, Rate
    print("Key to sort data by? (1 = cases, 2 = deaths, 3 = rate)")
    choice = input()

    if choice == '1':
        sort_key = 'Cases'
    elif choice == '2':
        sort_key = 'Deaths'
    elif choice == '3':
        sort_key = 'Rate'

    # print first item in loaded report for debugging
    '''
    if report:
        print("First item in the dataset:", report[0])
    else:
        print("Dataset is empty or not loaded correctly")
    '''

    print("Sorting algorithm? (1 = merge, 2 = quick)")
    sort_method = input()

    if sort_method == '1':
        # merge sort
        # start timer
        time1 = time.time()
        merge_sort(report, sort_key)
    elif sort_method == '2':
        # quick sort
        # start timer
        time1 = time.time()
        quick_sort(report, sort_key)

    time2 = time.time()
    time3 = time2 - time1

    if sort_method == '1':
        print(f"Merge sort completed in {time3} seconds")
    elif sort_method == '2':
        print(f"Quick sort completed in {time3} seconds")

    # print first 10 items of sorted data
    print("First 10 items in sorted result:")
    for item in report[:10]:
        print(item)

if __name__ == "__main__":
    main()