#include <stdio.h>

/**
 * Write a programme that causes off by one overflow
 */

int main(int argc, char *argv[])
{
    printf("Off-by-one buffer overflow | out of bounds overflow \n");
    int arr[1];
    arr[0] = 1;
    arr[1] = 2;
    return 0;
}
