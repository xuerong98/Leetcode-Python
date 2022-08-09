#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 23:46:10 2022

@author: lcisxr
"""

#1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                
#Question: Why can't I use len(nums)-1
#range include left but not right