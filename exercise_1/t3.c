#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Write a programme that causes heap overflow
 */

int main(int argc, char *argv[])
{
    int size = atoi(argv[1]);
    char *buffer = (char *)malloc(size);
    strcpy(buffer, argv[2]);
    return 0;
}