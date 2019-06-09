/*	This program will generate an array of integers
	filled with ordered numbers between 1 & 150,
	search that array 100 times using an ordered list
	sequential search for random numbers in the same
	range, and print statistics about those searches.
	   Written by:
	   Date:
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define MAX_ARRAY 100
#define NUMBER_LIMIT 150
#define SEARCHES 100

//	Prototype Declarations
void fillAryOrerd  (int array[]);
bool binarySearch();

int main (void){
    
    int array [MAX_ARRAY];
    srand (time (NULL));
	fillAryOrerd (array);
	for (int i = 1;  i <= SEARCHES;  i++)
	{
        binarySearch();
    }
    return 0;
}// main


/*	=================== binarySearch ============
	This function will ask for an array of integers then ask for the ascending order or the array then ask the user 
    what integer to find in the array then print out the position of that integer.
	   Pre  :  array is an empty array of integers
	   Post :  array filled with number series */


bool binarySearch(int i, int n, int x, int flag, int first, int last, int mid)   // DO NOT ASK WHY IT WORKS ...IT JUST KNOW IT WORKS 
{
//	Local Definitions
	int arry [MAX_ARRAY];
   
//	Statements
	srand (time (NULL));
	fillAryOrerd (arry);
	for (i = 1;  i <= SEARCHES;  i++)
	{
            printf("***********************************\n");
            printf("Enter size of array:");
            scanf("%d",&n);
            printf("\nEnter array elements(*****ASCENDING ORDER******* and enter)\n");
        
            for(i=0;i<n;++i)
                scanf("%d",&arry[i]);
        
            printf("\nEnter the element to search:");
            scanf("%d",&x);
        
            first=0;
            last=n-1;
        
            while(first<=last)
            {
                mid=(first+last)/2;
        
                if(x==arry[mid]){
                    flag=1;
                    break;
                }
                else
                    if(x>arry[mid])
                        first=mid+1;
                    else
                        last=mid-1;
            }
        
            if(flag==1)
                printf("\nElement found at position %d\n",mid+1);
            else
                printf("\nElement not found. Try Again \n");
        
    }
    return main;
	        

}// binarySearch

/*	=================== fillAryOrerd ============
	This function will fill an array of integers with
	numbers by first adding 2, then adding 1, then
	adding 2 again, and so on.
	   Pre  :  array is an empty array of integers
	   Post :  array filled with number series
*/
void fillAryOrerd (int array [ ])
{
//	Local Definitions 
	int i    =  0;
	int num  =  1;

//	Statements
	while (i < MAX_ARRAY)
	   {
	    array[i]  =  num;
	    i++;
	    num      +=  2;
	    array[i]  =  num;
	    i++;
	    num++;
	   } // while 
	return;
}	// fillAryOrerd




