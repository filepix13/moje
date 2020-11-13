#include<stdio.h>

int fibo(int liczba);

int main(){

    int n;

    printf("How many numbers of fibounnaci sequence should we print?\nYour anwser: ");
    scanf("%d", &n);

    if(fibo(n) != -1){

        printf("The sequence: ");
        for(int i = 0; i < n; i++){
            printf("%d ", fibo(i));
        }
    } else{
        printf("Number should be intager that is >=0");
    }

    return 0;

}

int fibo(int liczba){

    long long wynik;
    
    if(liczba > 1){
        wynik = fibo(liczba-1)+fibo(liczba-2);
    } else if(liczba == 1){
        wynik = 1;
    } else if(liczba == 0){
        wynik = 0;
    } else{
        wynik = -1;
    }

    return wynik;
}