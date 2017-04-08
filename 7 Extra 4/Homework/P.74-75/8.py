""" Docstring """
def main():
    """ Function Docstring """
    hour1 = int(input("Hour 1 : "))
    min1 = int(input("Minute 1 : "))
    hour2 = int(input("Hour 2 : "))
    min2 = int(input("Minute 2 : "))

    hour_diff = abs(hour2-hour1)

    if min2-min1 > 0:
        hour_diff -= 1
        min2 += 60

    diff = hour_diff*60 + (min2-min1)

    result_hour = diff // 60
    result_min = diff % 60

    print(result_hour, "Hour(s)", result_min, "Minute(s)")


if __name__ == '__main__':
    main()
