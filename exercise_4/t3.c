#include <sys/types.h>
#include <sys/time.h>
#include <sys/resource.h>


/**
 * This code is copied from OReilly library on how to disable memory dumps in the event of a crash
 * Reference code: https://ww.oreilly.com/library/view/secure-programming-cookbook/0596003943/ch01s09.html
 *
 */

void main(void)
{
   struct rlimit rlim;
   printf("RLIMIT CURRENT: %d\n", rlim.rlim_cur);
   printf("RLIMIT Max: %d\n", rlim.rlim_max);
   // abort();

   rlim.rlim_cur = rlim.rlim_max = 0;
   setrlimit(RLIMIT_CORE, &rlim);
   printf("RLIMIT CURRENT: %d\n", rlim.rlim_cur);
   printf("RLIMIT Max: %d\n", rlim.rlim_max);
   abort();
}