#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 10:45:25 2022

@author: lcisxr
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        a = [-1,-1]
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                a = [mid, mid]
                break
        print(mid)
        # while a != [-1,-1]:

        #     for i in range(mid, len(nums)):
        #         if nums[i] == target:
        #             i = i+1
        #             print(i)
        #         else:
        #             a[1] = i
        #             break
        #     a[1] = i
            
        #     for j in range(mid, -1, -1):
        #         if nums[j] == target:
        #             j = j-1
        #             print(j)
        #         else:
        #             a[0] = j
        #             break
        #     return a
        # return a
        i = mid
        j = mid
        while i <= len(nums) -1 and nums[i] == target:
            a[1] = i
            i += 1
            
        while j >= 0 and nums[j] == target:
            a[0] = j
            j -= 1
        return a


        

nums = [5,7,7,8,8,10]
target = 7
an = Solution()
sol = an.searchRange(nums, target)
print(sol)

