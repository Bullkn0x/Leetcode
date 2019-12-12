import sys
import math

A= [3,2,4]
target =6
# BruteForce Method
# Time Complexity:  O(n**2)  Runtime :0.024-0.6s
# Space Complexity: O(1) no auxillary data structures to store data

def twosumBF(A,target):
    for x in range(len(A)-1):
        for y in range(x+1,len(A)):
            if (A[x]+A[y] == target):
                return A[x],A[y]
    return 'No Pair'
print(twosumBF(A,target))

# Dictionary Method
# Time Complexity:  O(n)  Runtime :0.018-0.3s
# Space Complexity: O(n) using hashtable to store values

def twosumHT(A,target):
    ht=dict()
    for i in range(len(A)):
        if A[i] in ht:
            return ht[A[i]], A[i]
        else:
            ht[target-A[i]] =  A[i]
    return 'No Pair'
print(twosumHT(A,target))

# Two iterator Method
# Time Complexity:  O(n)  Runtime :0.018-0.3s
# Space Complexity: O(1) no auxillary data structures to store

def twosumPointer(A,target):
    i=0
    j=len(A)-1
    while i<=j:
        if A[i]+ A[j] == target:
            return A[i],A[j]
        elif A[i]+A[j]< target:
            i+=1
        else:
            j-=1
    return 'No Pair'

print(twosumPointer(A,target))
