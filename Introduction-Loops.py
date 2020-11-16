# Task
# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i squared.


n = int(input())
i = 1

while (i < n):
    squared = i**2
    print(squared)
    i = i + 1