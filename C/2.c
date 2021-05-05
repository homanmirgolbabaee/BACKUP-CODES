#include<stdio.h>
int main(){

char sentence[100],c,k, h,sentence2[100],sentence3[100];
int i =0;
printf("Input:\n");
printf("Name:");
while (( c = getchar()) != '\n'){
    sentence[i++] = c;
    sentence[i] = '\0';
}
for(int i =0 ; i < 100 ; i++){
    printf("%c",sentence[i]);
}
printf("Adress:");
while (( k = getchar()) != '\n'){
    sentence2[i++] = k;
    sentence2[i] = '\0';
}
printf("\n");
for(int i =0 ; i < 100 ; i++){
    printf("%c",sentence2[i]);
}
printf("Age:");

while (( h = getchar()) != '\n'){
    sentence3[i++] = h;
    sentence3[i] = '\0';
}
for(int i =0 ; i < 100 ; i++){
    printf("%d",sentence3[i]);
}

}
