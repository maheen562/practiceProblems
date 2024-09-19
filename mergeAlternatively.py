"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        #determine the length

        w1Len = len(word1)
        w2Len = len(word2)

        count = 0
        w1List = list(word1)
        w2List = list(word2)
       
       # join characters alternatively until same length

        new_word=""

        while count<w1Len and count<w2Len:
            new_word = new_word + w1List[count] + w2List[count]
            count = count + 1

        #add remaining characters

        rem_word = ""
        if w1Len>w2Len:
            rem_word = w1List[count:]
            # rem_word = " ".join(rem_word)
        elif w1Len<w2Len: 
            rem_word = w2List[count:]
            # rem_word = " " + " ".join(rem_word)

        for ch in rem_word:
            new_word = new_word+ch
        

        return new_word

        
