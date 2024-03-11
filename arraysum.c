//base code by HackerRank

#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



/*
 * Complete the 'simpleArraySum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY ar as parameter.
 */

int simpleArraySum(int ar_count, int* ar) {
    int arraySum=0;
    for (int i=0;i<ar_count;i++){
        arraySum +=*(ar + i);
        }

    return arraySum;

}
