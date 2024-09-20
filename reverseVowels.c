/**
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
*/

#include<stdio.h>
#include<string.h>

int isVowel(char ch);

char* reverseVowels(char* s) {
    int sLen = strlen(s) - 1; //determine length of string, till 
    //last position
    int halflen = sLen/2 + 1;//determine halfpoint
    int i = 0,k=0,f1=0,f2=0,p1=0,p2=0; //two positions, two found variables, two indexes
    char v1=' ',v2=' ';

    //run a while loop, search string from start and end, once
    //two vowel found, 1 from start and end, swap them. 
    //run while loop till midpoint is reached

    while(i<(sLen-k)){

        //find vowel from start
        if (isVowel(s[i])){
            
            v1 = s[i];
            p1 = i;
            f1 = 1;
        }

        if (f1==1){

            //find vowel from end
            while(f2==0 && (sLen-k)>i){
                if (isVowel(s[sLen-k])){
                    v2 = s[sLen-k];
                    p2=sLen-k;
                    f2=1;
                }
                k++;
            }
            //switch vowels
            if(f1==1 && f2==1){
                s[p1] = v2; 
                s[p2] = v1; 
            }

            f1=0;f2=0;
        }
        
        i++;
    }
    return s;

}

int isVowel(char ch){
    if (ch== 'a' || ch== 'e'|| ch== 'i'|| ch== 'o'|| ch== 'u'|| ch== 'A'|| ch== 'E'|| ch== 'I'|| ch== 'O'|| ch== 'U'){
        return 1;
    }
    return 0;
}