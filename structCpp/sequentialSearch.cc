#include<iostream>
#include"fillArray.h"
const int DECLARED_SIZE = 20;

int search(const int a[], int numberUsed, int target);

int main()
{
	int arr[DECLARED_SIZE], listSize, target;
	fillArray(arr, DECLARED_SIZE, listSize);

	char ans=0;
	int res;
	do{
		std::cout<<"Enter a number to search for:";
		std::cin>>target;
		res = search(arr, listSize, target);
		if(res == -1)
			std::cout<<target<<" is not on the list"<<std::endl;
		else 
			std::cout<<target<<" is stored in array position "
				<<res<<std::endl;
		std::cout<<"Search again?(y/n)";
		std::cin>>ans;
	}while(ans == 'y' || ans == 'Y');
	std::cout<<"End"<<std::endl;
	return 0;
}

int search(const int a[], int numberUsed, int target)
{
	for(int i = 0, found = 0; !found && (i < numberUsed); i++)
	{
		if(target == a[i])
			found = 1;
		if(found)
			return i;
	}
		return -1;
}
