#include<stdio.h>
#include <time.h>
#include <stdlib.h>

//void printLab(char lab[][]);
void printLab(char [][5]);

int main(){

    char lab[5][5];
    int test;
    int numb = 0;
    char u;
    int r;
    int i;
    int j;
    int x = 0;
    int y = 0;


    srand(time(NULL)); 

    //Initialize labirinth
    for(i = 0; i < 5; i++){
        for(j = 0; j < 5; j++){
            
            r = rand() % 2; 
            
            if(numb > 7){
                r = 0;
            }

            if(r == 1){
                u = '#';
                numb ++;
            } else{
                u = ' ';
            }
            
            lab[j][i] = u;  
        }
        
    }

    lab[x][y] = 'o';  
    printLab(lab);

    while(!(x == 4 && y ==4)){
        
        printf("\n\nWhere to go now?");
        scanf("%d", &test);
        printf("%d", test);
        
        switch(test){
            case 8: 
            if(y > 0 && lab[x][y-1] == ' '){
                    y -= 1;
                }
            break;
            case 6:
            if(x < 5 && lab[x+1][y] == ' '){
                    x += 1;
                }
            break;
            case 4:
            if(x > 0 && lab[x-1][y] == ' '){
                    x -= 1;
                } 
            break;
            case 2:
            if(y < 5 && lab[x][y+1] == ' '){
                    y += 1;
                } 
            break;
            default:

            break;
        }

        lab[x][y] = 'o';
        printLab(lab);
    }

}   


//void printLab(char lab[][]){
void printLab(char lab[][5]){
    int i;
    int j;

    for(i = 0; i < 5; i++){
        printf("-----------");
        printf("\n");
        printf("|");

        for(j = 0; j < 5; j++){
            printf("%c|", lab[j][i]);
        }
        printf("\n");
    }
    printf("-----------");

}





