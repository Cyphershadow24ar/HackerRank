# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  

# Function Description
# Complete the swap_case function in the editor below.

# swap_case has the following parameters:
# string s: the string to modify
# Returns
# string: the modified string

# Input Format
# A single line containing a string .

# Constraints
# 0<len(s)<=1000

# Sample Input 0
# HackerRank.com presents "Pythonist 2".
  
# Sample Output 0
# hACKERrANK.COM PRESENTS "pYT

# Solution:-

def swap_case(s):
    return s.swapcase() 
  # INbuild fucntion to Swap OR covert the lower case to upperCase & Vice Versa.

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
