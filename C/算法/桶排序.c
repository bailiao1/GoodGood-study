#include <stdio.h>
int main()
{
  int a[11],i,j,t;
  for (i = 0;i<=10;i++)        // 将桶初始化为0
    a[i] = 0

  for(i=1;i<=5;i++)          
  {
    scanf("&d",&t);            // 输入需要排序的5个数
    a[t]++;                    // 对应的桶+1
  }

  for (i=0;i<=10;i++)          // 依次判断a[0] ~ a[10]
    for (j=1;j<=a[i];j++)      // 出现几次就打印几次 
      printf("%d",i);
  
  return 0;
}
