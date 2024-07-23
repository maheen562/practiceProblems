"""
LeetCode question
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # if k is greater then array length, do k%arr toreduce number of calculations
        arr_length = len(nums)
        if k>arr_length:
            k = k%arr_length

        #run a circular queue k number of times.
        while k:
            index = arr_length-1
            last_element = nums[arr_length-1]
            
            while index > 0:
                
                nums[index]=nums[index-1]
                index = index-1

            nums[0] = last_element
            k = k-1
            

            