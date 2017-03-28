import sys

N = 10
i = 0
j = 0

while i < N:
	j = 0
	k = 1
	while j < N-i:
		sys.stdout.write("-")
		j+=1
	while k <= i:
		l = k%10
		sys.stdout.write("%s" % l)
		k+=1
	while k > 0:
		l = k%10
		sys.stdout.write("%s" % l)
		k-=1
	i+=1
	print()

'''
#include<stdio.h>

int main()
{
	int n = 10;

	for(int i=1;i<=10;++i){

		for(int j=1;j<= n-i+1;++j ){
			printf("-");
		}
		for(int j=1;j<=i;++j){
			printf("%d",j%10);
		}
		for(int j=i-1;j>0;--j){
			printf("%d",j);
		}
		printf("\n");
	}

	return 0;
}
'''