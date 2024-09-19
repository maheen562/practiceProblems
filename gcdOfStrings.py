"""For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2."""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # We need to find greatest common divisor, find out what is comman b/w string 1 and 2
        # so we need to find the smallest possible divisor between b/w 1 and 2 and find out if it is added to both

        #start with factors of the smaller one

        #find smaller
        smallerStr = ""
        largerStr = ""
        if len(str1)<len(str2):
            smallerStr = str1
            largerStr = str2
        else:
            smallerStr = str2
            largerStr = str1

        #find multiples of smaller str
        lenMultiples=[]
        for i in range(1,len(smallerStr)+1):
            if len(smallerStr) % i == 0:
                lenMultiples.append(i)
        
        # print(lenMultiples)

        #see if any of the multiple length are divisible by both, starting from the largest
        #combine str so we don't need to divide by multiple individually

        lenMultiples.sort(reverse=True)
        combinedstr = str1 + str2
        for eachMultiple in lenMultiples:
            if len(largerStr) % eachMultiple == 0: #check if it is a multiple of the larger str
                #split them into equal chunks of the multiple
                split_strs = [combinedstr[i:i+eachMultiple] for i in range(0, len(combinedstr), eachMultiple)]
                #remove duplicates, if one pair remaining then we have a multiple, else we dont
                multiple = list(set(split_strs))
                if len(multiple) == 1:
                    return multiple[0]
        
        #if no multiple then return empty string
        return ""
        
