#include <stdio.h>
/**
 * Write a programme that causes unlimited buffer overflow
 */

int main(int argc, char *argv[])
{
    printf("Enter 3 characters:");
    char input[3];
    gets(input);
    char *bar = input;
    printf("Result: %s", bar);
    return 0;
}