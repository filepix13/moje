#include<stdio.h>
#include<math.h>

int main()
{
    int number, t, rem;
    int sum = 0;
   
    printf("\nPlease enter a number to find whether it is an armstrong or not");
    scanf("%d",&number);

    t = number;
 
 
 
    while( t != 0 )
 
    {
    
        rem = t%10;
    
        sum = sum + rem*rem*rem;
    
        t = t/10;
    
    }
    
    if ( number == sum )
    
        printf("\nThe number %d is an armstrong number", number);
    
    else
    
        printf("\nThe number %d is not an armstrong number", number);
    

    return 0;

}