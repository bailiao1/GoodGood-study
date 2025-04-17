#include <stdio.h>

int main()
{
    int arr[9] = {1,2,3,4,5,6,7,8,9};
    int size = sizeof(arr) / sizeof(arr[0]);

    int left = 0;
    int right = size - 1;
    int find = 0;
    int target = 0;
  
    printf("请输入要查找的目标：\n");
    scanf("%d",&target);

  
    while (left <= right)
    {
        int mid = left + (right - left)/2 ;             // 等价于 (left + right)/2 但防止栈溢出

        if (arr[mid] == target)
        {
            printf("找到啦，索引是%d\n", mid);
            find = 1;
            break;
        }
        else if (arr[mid] < target)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    if (!find)
    {
        printf("没找到o.o\n");
    }

    return 0;
}
