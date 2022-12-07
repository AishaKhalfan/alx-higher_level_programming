#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    number_of_args = len(sys.argv)
    print("{:d} arguments:{:d} {}".format(number_of_args, sys.argv[1:], sys.argv))
