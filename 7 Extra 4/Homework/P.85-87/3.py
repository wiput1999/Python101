""" Docstring """
import os

def main():
    """ Docstring """
    directory = os.getcwd() + "/res2/"
    for filename in os.listdir("res2"):
        old = os.path.join(directory, filename)
        new = os.path.join(directory, filename[-7:])
        os.rename(old, new)

if __name__ == '__main__':
    main()
