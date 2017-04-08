""" Docstring """
def main():
    """ Function Docstring """

    num1 = int(input("num1 : "))
    num2 = int(input("num2 : "))
    num3 = int(input("num3 : "))

    if num1 + num2 == num3:
        print("+")
    elif num1 - num2 == num3:
        print("-")
    elif num1 * num2 == num3:
        print("*")
    elif num1 / num2 == num3:
        print("/")


if __name__ == '__main__':
    main()
