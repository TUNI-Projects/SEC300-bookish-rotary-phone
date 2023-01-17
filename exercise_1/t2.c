#include <stdio.h>

/**
 * Write a program that causes off by one overflow
 */

int main(int argc, char *argv[])
{
    printf("Off-by-one buffer overflow | out of bounds overflow \n");
    int arr[5];
    for (int i = 0; i <= 5; i++)
    {
        arr[i] = 2 * i;
    }

    for (int i = 0; i <= 5; i++)
    {
        printf("%x - %d\n", arr[i], arr[i]);
    }
    return 0;
}
