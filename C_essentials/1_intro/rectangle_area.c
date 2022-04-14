#include <stdio.h>
#include <stdlib.h>

int main()
{
	int side_a = 0;
	int side_b = 0;

	scanf_s("%d", & side_a);
	scanf_s("%d", & side_b);

	int area = side_a * side_b;

	printf("Area %d.", area);

	return 0;
}
