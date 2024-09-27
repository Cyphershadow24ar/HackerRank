# Task
Question: - 
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.
Example
a = 3
b = 5

Print the following:
1. a + b = 8
2. a-b = -2
3. a*c = 15

Solution: -

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
