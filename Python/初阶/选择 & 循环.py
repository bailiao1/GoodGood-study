# 判断分支:如果...或者...否则...

a = int(input("输入值:"))
if a:                                           # 如果(if) a 不为 0、不为 False、不为 None、不为 ""，就为 True
    print("a 有值")                              # 那么这行就会被执行
else:
    print("a 没有值")                            # 否则就执行这行


# 小例子：
a = int(input("输入你的得分："))
if 90 <= a <= 100:                              # 判断条件，为真就执行，为假就跳过
    print("A级")

elif 80 <= a < 90:                              # if拓展，如果if为假，就判断elif，如果elif也为假，继续跳过
    print("B级")

elif 70 <= a < 80:                              # 继续判断下面的elif条件，只要一个成立，就输出对应的代码
    print("C级")

elif 60 <= a < 70:
    print("D级别")

elif 0 <= a < 60:
    print("F...")
    if a > 50:                                  # if可嵌套
        print("但还是有希望的哈...")

else:                                           # 如果以上全都为False，最终执行else
    print("别乱输啊喂...")


#---------------------------------------------------------------------------------------------------------


# 循环语句：如果判断为True，就执行

# for循环
for i in range(1,6):                                # i：临时变量，可自定义名称。  range：(start,end,step)在这里是从1到6，每次加1
    print(i)                                        # i < 6; i+=1; 总共循环5次

for i in range(6):                                  # 直接从0-5循环6次：012345
    print(i)


# 例子(反向)
for i in range(5,-1,-1):                            # i < -1; i-=1; 从5-0,总共循环6次: 543210
    print(i)

# 例子(循环嵌套)
for i in range(1,10):                                # 外循环生成1-9
    for j in range(1,i+1):                           # 外循环一轮，内循环完整运作一个周期
        print(f"{j}*{i}={j*i}",end=' ')              # 循环体(最终执行 j (9+8+7+6+5+4+3+2+1)次，生成九九乘法表)
    print("\n")                                      # 这是外循环的循环体(只会执行 i (9)次)

# enumerate():返回索引与值
lst = ["apple", "banana", "cherry"]
for index, value in enumerate(lst):                    # 0:apple  1:banana  2:cherry
    print(index, value,sep=':',end="\t")


# zip 同步遍历
names = ["a", "b", "c"]
scores = [60, 70, 80]
for name, score in zip(names, scores):                  # a 60	b 70	c 80
    print(name, score,end="\t")



# for循环还可以迭代器取值(可迭代对象(iterator)：能够“一个一个”取出值的对象，就是可迭代对象，可以被 for 循环处理。)

for i in "Hello World":                                    # H_l_l_o_ _(e被跳过，W之后(包括W都被截断))
    if i == 'e':
        continue                                           # continue：遇到某条件，直接跳过当前循环，进入下一轮
    elif i == 'W':
        break                                              # break：遇到某条件，直接退出循环(直接结束)
    print(i,end='_')

print("\n")                                                # 手动打印换行符

a = {"name":"bai","age":18,"weight":55,"height":111}
for k, v in a.items():                               # 可以多变量同步
    print(f"{k}={v}",end='--')                       # name=bai--age=18--weight=55--height=111--

# 常见的可迭代对象有：字符串(str),列表(list),字典(dict),元组(tuple),集合(set),range对象,文件(file)...
# 不可迭代的对象就是那些分不开的玩意：单个数值(int、float、boolean、none_type)...
# 之后还有自定义迭代器类。。。(学个屁编程，这么多概念怎么记？)

# 小拓展：判断迭代器类型
from collections.abc import Iterable                 # 只需要先导入迭代器的type
print(isinstance("Hello", Iterable))                 # isinstance类型判断：可以用于判断int,str等等类型
print(isinstance(123, Iterable))                     # False


#---------------------------------------------------------------------------------------------------------------------------------



# while循环：只要符合条件，就一直循环下去(自由度超级高,所以记得设置结束条件,避免死循环)

i = 0                                               # 设置参数
while i < 10:                                       # 判断条件，如果为True，就循环；False就退出
    if i == 5:
        print("继续循环请按1,跳过回合请按2,中断循环请按0")
        a = input("请输入:")                         # 其实就 0 和 2 有效哈
        if a == '0':
            break                                   # break 和 continue在这同样适用
        elif a == '2':
            i += 1                                  # 避免continue跳过下面的i更新，这里手动更新参数(不然就卡在这了)
            continue
    print(i)                                        # 循环体(我们需要重复执行的任务...)
    i += 1                                          # 参数更新,让循环可终
    
else:                                               # while + else：正常退出才会执行 else，break终止的话不会执行
    print("正常结束啦！")
    


# 经典死循环(某些场景需要)
while True:
    a = input()
    if a.lower() == 'exit':                         # lower(): 字符串转小写(防止大写字母无法识别)
        break
    print(a)
