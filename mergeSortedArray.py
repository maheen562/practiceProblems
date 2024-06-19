

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1.extend(nums2)
        nums1.sort()

        while len(nums1) > m + n:
            nums1.remove(0)