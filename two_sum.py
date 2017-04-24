#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#https://leetcode.com/problems/two-sum/#/description
class Solution(object):
    def twoSum( selfnums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            m=0
            for i in nums:
                m=m+1
                n=0
                for j in nums:
                    n=n+1
                    if m!=n:
                        if i+j==target:
                            ind=[m-1,n-1]
                            return ind
