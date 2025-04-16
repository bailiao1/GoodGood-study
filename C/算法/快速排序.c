#include <stdio.h>

void temp(int* a, int* b)                                                      // 封装一个换位函数哈（使用指针，使函数影响全局）
{
  int temp = *a;                                                               // 构建temp变量作为交换的临时容器
  *a = *b;
  *b = temp;                                                              
}


int opp(int arr[],int left,int right)                                          // 分割数组
{                                                              
  int i = left - 1;                                                            // 构建一个变量，用于记录交换位置

  for (int j = left; j < right; j++)                                           // 构建循环，遍历数组，每个数都要与定义的 中间数/分类点（默认使用最右/左的值）对比大小
    {
      if (arr[j] <= arr[right])                                                // 如果当前的值比最（右）的值小
      {
        i++;                                                                   // 触发条件，i+1
        temp(&arr[j] , &arr[i]);                                               // 当前值前移（小数前移，大数后迁，升序）
      }
    }
  temp(&arr[i+1],&arr[right]);                                                 // 对比结束，现在比arr[right]小的值都在数组前部分，每一次触发，i就会后移一位，现在的位置也到了最后一个比arr[right]小的索引，我们将中间数插入，大值移到末尾
  return i+1;                                                                  // 分类完成，将中间数（arr[right]）的索引返回主函数（a~b < 中间数 < c~d）
}


void kuai(int arr[],int left,int right)                                        // 快速排序主函数
{  
  if (left < right)                                                            // 递归结束条件（直到数组被分的不可再分，也就是只剩一个数时（arr[0] == arr[0]））
  {
    int p = opp(arr,left,right);                                               // 找到pivot
    kuai(arr, left, p-1);                                                      // 递归使用pi分类左数组（left(0) ,  p-1）                // 将数组不断细分，不断使用新的中间数，插入正确的位置，不再参与排序，递归深处的数组范围只会越来越小（-=1）   
    kuai(arr, p+1, right);                                                     // 递归使用pi分类右数组（p+1 ， right(size - 1)）        // 分类点（pivot）也会越来越靠近边界（left/right），直到重合。                                                                                                                                    
  }                                                                                                                                   // 最终每个数都成为一次分类点，找到了正确的位置，数组的位置也就排序完成了
}


int main()
{
  int arr[9] = {8,5,1,3,9,4,2,6,7};                       
  int size = sizeof(arr) / sizeof(arr[0]);                 // 计算数组内有多少个数

  kuai(arr,0,size-1);
  
  for (int i = 0; i < size; i++)                                                   
    {
      printf("%d ",arr[i]);                                // 1 2 3 4 5 6 7 8 9 
    }
  printf("\n完成啦!\n");

  return 0;
}
