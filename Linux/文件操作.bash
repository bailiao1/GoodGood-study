# 查看当前所在目录的绝对路径
pwd

# 列出目录下的所有文件
ls
ls -l    # 详细列出文件信息
ls -la   # 列出所有文件，包括 "." 开头的隐藏文件
ls -lh   # 人类可读的大小格式：kb/mb 
ls /home # 列出指定目录下的文件(这里用home示范)


# 切换目录
/ (root)
├── home/
│   └── alice/
│       ├── Documents/
│       │   ├── work/
│       │   │   └── report.txt
│       │   └── personal/
│       ├── Downloads/
│       └── Pictures/
└── etc/
# 当前所在/home/alice

cd /home/alice/Documents # "/" 开头，指定绝对路径目录
cd Document              # 相对路径进入，
cd Document/work

cd ..                    # 返回上一级目录
cd ../../etc             # 从alice开始返回两次上级，回到root目录，再进入etc
cd ~                     # 导航回home目录，单独使用cd命令也会返回home


# 创建和删除
mkdir new_floder           # 创建空目录(win的文件夹)
mkdir -p new_floder/child  # 创建多级目录

touch file.txt             # 创建空文件
rm file.txt                # 删除指定文件（不包括目录）

rm -r new_floder           # 递归删除目录及内部的文件，子目录
rmdir new_floder           # 只删除空目录（非空会报错）

# 可以先删除目录内所有文件（/*）
rm new_floder/*      # 删除所有文件（不包括子目录）
rm -r new_floder/*   # 删除所有文件和子目录


# 查看文件
cat
