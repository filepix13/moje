#include<stdio.h>

int main(){

    float x;
    float y;
    float cost;
    char choice;

    while(1){

        printf("\n1-Calculate cost of tiles\n");
        printf("0-End\n");

        printf("Your choice: ");
        scanf("%c", &choice);

        switch(choice){
            
            case '1':
                printf("Enter width of the floor (meters):");
                    if(scanf("%f", &x) == 1){
                        printf("Enter lenght of the floor (meters): ");
                        if(scanf("%f", &y) == 1){
                            printf("Enter cost of one squere meter of the tiles : ");
                            if(scanf("%f", &cost) == 1){
                                printf("%.2f$", x*y*cost);
                            }else{
                                printf("\nEntered character needs to be a number");
                            }
                        }else{
                            printf("\nEntered character needs to be a number");
                        }
                    } else{
                        printf("\nEntered character needs to be a number");
                    }
            break;
            case '0':
                return 0;
            break;
            default:
                printf("\nUndeclared option");
            break;

            }

        }
    return 0;
}