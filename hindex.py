class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # we need to find the median

        #first we sort the list
        citations.sort(reverse=True)

    # Iterate through the sorted list and find the h-index
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h = i + 1
            else:
                break

        return h
        
