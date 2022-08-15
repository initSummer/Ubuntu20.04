#include"fillArray.h"
#include<random>
#include<time.h>
void fillArray(int a[], int size, int& numberUsed)
{
	srand(time(NULL));
	int i = 0;
	for(; i < size; i++)
		a[i] = rand()%10;
	numberUsed = i;
}
