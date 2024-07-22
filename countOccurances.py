"""Leetcode
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #determine array length        
        arr_length = len(nums)
        count = 0

        #sort array so we done have to keep track of each element
        nums.sort()
        curr = nums[0]
        
        #count an occurance for a repeated element else set the occurance to one
        #return if occurance exceeds arr_length/2
        for each_num in nums:
            if each_num == curr:
                count = count + 1
            else:
                curr = each_num
                count = 1

            if count > arr_length/2.0:
                return curr

            
#time complexity(O(n))- not counting sort function