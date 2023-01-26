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

    printf("%s\n", buffer);
    strcpy(buffer, argv[3]);
    printf("%s\n", buffer);

    return 0;
}