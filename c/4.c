#include<stdio.h>

int main(){

    int n;
    char choice;
    int i;

    while(1){

        scanf(" %c", &choice);

        switch(choice){
            case '1':
                printf("How many prime numbers should I find?\n");
                printf("Your anwser: ");
                scanf("%d", &n);

                while(i < n)
                {
                    


                }
            break;
            case '0':
                return 0;
            break;
            default:
                printf("Stupid");
            break;

        }

    }

}