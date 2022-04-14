#include <stdio.h>
#include <stdlib.h>

int main()
{
    int days, workers, cakes, waffles, pancakes;
    scanf_s("%d %d %d %d %d", & days, &workers, &cakes, &waffles, &pancakes);

    int cake_sum = 45 * cakes;
    double waffles_sum = 5.80 * waffles;
    double pancakes_sum = 3.20 * pancakes;

    double total_sum_per_worker_per_day = workers * (cake_sum + waffles_sum + pancakes_sum);
    double final_sum = (days * total_sum_per_worker_per_day) * 0.875;

    printf("%.2f", final_sum);

    return 0;
}