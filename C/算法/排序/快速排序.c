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


//-----------------------------------------------------------------------------------------------------------

// 当基础版快排遇到一些场景(如数组已排序)，由于pivot的固定，就会发生左边的数一直比右边小，流程一直被跳。
// 所有工作都交给了左递归，导致效率退化(变成链式递归，深度 O(n)，直接从快排退化为冒泡排序的效率 O(n²))。
// 所以我们可以引入pivot选择优化: “避免 pivot 选得太偏”，让左右两边划分得更平衡


// 三数取中法
void three_getone(int arr[], int left, int right)
{
    int mid = (left + right) / 2;                            // 选择中间的索引

    if (arr[left] > arr[mid])                                // 先一步保证 arr[left] < arr[mid] < arr[right]
        temp(&arr[left], &arr[mid]);
    if (arr[left] > arr[right])
        temp(&arr[left], &arr[right]);
    if (arr[mid] > arr[right])
        temp(&arr[mid], &arr[right]);

    // 最后把中间值（原来在 mid）换到 right，适配后续流程                        
    temp(&arr[mid], &arr[right]);                
}

// 直接在opp中，一步调整数组：
int opp(int arr[],int left,int right)
{                                                              
  three_getone(arr,left,right)                                                 // 只需要添加这一步，固定right就会被改成中间数owo
  int i = left - 1;                                                            // 剩下的过程，全都不需要改变
//......
}


