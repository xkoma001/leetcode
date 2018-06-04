# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        rels = {}
        for pos in range(len(nums)):
            if nums[pos] in rels:
                return [rels[nums[pos]], pos]
            else:
                rels[target-nums[pos]] = pos

        return []

