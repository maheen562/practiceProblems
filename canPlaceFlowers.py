"""
    You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        #go through the array to determine if a certain position is valid or not.
        position = 0


        if len(flowerbed) >1:

            while position<len(flowerbed) and n>0:
                #first check if it is not the last position, as we will only have to see behind
                #check if not first positiion as we'll only need to check ahead
                #check ahead and behind
            
                
                #change plantation to 1, decrement needed places, length is greater then 1
                if ((((position + 1) == len(flowerbed) and (flowerbed[position-1]!= 1)) or (position == 0 and (flowerbed[position+1]!= 1)) or     (flowerbed[position-1]!= 1 and flowerbed[position+1]!= 1)) and flowerbed[position]!=1):

                        flowerbed[position] = 1
                        n = n-1
                position = position+1
            if n>0:
                return False
            return True
        else:
            if (flowerbed[0] == 0 and n==1) or n==0:
                return True
            return False

        
            