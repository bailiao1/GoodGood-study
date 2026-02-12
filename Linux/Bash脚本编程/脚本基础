# 创建脚本
touch script.sh

# 写入shebang(不是必须但推荐)
echo '#!/bin/bash' > script.sh      # 这不是注释，脚本内告诉系统用哪个解释器执行

#!/usr/bin/env bash 更安全，防止bash不在/bin，env 会在 PATH 里找

# 追加脚本内容（单引号'' 强引用，里面的所有字符都保持原样，没有任何特殊含义）
echo 'echo "hello linux"'

# chmod（修改文件权限的命令）
chmod +x script.sh                  # 给脚本script.sh 添加可执行的权限（+（增加）x（执行execute））

# 执行
./script.sh


# 多行写入 ('EOF'加上单引号，保证内容原封不动地写入文件)
cat > script.sh <<'EOF'
#!/usr/bin/env bash
echo "hello linux"
EOF

# 特殊变量：
echo $0                     # 脚本名
echo $#                     # 参数数量
echo $@                     # 所有参数

# 条件判断（test / [] / [[]]）
# 数值比较包括: -lt(小于) , -le(小于等于) , -eq(等于) , -ne(不等于) , -gt(大于) , -ge(大于等于)
# 字符串比较包括：=(等于) , !=(不等于) , -z(空) , -n(非空)
# 文件测试： -f(文件) ， -d(目录) , -e(存在) , -r(可读) , -w(可写) , -x(可执行)

# [ xxx ] 本质是test命令，必须有空格：[ 条件 ]，判断真假依赖“退出状态码”（0为真，非0为假）

# 数值比较
if [ "$1" -gt 10 ]; then        # $1代表执行脚本时传入的第一个位置参数，建议给变量加双引号，避免参数为空时报错
    echo "大于10"
elif [[ $1 -eq 10 ]]; then      # [[]]更安全写法，不需要给变量强制加引号,支持正则匹配,< > 不会被当成重定向
    echo "等于10"                # 非POSIX，/bin/sh 可能跑不了，开头应该 #!/usr/bin/env bash
else
    echo "小于10"
fi                              # if判断结束

# 字符串比较
if [[ $name == "Bai" ]]; then   # [[]]中更常用 ==
    echo "Hi Bai"
fi
if [ -z "$name" ]; then
    echo "为空"
fi

# 文件测试
if [ -f "/etc/passwd" ]; then            # -f 判断路径是否存在，且必须是一个普通文件"regular file"
    echo "文件存在"
fi

if [ -d "/tmp" ]; then                   # -d 判断目录
    echo "目录存在"
fi

# for循环
for i in {1..5}; do
    echo "Number: $i"
done

for file in *.txt; fo
    echo "$file"
done

# while循环
count=1
while [ "$count" -le 5 ]; do
    echo "Count: $count"
    count=$((count + 1))                # $(( ... ))算数扩展，会进行整数计算
done

# 现代写法，需要 #!/usr/bin/env bash
while (( count <= 5 )); do
    echo "Count: $count"
    ((count++))
done

# 函数
say_hello() {
    local name=$1                       # local声明函数内局部变量，$1（传入的第一个参数）
    echo "hello $name"
}
# 调用
say_hello "Bai"   

add() {
    local sum$(( $1 + $2 ))
    echo "Sum is: $sum"
}
result=$(add 10 20)
echo "Sum is: &result"
