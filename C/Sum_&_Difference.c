// Your task is to take two numbers of int data type, two numbers of float data type as input and output their sum:

// Declare  variables: two of type int and two of type float.
// Read  lines of input from stdin (according to the sequence given in the 'Input Format' section below) and initialize your  variables.
// Use the  and  operator to perform the following operations:
// Print the sum and difference of two int variable on a new line.
// Print the sum and difference of two float variable rounded to one decimal place on a new line.

// Sample Input

// 10 4
// 4.0 2.0
// Sample Output

// 14 6
// 6.0 2.0

//Solution: -

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a=10,b=4;
    float c=4.0,d=2.0;
        
    int sum1 = a+b;
    int min1 = a-b;
    float sum2 = c+d;
    float min2 = c-d;
    
    printf("%d %d\n",sum1, min1);
    printf("%.1f %.1f\n",sum2, min2);

    return 0;
}
