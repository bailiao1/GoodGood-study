#include <stdio.h>

// 1. 宏常量（预处理器定义常量）
// #define 是预处理器指令，在编译之前进行简单的字符串替换
// 它不占用内存空间，不进行类型检查
#define MAX 100                 
#define STR "abcdef"            



// 2. 枚举常量（enum）
// 枚举是一种将相关的整数常量组合在一起的方式，具有一定的可读性
enum Color                     
{
    RED,       // 0
    GREEN,     // 1
    BLUE       // 2
};


// 3. const 常变量
// const 修饰的变量称为“常变量”，有内存空间，但值不可更改
// 与 #define 区别：const 有类型、参与类型检查，可以调试


// 全局变量
// 定义在函数外的变量，整个程序都可访问，生命周期为整个程序运行期间
int b = 0;      


// main 函数入口
int main()
{
    // 局部变量：只在 main 函数作用域中有效
    int a = 1;  // 普通变量，可以修改
    const int c = 0;  // const 常变量，不可修改

    // 枚举变量的使用
    enum Color d = RED;

    // 使用 #define 宏常量定义数组长度(数组大小必须是常量表达式，const定义的常变量本质还是变量)
    char arr[MAX] = "abc";  


    // 输出所有变量与常量的值
    printf("变量 a 的值（局部变量）：%d\n", a);
    printf("变量 b 的值（全局变量）：%d\n", b);
    printf("const 常变量 c 的值：%d\n", c);
    printf("枚举变量 d 的值（RED=0）：%d\n", d);
    printf("#define 宏常量 MAX 的值：%d\n", MAX);
    printf("#define 字符串 STR 的值：%s\n", STR);
    printf("字符数组 arr 的值（字符串）：%s\n", arr);

    return 0;
}
