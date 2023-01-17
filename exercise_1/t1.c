#include <stdio.h>
/**
 * Write a progam that causes unlimited buffer overflow
 */

int main(int argc, char *argv[])
{
    printf("Enter 5 character: ");
    char input[5];
    gets(input);
    char *bar = input;
    printf("Result: %s", bar);
    return 0;
}