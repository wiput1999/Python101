''' main file '''


def main():
    ''' main function '''

    celsius = int(input('C: '))
    fahrenheit = (9 / 5) * celsius + 32
    print("F: " + str(fahrenheit))

if __name__ == '__main__':
    main()
