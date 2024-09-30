# Question:
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird.
# If n is even and in the inclusive range of 6 to 20, print Weird.
# If n is even and greater than 20, print Not Weird.


# Solution: - 

# import math
# import os
# import random
# import re
# import sys

# solution:-
if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:  # Odd number
        print("Weird")
elif n % 2 == 0 and 2 < n < 5:  # Even number between 2 and 5
        print("Not Weird")
elif n % 2 == 0 and 6 < n < 20:  # Even number between 6 and 20
        print("Weird")
elif n % 2 == 0 and n > 20:  # Even number greater than 20
        print("Not Weird")
