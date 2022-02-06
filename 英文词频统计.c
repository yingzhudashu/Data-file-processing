#include <stdio.h>
#include <string.h>
#include <wctype.h>

struct tongji{
	char danci[33];
	int shuzi;
}wa[999];

int main(){
	char a,str[999];
	int i=0,j=0,k,s;
	FILE *f1;
	f1=fopen("article.txt","r");
	a=fgetc(f1);
	while(a!=EOF){
		a=towlower(a);
		if(96<a&&a<123){
		   j=0;
		   do{	str[j++]=a;
		   		a=fgetc(f1);
		   		a=towlower(a);
		   }while(96<a&&a<123);
		   str[j]='\0';
		   if(i==0){
			strcpy(wa[i].danci,str);
			wa[i++].shuzi=1;
			continue;
			}
		}
		else {
			a=fgetc(f1);
			continue;
		}
		for(k=0;k<=i;k++){
			if(strcmp(wa[k].danci,str)==0){
				wa[k].shuzi++;
				break;
			}
		}
		if(k>i){
			strcat(wa[i].danci,str);
			wa[i++].shuzi=1;
			}
		a=fgetc(f1);
	}
	for(j=0;j<i-1;j++){
		for(k=0;k<i-j-1;++k){
			if(strcmp(wa[k].danci,wa[k+1].danci)>0){
				strcpy(str,wa[k].danci);
				strcpy(wa[k].danci,wa[k+1].danci);
				strcpy(wa[k+1].danci,str);
				s=wa[k].shuzi;
				wa[k].shuzi=wa[k+1].shuzi;
				wa[k+1].shuzi=s;
			}
		}
	}
	for(k=0;k<i-1;++k)
		printf("%s %d\n",wa[k].danci,wa[k].shuzi);
	printf("%s %d",wa[k].danci,wa[k].shuzi);
	fclose(f1);
}
