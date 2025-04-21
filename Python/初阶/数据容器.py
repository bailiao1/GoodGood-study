# 列表 (List)
a = [1,2.5,'3',[4,5]]                                  # 将一串数据保存到一个变量中
b = []                                                 # 列表可以为空
print(a)                                               # [1, 2.5, '3', [4]]   (列表里可以保存各种数据类型)
print(b)                                               # []

# 索引
print(a[3][0])                                          # 4 (取出第 4 个值中的第 1 个值)索引从0开始计算

# 切片
print(a[0:3:2])                                         # [1, '3'] (取出第1到第4的值，步长为2)


# 添加元素
b.append("hello")                                       # 整体添加
print(b)                                                # ['hello']

b.extend("ld")                                          # 分散添加(仅限可迭代对象:字符串,列表......)
print(b)                                                # ['hello', 'l', 'd'] ("ld"字符串被拆分成一个个单独的字符)

b.insert(1,'wor')                        # 指定位置添加
print(b)                                                # ['hello', 'wor', 'l', 'd'] 在原本索引[1]的插入


# 移除元素
b.remove('wor')                                         # 根据元素移除
print(b)                                                # ['hello', 'l', 'd']

del b[2]                                                # 根据下标移除
print(b)                                                # ['hello', 'l']

c = b.pop(1)                                            # 移除指定小标并返回值                           
print(f"b:{b} c:{c}")                                   # b:['hello'] c:l
