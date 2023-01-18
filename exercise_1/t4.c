#include <stdio.h>

/**
 * Write a program that causes function pointer overflow
 */
void (*hello)();

int main(int argc, char const *argv[])
{
    hello = argv[1];
    hello();
    return 0;
}

/**
 * I get segmentation fault here. not sure if it is the correct answer
 *  I am trying to access memory I am not supposed to access!?
 *  ➜  exercise_1 git:(master) ✗ ./t4 helloworld
    [1]    14899 segmentation fault  ./t4 helloworld
    ➜  exercise_1 git:(master) ✗ ./t4 potato
    [1]    14916 segmentation fault  ./t4 potato
    ➜  exercise_1 git:(master) ✗ make t4
    cc     t4.c   -o t4
    ➜  exercise_1 git:(master) ✗ ./t4
    [1]    14966 segmentation fault  ./t4
    ➜  exercise_1 git:(master) ✗ ./t4 he
    [1]    14983 segmentation fault  ./t4 he
 */