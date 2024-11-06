"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise."""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currVal = 0

        for n in nums:
            if currVal<0:
                return False
            elif n>currVal:
                currVal = n
            currVal -=1

        return True
        