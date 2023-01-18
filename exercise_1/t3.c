#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Write a program that causes heap overflow
 */

int main(int argc, char *argv[])
{
    int size = atoi(argv[1]);
    // printf("%d\n", size);
    char *buffer = (char *)malloc(size);
    // printf("%s\n", argv[2]);
    strcpy(buffer, argv[2]);
    // printf("%s\n", buffer);
    return 0;
}