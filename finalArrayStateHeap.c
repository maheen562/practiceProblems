/**
Leetcode question

**/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */


 #include <limits.h>

 int* getFinalState(int* nums, int numsSize, int k, int multiplier, int* returnSize) {
 
     int min = INT_MAX;
     int minIndex = 0;
     *returnSize = numsSize;
 
     for (int i=0;i<k;i++){
         for (int j=0;j<numsSize;j++){
             if(nums[j]<min){
                 min = nums[j];
                 minIndex = j;
             }
             // printf("%d",nums[j]);
         }
         nums[minIndex] = nums[minIndex]*multiplier;
         min = INT_MAX;
     }
 
     return nums;
 }