#include <stdio.h>

/**
 * Write a programme that causes off by one overflow
 */

int main(int argc, char *argv[])
{
    printf("Off-by-one buffer overflow | out of bounds overflow \n");
    char arr[10];
    for (int i = 0; i < 12; i++)
    {
        arr[i] = 'A';
    }

    for (int i = 0; i < 12; i++)
    {
        printf("%d - > Result: %c - %x\n", i, arr[i], arr[i]);
    }
    return 0;
}
