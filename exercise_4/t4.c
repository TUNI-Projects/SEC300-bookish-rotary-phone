/**
 * Implement a program that creates temp file
How do you implement this as securely as possible?
*/

#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(void)
{
    char file_data[] = "Hello World";
    int length = strlen(file_data);

    FILE *tmp = tmpfile();

    if (tmp == NULL)
    {
        printf("Unable to create a temp file!\n");
        return -1;
    }

    fputs(file_data, tmp);
    rewind(tmp); // puts the file pointer at the beginning of the stream

    char get_file_data[length];
    fgets(get_file_data, sizeof length, tmp);

    printf("File Read: %s\n", get_file_data);

    char fname[FILENAME_MAX], link[FILENAME_MAX] = {0};

    printf(fname, "/proc/self/fd/%d", fileno(tmp));

    if (readlink(fname, link, sizeof link - 1) > 0)
        printf("File name: %s\n", link);

    return 0;
}
