#include <stdio.h>
/**
 * Write a programme that causes unlimited buffer overflow
 */

void pao_pao()
{
    printf("Enter 3 characters: ");
    char input[3];
    gets(input);
    printf("Result: %s\n", input);
}

int main(int argc, char *argv[])
{
    printf("Print before pao_pao\n");
    pao_pao();
    printf("Print after pao pao\n");
    return 0;
}

/**
 * Safe to execute from [a - j]
 * Print before pao_pao
warning: this program uses gets(), which is unsafe.
Enter 3 characters: abcdefghijk
Result: abcdefghijk
[1]    31904 segmentation fault  ./test
*/