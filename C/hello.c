//This challenge requires you to print  on a single line, and then print the already provided input string to stdout. 
//If you are not familiar with C, you may want to read about the printf() command.

// Example : "s = life is beautiful"

// The required output is:
// Hello, World!  
// Life is beautiful  

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
	
    char s[100];
    printf("Hello, World!\n");
    scanf("%[^\n]%*c", &s);
    printf("%s\n", s);   

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    return 0;
}
