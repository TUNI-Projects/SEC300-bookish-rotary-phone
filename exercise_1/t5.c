#include <stdio.h>

/**
 * Write a program that contains printf vulnerability
 */

int main(int argc, char const *argv[])
{
    /* code */
    printf(argv[1]);
    return 0;
}

// example command: ./t5 "hello world %s%s%s% "