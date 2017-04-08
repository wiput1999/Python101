""" Docstring """
def main():
    """ Function Docstring """
    numbers = []

    for _ in range(10):
        numbers.append(int(input()))

    print("Max :", max(numbers))


if __name__ == '__main__':
    main()
