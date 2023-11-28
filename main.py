import covid
from merge_sort import merge_sort

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
        print("Dataset is empty or not loaded correctly.")
    '''

    # merge sort
    merge_sort(report, sort_key)

    # print first 10 items of sorted data
    for item in report[:10]:
        print(item)

if __name__ == "__main__":
    main()