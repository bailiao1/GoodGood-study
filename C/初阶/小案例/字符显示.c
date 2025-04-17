#include <stdio.h>

// 方法一:

int main()
{
    char arr1[] = "hello world!";
    char arr2[] = "############";

    int size = sizeof(arr1) / sizeof(arr1[0]) - 1;                // 不含 \0

    for (int i = 0; i <= size / 2; i++)                           // 两头齐进，只需要循环一半
    {
        arr2[i] = arr1[i];                                        
        arr2[size - 1 - i] = arr1[size - 1 - i];                 
        printf("%s\n", arr2);
    }
  
    return 0;
}



//-------------------------------------------------------------------------------------------------------------------------------

/*

方法二：

int main()
{
    char arr1[] = "hello world!";
    char arr2[] = "############";

    int size = sizeof(arr1) / sizeof(arr1[0]) - 1;  
    int left = 0;
    int right = size - 1;                                          // 最后一个字符的下标是 size - 1

    while (left <= right)
    {
        arr2[left] = arr1[left];
        arr2[right] = arr1[right];
        printf("%s\n", arr2);
        left++;
        right--;
    }

    return 0;
}

}

*/
