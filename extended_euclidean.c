#include <stdio.h>
#include <stdlib.h>

int extended_euclidean(int n,int a);

int main(){
	int n,a;
	printf("Enter n and a\n");
	scanf("%d%d",&n,&a);
	printf("the inverse of %d in Z-%d is : ",a,n);
	int multiplicative_inverse = extended_euclidean(n,a);
	printf("%d\n",multiplicative_inverse);
	return 0;
}

int extended_euclidean(int n, int a){
	int r1 = n;
	int r2 = a;
	int t1 = 0;
	int t2 = 1;
	int r,t,q;

	while(r2 > 0){
		q = r1/r2;
		r = r1 - q * r2;
		r1 = r2;
		r2 = r;
		t = t1 - q * t2;
		t1 = t2;
		t2 = t;
	}
	
	while(t1 < 0){
		t1 = n - abs(t1);
	}

	return (t1 % n);
}