/**
 * Implement a program that creates temp file
How do you implement this as securely as possible?

Reference: https://en.cppreference.com/w/c/io/tmpfile
and https://www.geeksforgeeks.org/tmpfile-function-c/
*/

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>   

int main(void)
{
    char file_data[] = "Hello World";
    int length = strlen(file_data);
    printf("word length: %d\n", length);
    printf("file data: %s\n", file_data);

    FILE *tmp = tmpfile();
    

    if (tmp == NULL)
    {
        printf("Unable to create a temp file!\n");
        return -1;
    }

    char fname[FILENAME_MAX], link[FILENAME_MAX] = {0};

    // printf(fname, "/proc/self/fd/%d", fileno(tmp));
    printf(">> %s\n", fname);
    printf(">> %c\n", fileno(tmp));


    fputs(file_data, tmp);
    rewind(tmp); // puts the file pointer at the beginning of the stream

    char get_file_data[20];
    fgets(get_file_data, sizeof length, tmp);

    printf("File Read: %s\n", get_file_data);

    if (readlink(fname, link, sizeof link - 1) > 0)
        printf("File name: %s\n", link);
    // abort();

    return 0;
}
