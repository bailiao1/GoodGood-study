// goroutine：Go 提供的一种轻量级并发执行单位，使用M:N 调度模型，允许程序并发执行 （并非 != 并行）
// 并发：逻辑上同时
// 并行：物理上同时（多核）
// M:N：（ M 个 goroutine，运行在 N 个操作系统线程上 ）调度器自动分配，不用管线程

// 和线程的区别：
// 传统线程：由操作系统管理，每个线程几 MB 栈空间，切换成本高
// goroutine：由 Go runtine 调度，栈动态增长，切换非常轻量


// 普通程序（单线程）
func main(){
  task1()
  task2()
}
// 执行顺序一定是 task1 -> 完成 -> task2 , 一次只做一件事


// 而 goroutine 的意思是，把task1放到 并行执行队列 中运行（主程序不会等它）
func main(){
  go fmt.Println("A")
  fmt.Println("B")
}
// 最终可能输出 A B ，也可能只输出 B（因为 main结束，程序退出，而 goroutine 还没来得及跑）
// goroutine 的本质不是传统线程，而是由 Go runtine 管理的协程，特点是：启动成本极低，栈空间初始很小（几 kb），可以开几十万
