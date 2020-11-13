#include<stdio.h>

int main()
{
    int A;
    int B;
    int *ptrA;
    

    printf("Enter 1 digit: ");
    scanf("%d", &A);
    printf("Enter 2 digit: ");
    scanf("%d", &B);

    ptrA = &A;
    A = B;
    B = *ptrA;

    printf("A=%d ", A);
    printf("B=%d \n", B);
    return 0;

}