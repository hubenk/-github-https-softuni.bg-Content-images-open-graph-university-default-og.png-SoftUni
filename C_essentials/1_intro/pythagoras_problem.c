#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int a;
    int b;

    scanf_s("%d", &a);
    scanf_s("%d", &b);

    int area = a * a + b * b;

    int result = sqrt(area);

    printf("Hypotenuse is %d.", result);

    return 0;
}