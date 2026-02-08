""" You are given an array arr of positive integers. Your task is to find all the leaders in the array.
 An element is considered a leader if it is greater than or equal to all elements to its right. 
 The rightmost element is always a leader."""

class Solution:
    def leaders(self, arr):
        
        # just iterate once from right
        n = len(arr)
        leader = []
        
        # find max and append
        max = arr[n-1]
        leader.append(max)
        
        #iterate once:
        for i in range(n-2,-1,-1):
            if arr[i] >= max:
                max = arr[i]
                leader.append(max)
        
        # get back to correct order
        leader.reverse()
        return leader
        