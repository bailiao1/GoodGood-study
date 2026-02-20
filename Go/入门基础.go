pack age main        // 每个 Go 文件必须属于一个包（package），程序入口是 main包的 main()函数

import "fmt"        // 导入库

func main() {
    fmt.Println("Hello World")
}

// bash 运行 go run main.go

// 变量声明
var name string = "Bai"      // 完整版var + 类型声明
age := "19"                  // 简短声明，自动判断类型

// 常量
const Pi = 1.14159

// 基本数据类型
整数：int,int8,int64
浮点：float32,float64
布尔：bool (true/false)
字符串：string


// if-else
if age >= 18 {
  fmt.Println("成年人")
} else {
  fmt.Println("未成年")
}

// for 循环 ( Go 只有 for )
for i := 0; i < 5; i++ {
    fmt.Println(i)
}

// switch
switch city {
case "Beijing":
  fmt.Println("北京")
case "shanghai":
  fmt.Println("上海")
default:
  fmt.Println("其他城市")
}


// 基本函数
func add(a int, b int) int {
  return a + b
}


// 多返回值（Go 特色）
import "errors"
func divide(a, b float64) (float64, error) {
    if b == 0 {
        return 0, errors.New("division by zero")
    }
    return a / b, nil
}
// 调用
result, err := divide(10, 2)
if err != nil {
	fmt.Println("错误:", err)
	return
}
fmt.Println("结果:", result)


// 数组（长度固定）
arr := [3]int{1,2,3}

// 切片（长度可变）
s := []int{1,2,3}
s = append(s,4,5)
fmt.Println(s)      // [1 2 3 4 5]
fmt.Println(s[1:3]) // [2 3] 依旧包头不包尾

// Map 字典
m := map[string]int{
    "apple":5.
    "banana:3,
}
m["cherry"] = 8
// 取值判断是否存在 val是取值，ok是bool类型，只判断这个值是否存在
val , ok := m["apple"]
if ok {
    fmt.Println(val)
}
delete(m,"banana")    //删除


// 结构体 （Struct）
typr Person struct {
    Name string
    Age int
}
// 方法
func (p Person) Greet() string {
    return fmt.Sprintf("我是 %s,今年 %d 岁", p.Name,p.Age)
}

func main() {
    bob := Person{Name:"Bob",Age:25}
    fmt.Println(bob.Greet())
}


// 指针
x := 10
p := &x           // p 是 x 的地址
*p = 20           // *解指针，通过指针修改x
fmt.Println(x)    // 20

// 
