/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* productExceptSelf(int* nums, int numsSize, int* returnSize) {

    *returnSize = numsSize;

    int* rNums = malloc(numsSize*sizeof(int));

    int product = 1;
    int currIndex = 0;
    int currProduct = 1;

    //divide it into two halves, 
    //calculate product before and after the index

    //for before, we start from the first position which will be unknown, then we calculate the first using the prev, and go on
    //we add product, and add it to the next one

    //initalise all elements of the array to 1
    for(int i=0;i<numsSize;i++){
        rNums[i] = 1;
    }

    for(int i=0;i<numsSize-1;i++){
        //add product of i0 to currProduct
        currProduct = nums[i]*currProduct;
        //list this product to i+1
        rNums[i+1] = currProduct;

        currIndex++;

    }

    
    //now we go from the other way, calculating from the other end
    //currproduct should be equal the the product of the last position
    currProduct = 1;
    //we add the product from the other side to the existing product
    //e.g. pos 2 already has 1, now we need to add the product of 3    and 4 for the example [1,2,3,4]

    for(int i=numsSize-1;i>0;i--){
        //add product of i0 to currProduct
        currProduct = nums[i]*currProduct;
        //list this product to i+1
        rNums[i-1] = currProduct*rNums[i-1];

        currIndex++;

    }


    // for(int i=0;i<numsSize;i++){
    //      printf("num %d\n",rNums[i]);

    // }

    
    return rNums;
}