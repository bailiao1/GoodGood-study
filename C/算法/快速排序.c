#include <stdio.h>

void temp(int* a, int* b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

int opp(int arr[],int left,int right)
{
  int pi = right;
  int i = left - 1;

  for (int j = left; j < right; j++)
    {
      if (arr[j] <= arr[pi])
      {
        i++;
        temp(&arr[j] , &arr[i]);
      }
    }
  temp(&arr[i+1],&arr[right]);
  return i+1;
}

void kuai(int arr[],int left,int right)
{  
  if (left < right)
  {
    int p = opp(arr,left,right); 
    kuai(arr, left, p-1);
    kuai(arr, p+1, right);
  }
}
