""" Docstring """
def main():
    """ Docstring """
    price = []
    result = 0

    for i in range(4):
        price.append(int(input("Price : ")))

    price.sort()
    price.reverse()

    for i in range(3):
        result += price[i]

    print("Total Cost :", result)

if __name__ == '__main__':
    main()
