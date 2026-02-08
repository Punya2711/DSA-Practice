""" You are given an array arr[] of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
This array represents a permutation of the integers from 1 to n with one element missing. 
Your task is to identify and return the missing element."""

class Solution:
    def missingNum(self, arr):
        t_sum = 0
        a_sum = 0
        n = len(arr)+1
        t_sum = n*(n+1)//2
        a_sum = sum(arr)
        return t_sum - a_sum