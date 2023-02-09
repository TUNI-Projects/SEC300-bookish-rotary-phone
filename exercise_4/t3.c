#include <sys/types.h>
#include <sys/time.h>
#include <sys/resource.h>

/**
 * This code is copied from OReilly library on how to disable memory dumps in the event of a crash
 * Reference code: https://www.oreilly.com/library/view/secure-programming-cookbook/0596003943/ch01s09.html
 *
 */

void main(void)
{
   struct rlimit rlim;

   rlim.rlim_cur = rlim.rlim_max = 0;
   setrlimit(RLIMIT_CORE, &rlim);
}