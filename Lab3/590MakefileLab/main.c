#include <stdio.h>
#include "fibonacci.h"

# trying_to_break_this (Commented out to be able to merge.)

int main(void) {
    int term = 10;
    printf("The %dth Fibonacci number is %d\n", term, fibonacci(term));
    printf("The theoretical Golden Ratio is %f\n", golden_ratio_approx(term));
    return 0;
}
