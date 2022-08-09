#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 13:12:57 2022

@author: lcisxr
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        n = list(str(x))
        if n == n[::-1]:
            return True
        else:
            return False

#Note: true and false are logic, cannot use string