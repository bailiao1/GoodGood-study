#include <stdio.h>

int main()
{
  int arr[9] = {8,5,1,3,9,4,2,6,7};                        // 设置例子数组

  int size = sizeof(arr) / sizeof(arr[1]);                 // 计算数组内有多少个数
  int i,j,temp;                                            // 初始化变量，temp作为数值交换位置的媒介

  for (i = 0; i < size-1; i++)                             // 设置外循环（size-1,避免索引越界. 遍历数组内所有索引）
    {
      for (j = 0; j < size-i-1; j++)                       // 设置内循环（开始对比排序，size-i 避免浪费）
        {
          if (arr[j] > arr[j+1])                          // 如果arr[j] > arr[j+1] ，将大数与小数换位，j++ .  下一轮内循环继续使用被移到[j+1]的大数  
          {                                               // 就算此轮arr[j] < arr[j+1],下一轮依旧使用新的最大值遍历对比。最终第一轮结束，当前数组最大值也会被移动到数组尾部
            temp = arr[j];                                // 外循环i++，内循环size - i - 1 使 j 的范围 -1 ，刚好不用去管已经处理完的最大值。接下来继续遍历对比，直到所有数从小到大排序完成
            arr[j] = arr[j+1];
            arr[j+1] = temp;
          }
        }
    }

  for (i = 0; i < size; i++)                                                   
    {
      printf("%d",arr[i]);                                // 123456789
    }
  printf("\n完成啦!\n");

  return 0;
}
