# 系统信息命令
whoami                 # 内核眼里，我现在是谁？（用户名/root）
id                     # uid（用户身份），gid（主组），groups（能用哪些附加权限）
uname -a               # 操作系统的内核是什么？（内核类型,主机名,内核版本,编译信息,架构，用户环境）
                       # 常见的几种内核抢占模型：PREEMPT_NONE（高延迟高吞吐），PREEMPT_VOLUNTARY（中延迟中吞吐），PREEMPT（低延迟低吞吐），PREEMPT_DYNAMIC（可切换）    

lsb_release -a         # 用的发行版是哪家? (发行方,人类可读名称,发行版本,代号) 。当某些最小系统/容器里 没有 lsb_release 时可以用：cat /etc/os-release

# 系统状态
df -h                  # 查看磁盘使用情况（人类可读）
du -sh folder/         # 查看目录大小
free -h                # 查看内存使用情况

top                    # 实时查看进程（类似任务管理器）
htop                   # top增强版（需要先安装）

kill 1234              # 给 PID=1234 的进程发信号，通常能关闭，但不是马上
kill -9 1234           # 强制杀死进程

ps -p 1                # 查看PID=1的进程，PID1通常是systemd或其他init系统，是所有用户进程的祖先进程。如果PID1出问题，系统基本完蛋
ps -o pid,ppid,cmd     # 查看当前进程是谁（PID），它爹是谁（PPID），它启动了什么命令（CMD）。每输入一串指令都是一段进程，bash存在也是一段进程
ps aux                 # 查看所有进程

ps aux | grep nginx    # 查看特定进程（会包含grep自己，不推荐）
ps -C nginx -f         # 使用 ps -C name（推荐）-f 查看完整信息

type cd                # 可查看指令是否为shell内建（builtin 不会 fork 新进程，必须在 bash 里执行）

# 网络
ip addr                # 或简写 ip a 查看所有接口IP地址

ping google.com                    # ping使用 ICMP协议 测试网络连通性，DNS，延迟等。无法测试目标服务是否可用，不能代表真实速度
curl https://api.ipify.org         # 查看公网ip，curl是主动请求资源并看返回结果的网络工具
wget https://example.com/file.zip  # 面向下载的工具，从 URL 下载资源，直接保存成文件，文件名默认取 URL 最后的部分

# 查看当前目录
pwd         # 默认可能保留逻辑路径        
pwd -P      # 显示物理路径

# 列出文件和目录
ls          # 简单列出
ls -l       # 详细列出（权限、大小、时间）
ls -la      # 包括隐藏文件（以.开头的文件）
ls -lh      # 人类可读的大小（KB, MB）
ls -lt      # 按修改时间排序
ls -ltr     # 按修改时间倒序
ls /home    # 列出指定目录

# 切换目录
cd /home/user      # "/" 绝对路径
cd Documents       # 相对路径
cd ..              # 上一级目录
cd ~               # 家目录
cd -               # 回到上一个目录

# 可组合
cd ../../etc       # 从user开始，返回两次上级，user -> home -> /(根目录) 再打开根目录下的etc目录

# 创建和删除
mkdir new_floder           # 创建空目录
mkdir -p new_floder/child  # 创建多级目录
touch file.txt             # 创建空文件

rm file.txt                # 删除指定文件（不包括目录）

rm -r new_floder           # 递归删除目录及内部的文件，子目录
rmdir new_floder           # 只删除空目录（非空会报错）

# 可以先删除目录内所有文件（/*）
rm new_floder/*      # 删除所有文件（不包括子目录与子目录中的文件，单个*只能向下一层）
rm -r new_floder/*   # 删除所有文件和子目录

# 复制与移动
cp file.txt file_backuo.txt     # 复制file并在当前目录创建一个file_backuo（如果已有，即覆盖）
cp file.txt floder1/            # 复制到floder1下
cp -r folder1 folder2           # 递归复制目录

mv file.txt floder1/            # 移动file到floder1下（可直接移动目录）
mv old_name.txt new_name.txt    # 重命名

# 查看文件
cat file.txt           # 显示整个文件
less file.txt          # 分页查看（可向前也能向后 1 <-> 2）
more file.txt          # 分页查看（只能前向查看 1 -> 2）

# less中常用的几个键
q     #退出
Space #下一页
b     # 上一页
↑ ↓   # 上下滚动
/     # 搜索
n / N # 下一个 / 上一个匹配
g     # 文件开头
G     # 文件结尾

hand -n 10 file.txt    # 查看开头10行
tail -n 10 file.txt    # 查看尾部10行

tail -f log.txt        # 小写f，它的作用是“跟踪”文件的变化，会先显示文件的最后10行，然后并不会退出，而是继续等待并显示之后被追加到文件中的新内容
tail -f -n 20 log.txt  # 会先显示日志文件最后20行
tail -s 1 -f log.txt   #  则表示每秒检查一次（-s 指定间隔秒数）

tail -F log.txt        # 大写F，跟踪文件名
                       # 当创建新的log.txt时，f会继续保持跟踪原文件，而F会重新打开新文件，转而跟踪新文件log.txt的内容

# 搜索文本
grep "xxx" file.txt    # 在file文件中，搜索包含"xxx"的行
grep -r "xxx" floed/   # 递归在某目录中搜索
grep -i                # 忽略大小写差异
grep -n                # 显示行号

# 排序
sort file.txt          # 默认按各行开头字母排序
sort -n                # 按数字排序
sort -h                # 按人类可读（内存大小）排序
sort -r                # 反向排序（倒序）
sort -u                # 先排序+按排序键去重（可能会丢掉“不同内容但 key 相同”的行）
sort file.txt | uniq   # uniq 去重相邻且相同的行

sort -k2               # 用第2个字段作为排序键（默认字段分隔符是 空格/tab）
sort -k2,2             # 只看第二列字段（从2开始，到2结束）
sort -t,               # 用"，"作为分隔符

# 计数
wc file.txt            # 统计行数，单词数，字节数
wc -l                  # 统计行数
wc -w                  # 统计单词数
wc -c                  # 统计字节数
wc -m                  # 统计字符数
