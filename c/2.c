#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 18

int main(int argc, char *argv[])
{
    if (argc != 2) {
        printf("Usage: ./pi_to_n_digit DIGITS\n");
        return -1;
    }
    
    int N_real;
    int N = atoi(argv[1]);

    if (N < 1) {
        printf("Error. Enter at least 1 digits to calculate\n");
        return -1;
    } else if (N > MAX) {
        N_real = MAX;
    } else {
        N_real = N;
    }

    double digit = 0.0;
    int i;
    for (i = 0; i != N_real; ++i) {
        digit += ((pow(16, -i))) * (((4.0 / (8 * i + 1))) -((2.0 / (8 * i + 4))) - ((1.0 / (8 * i + 5))) - ((1.0 / (8 * i + 6))));
    }
    printf("Pi is: %.*f\n", N_real, digit);

    return 0;
}