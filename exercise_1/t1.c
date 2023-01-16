#include <stdio.h>
void testBufferOverflow();

int main(int argc, char *argv[])
{
    testBufferOverflow();
    return 0;
}

void testBufferOverflow()
{
    int arr1[10];

    for (int i = 0; i < 10; i++)
    {
        arr1[i] = 2 * i;
    }

    for (int i = 0; i < 50; i++)
    {
        printf("%x\n", arr1[i]);
    }
}