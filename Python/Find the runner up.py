# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.
# Constraints : -
# 2<n<10
# -100<A[i]<100

# solution:-

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
unique_scores = list(set(arr))
unique_scores.sort(reverse=True)

if len(unique_scores) > 1:
    runner_up_score = unique_scores[1]
    print(runner_up_score)
else:
    print("There is no runner-up score.")
