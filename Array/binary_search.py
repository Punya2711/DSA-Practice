"""Given a sorted array arr[] and an integer k, find the position(0-based indexing) 
at which k is present in the array using binary search. If k doesn't exist in arr[] return -1. 

Note: If multiple occurrences are there, please return the smallest index."""

class Solution:
    def binarysearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == k:
                ans = mid          # store answer
                high = mid - 1     # move left
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1

        return ans
