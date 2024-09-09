#!/usr/bin/python3
""" FizzBuzz program """

import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    
    - For multiples of three print "Fizz" instead of the number.
    - For multiples of five print "Buzz" instead of the number.
    - For multiples of both three and five print "FizzBuzz".
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()  # Add a newline at the end


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        fizzbuzz(number)
    except ValueError:
        print("Please provide a valid integer.")
        sys.exit(1)
