""" Docstring """
def main():
    """ Function Docstring """
    year = int(input("Year : "))

    if year % 4 != 0:
        print("Common Year")
    elif year % 100 != 0:
        print("Leap Year")
    elif year % 400 != 0:
        print("Common Year")
    else:
        print("Leap Year")

if __name__ == '__main__':
    main()
