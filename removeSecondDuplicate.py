"""Leetcode problem
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #sort array using the sort function
        nums.sort()

        #check if previous is same as current, set double to true
        #remove further occurences
        prev = nums [0]
        repeat = 1
        for each_element in nums[1:]:
            if repeat >= 2 and each_element == prev:
                nums.remove(each_element)
            elif each_element == prev:
                repeat = repeat + 1
            else:
                prev = each_element
                repeat = 1


# time complexity O(n)