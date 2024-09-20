"""
iven an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        # split them into a list, remove fullstop from last word, and put back reversed list
        s_list=s.split(" ")

        #remove empty spaces
        while "" in s_list:
            s_list.remove("")

        rWord_list = []
        for eachWord in reversed(s_list):
            rWord_list.append(eachWord)

        rWord = " ".join(rWord_list)

        return rWord