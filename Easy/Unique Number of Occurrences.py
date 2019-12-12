'''Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        countdict={}
        for i in set(arr):
            count=arr.count(i)
            if count not in countdict:
                countdict[count] = i
            else:
                return False
        return True
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        