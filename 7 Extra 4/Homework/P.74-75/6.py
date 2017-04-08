""" Docstring """
def main():
    """ Function Docstring """

    for num1 in range(1, 500):
        for num2 in range(1, 500):
            for num3 in range(1, 500):
                if num2 > num1 and num3 > num1:
                    continue
                if num1**2 == num2**2 + num3**2:
                    if num2 > num3:
                        pass
                    else:
                        print(num2, num3, num1)


if __name__ == '__main__':
    main()
