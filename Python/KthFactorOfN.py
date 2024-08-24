"""
Problem: The Kth factor of N
Source: https://leetcode.com/problems/the-kth-factor-of-n/solutions/5671109/the-kth-factor-of-n/
Author: Osama Abdul Ghafoor
GitHub: https://github.com/Osama-Abdul-Ghafoor
"""

class Solution(object):
    def kthFactor(self, n, k):
        defList = []
        for value in range(1,n+1):
            if n % value == 0:
                defList.append(value)
        
            if(len(defList) == k):
                return defList[k-1]
        return -1
