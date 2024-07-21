"""
LeetCode Problem
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if len(nums) > 1:
            previous = nums[0]
            for each_element in nums[1:]:
                if previous == each_element:
                    nums.remove(each_element)
                else:
                    previous = each_element
            k = len(nums)