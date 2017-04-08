""" Docstring """
def main():
    """ Function Docstring """
    day = int(input("Day : "))
    month = int(input("Month : "))
    year = int(input("Year : "))

    month_count = [31, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Exclude February

    if year % 4 != 0:
        month_count.insert(1, 28)
    elif year % 100 != 0:
        month_count.insert(1, 29)
    elif year % 400 != 0:
        month_count.insert(1, 28)
    else:
        month_count.insert(1, 29)

    result = 0
    for i in range(month-1):
        result += month_count[i]
    result += day

    print(result)

if __name__ == '__main__':
    main()
