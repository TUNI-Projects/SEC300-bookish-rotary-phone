#include <stdlib.h>
#include <stdio.h>

/**
 * Code Reference
 * https://learn.microsoft.com/en-us/cpp/c-runtime-library/reference/rand-s?view=msvc-170
 * The rand_s function uses the operating system to generate cryptographically secure random numbers.
 * rand_s not available in swift, uses arc4random instead.
 * How to write in files in C: https://www.guru99.com/c-file-input-output.html
 */

int main()
{
    unsigned int number;
    FILE *file;
    file = fopen("t3_data.txt", "w");

    for (int i = 0; i < 15; i++)
    {
        number = arc4random();
        fprintf(file, "%u", number);
    }

    fclose(file);
    file = fopen("t3_data.txt", "r");

    int number_of_char = 0;
    for (char c = getc(file); c != EOF; c = getc(file))
    {
        // Increment count for this character
        number_of_char += 1;
    }
    printf("\nNumber of char: %d\n", number_of_char);
    return 0;
}