
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       for n in nums1:
        if 0 in nums1:
            nums1.remove(0)

       nums1.extend(nums2)
       nums1.sort() 
        