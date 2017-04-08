""" Docstring """
def main():
    """ Function Docstring """
    numbers = []

    for _ in range(10):
        numbers.append(int(input()))

    numbers.sort()
    numbers.reverse()

    print("2 Max values are")
    for i in range(2):
        print(numbers[i])


if __name__ == '__main__':
    main()
