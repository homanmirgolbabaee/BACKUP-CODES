#include<string>
#include<stdio.h>
#include<bool>


void printZigZagConcat(char str[], int n)
{

    if (n == 1)
    {
        printf("%c",str);
        return;
    }

    int len = str.length();

    string arr[n];

    int row = 0;
    bool down;


    for (int i = 0; i < len; ++i)
    {

        arr[row].push_back(str[i]);
        if (row == n-1)
          down = false;
        else if (row == 0)
          down = true;
        (down)? (row++): (row--);
    }
    for (int i = 0; i < n; ++i){
        printf("%c",arr[i]);
}

int main()
{
    string str = "GEEKSFORGEEKS";
    int n = 3;
    printZigZagConcat(str, n);
    return 0;
}
