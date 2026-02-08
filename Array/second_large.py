""" Given an array of positive integers arr[],
 return the second largest element from the array. 
 If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.
"""

class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
        sec_large = -1
        large = arr[0]
        for i in range(len(arr)):
            if arr[i] > large:
                large = arr[i]
        for i in range(len(arr)):
            if arr[i]<large and arr[i]>sec_large:
                sec_large = arr[i]
        return sec_large