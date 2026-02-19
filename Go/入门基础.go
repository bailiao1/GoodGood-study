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
result, err := dicide(10,2)
