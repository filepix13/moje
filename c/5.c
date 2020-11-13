#include<stdio.h>
#include<stdlib.h>

int main()
{
    int size, i;
    char *arrey;
    char *check;
    char pali;
    int true;

    while(1)
    {

        printf("How many characters do you want to enter?: ");
        scanf("%d", &size);

        if(size > 0)
        {
            arrey = (char*) calloc(size, sizeof(char));     /* creating arrey to store sentence */
            check = (char*) calloc(size, sizeof(char));     /* creating arrey to store reversed sentence */
        
            printf("Enter word or sentence: ");

            for(i = 0; i < size; i++)                       /* scanning the sentence */
            {   
                scanf("%c", &pali);             
                arrey[i] = pali;
            }
            
            for(i = 0; i < size; i++)                       /* reversing the sentence */
            {   
                check[i] = arrey[size-1-i];
            }

            for(i = 0; i < size; i++)                       /* checking if it is a palindrome */
            {   
                if(check[i] != arrey[i])
                    true = 1;
            }

            if(true != 1)       
                printf("It is palindrome\n");
            else
                printf("It isn't palindrome\n");

            break;
        }
        else
            printf("You need to enter at least one character.\n");    
    
    }
    return 0;
    
}