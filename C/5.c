#include <stdio.h>
#include <string.h>
int main()
{
   char s[100],s2[100];
   printf("Enter a string \n");
   gets(s);
   strrev(s);
   printf("Reverse of the string: %s\n", s);
   printf("Enter The Second String \n");
   gets(s2);
   printf("Reverse of the string: %s\n", s2);
   if(s2 == s){
    printf("yes");
   }
}
