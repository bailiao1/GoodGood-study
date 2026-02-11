# 查看当前目录
pwd

# 列出文件和目录
ls          # 简单列出
ls -l       # 详细列出（权限、大小、时间）
ls -la      # 包括隐藏文件（以.开头的文件）
ls -lh      # 人类可读的大小（KB, MB）
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
rm new_floder/*      # 删除所有文件（不包括子目录）
rm -r new_floder/*   # 删除所有文件和子目录


# 查看文件
cat file.txt           # 显示整个文件
less file.txt          # 分页查看（可向前也能向后 1 <-> 2）
more file.txt          # 分页查看（只能前向查看 1 -> 2）

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


                  
