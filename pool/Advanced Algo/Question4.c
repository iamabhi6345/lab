/* (a) Write a program for NAIVE-STRING-MATCHER algorithm.
(b) Write a program for modified NAIVE-STRING-MATCHER algorithm with O(n)
complexity.*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int matchStringNaive(char *str1, char *str2);
int matchStringN(char *str1, char *str2);
int main(){
    printf("Enter the number of characters in the string in the first string\n");
    int num1 = 0 , num2 = 0; // Maximum length of the input string
    scanf("%d", &num1);
    char *str1 = (char *)malloc((num1 ) * sizeof(char));
    printf("Enter string 1: ");
   // fgets(str1, num1, stdin);
     scanf("%s", str1);
    printf("Enter the number of characters in the string in the second string\n");
  //  int num1 = 0 , num2 = 0; // Maximum length of the input string
     scanf("%d", &num2);
    
 // Allocate memory for the string
    char *str2 = (char *)malloc((num2 )* sizeof(char));
//fgets(str2, num2, stdin);  
    printf("Enter string 2: ");
    scanf("%s", str2);
    printf("----- Naive String matcher Result -------\n");
    int status  = matchStringNaive(str1, str2);
    if(status == 0){
        printf("Pattern not found\n");
    }
    printf("\n");
    printf("-----String Matcher in O(n) ------\n");
    status = matchStringN(str1, str2);
    if(status == 0){
        printf("Pattern not found\n");
    }
    free(str1);
    free(str2); 
}
int matchStringNaive(char *str1, char *str2){
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int i = 0, j =0;
    int flag = 0;
    int shift = 0;
    for(i = 0 ; i <=len1-len2 ;i++){
        for(j = 0 ; j < len2 ;j++){
            if(str1[i+j]!=str2[j])
            break;
        }
        if(j == len2){
            printf("Pattern is found at index %d\n", i);
            flag = 1;
        }
        shift++;
    }
    printf("The number of shifts are %d\n", shift);
    return flag;
    
}
int matchStringN(char *str1, char *str2) {
    int len1 = strlen(str1);
    int len2 = strlen(str2);
    int i = 0, j = 0;
    int flag = 0;
    int shifts = 0; // Initialize shift counter
    do {
        if (str1[i + j] == str2[j]) {
            for (j = 0; j < len2; j++) {
                if (str1[i + j] != str2[j]) {
                    break;
                }
            }
            if (j == len2) {
                printf("Pattern is found at index %d\n", i);
                flag = 1;
            }
            i = i + j;
        }
        else
            i++;
        shifts++; // Increment shift counter for each iteration of the outer loop
    } while (i <= len1 - len2);
    
    printf("Number of shifts: %d\n", shifts); // Print the number of shifts
    
    return flag;
}
