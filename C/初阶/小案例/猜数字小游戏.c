#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void cai(void)
{
    srand(time(NULL));
    int a = rand() % 101;
    int b,d;
    int c = 0;
    
    printf("猜一个 0 到 100 的数字：");
    
    while(1)
    {   
        scanf("%d", &b);                // 获取用户输入
        if (b < 0 || b > 100)
        {
            printf("输入超出范围啦！只有 0 到 100 之间\n");
            continue;
        }
        c++;
        
        if (b > a)
        {
            printf("大了\n");

        }
        else if (b < a) 
        {
            printf("小了\n");

        }
        else
        {
            printf("对了\n只用了%d次就猜到了owo!\n",c);
            break;
        }
    }
}

int main()
{   
    int s = 1;
    do
    {
    cai();
    printf("扣1再来一把,扣0离开：\n");
    scanf("%d",&s);
    }while(s == 1);
    
    return 0;
}
