#include<stdio.h>

int main()
{
    int year;
    int a,c,e;
    float b,d,f;

    printf("Which year should i check? ");
    scanf("%d", &year);

    a = year/400;
    b = year/400.0;
    c = year/100;
    d = year/100.0;
    e = year/4;
    f = year/4.0;


    if((float)a == b)
        printf("This is a leap year");
    else if((float)c == d)
        printf("This is not a leap year");
    else if((float)e == f)
        printf("This is a leap year");
    else
        printf("This is not a leap year");

    return 0;  



}