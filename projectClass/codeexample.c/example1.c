#include<stdio.h>
#include <string.h> 
#include <stdlib.h> 

/////////////////////////////////////////////////////////////////////////////////////////////
// Test 1: For this task, you will receive a pointer to NULL terminated string: 
//		   The objective will be to fix any words incorrectly spelled words by replacing
//         every occurence of the letter 'y' with 's'.
//
// Expected Return Values:
//		- the task is successful: should return ERROR_SUCCESS (0).
//		- provided parameters are bad: should return ERROR_INVALID_PARAMETER (87)
//		- the letter 'y' is not part of 'sentence': should return ERROR_NOT_FOUND (1168)
/////////////////////////////////////////////////////////////////////////////////////////////
int changeLetterInString(char *sentence) //will receive a pointer to NULL terminated string:

{   
    
    char *result []; 
    char *oldW = "y";
    char *newW = "s"
  
    char *result = NULL; 
  
    // oldW string 
    char a_word [];  
    printf ("Enter a word: ");
    scanf ("%s", a_word);
    printf ("You entered: %s\n", a_word);
    
  
    int i, cnt = 0; 
    int newWlen = strlen(newW); 
    int oldWlen = strlen(oldW); 
  
    // Counting the number of times old word 
    // occur in the string 
    for (i = 0; sentence[i] != '\0'; i++) 
    { 
        if (strstr(&sentence[i], oldW) == &sentence[i]) 
        { 
            cnt++; 
  
            // Jumping to index after the old word. 
            i += oldWlen - 1; 
        } 
    } 
  
    // Making new string of enough length 
    result = (char *)malloc(i + cnt * (newWlen - oldWlen) + 1); 
  
    i = 0; 
    while (*sentence) 
    { 
        // compare the substring with the result 
        if (strstr(sentence, oldW) == sentence) 
        { 
            strcpy(&result[i], newW); 
            i += newWlen; 
            sentence += oldWlen; 
        } 
        else
            result[i++] = *sentence++; 
    } 
  
    result[i] = '\0'; 
    printf("New String: %sn", result); 
    free(result); 
    return result; 
} 
  
