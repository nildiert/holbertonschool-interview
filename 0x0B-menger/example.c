#include <stdio.h>
#include <stdlib.h>

int m=0x55555555;
int x;
void main(){
	int n;
	scanf("%d",&n);
	n=1<<2*--n;
	for(x=n*n;x--;)
		printf(x&x/2&m?"":"%c%c",x&x/n&m?32:35,x&n-1?32:10);
}
