# 异常：是一个事件，在程序执行过程中发生，影响了程序的正常执行(就是报错啦)
# 异常处理的最终目的：让程序在有异常时，仍然能正常运行(让你的代码就算报错，依旧能运行下去，或捕捉到这个bug，后期好处理)

# 异常处理格式一：try...except...(试试，如果报错，就运行except下的代码)

# 法一
try:                     
    print(a)                    # 这里的 a 还没定义，所以会报：NameError: name 'a' is not defined
except:                  
    print("出现错误")            # 出现错误(没报错，只是执行了这个print)

# 法二（加入指定错误捕捉：只有指定的错误出现，才会被捉住，出现其他异常的话，还是会爆红）
try:
    print(a)
except NameError as e:                  # 指定捕获异常类型为NameError，取别名为e ( 如果没取别名，直接在下面使用print(NameError)，只会打印错误的类型：<class 'NameError'> )
    print(e)                            # name 'a' is not defined,提醒了，但没报错
    print("异常属性：", type(e).__name__)          # NameError                    # e 同样可以打印异常的属性
    print("异常说明：", str(e))                    # name 'a' is not defined      # 异常的说明
    print("参数列表：", e.args)                    # 参数列表： ("name 'a' is not defined",)        # 如果报错的参数不止一个，都会写进这个元组

# 法三(Exception 万能捕捉。可以捕获任意异常)
try:
    print(a)
except Exception as e:    
    print(e)

# 法四：多分支异常(多设置几个except，触发对应的错误就去执行对应的except)
try:
    print(a)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except NameError as e:         # 命名错误
    print('命名错误')


  #-----------------------------------------------------------------------------------------------------
  
# 异常捕获格式二  try except else
# else 只有在没有异常时才会执行的代码
  
dic ={"name":"bai"}

try:
    print(dic["age"])       # 错误
    print(dic["name"])      # 正常
except Exception:
    print("出现错误")
else:                       # try依旧是一个整体，只要其中一个触发了异常，就会去执行except，而不是部分执行，部分被截
    print('没有捕获到异常')

  
# 异常排查鸡肋小函数
def func(a):                        # 输入一个名
    try:
        print(dic[a],end="")        # 在字典中看看有没有这个键，有的话就输出值
    except Exception:               # 没有就报错，但捕捉，继续看下一个名
        print(f"{a}出现错误")
    else:                           # 回应下，完全正常
        print('没有捕获到异常')
      
a="name","age","city"

list(map(func,a))          # 格式一，map 将元素一一映射

for i in a:                # or 格式二，for循环遍历执行
    func(i)


#---------------------------------------------------------------------------------
  
# 异常处理格式三   try...except...finally
try:
    print(a)
except NameError:
    print("出现错误")        # 出现错误
finally:                    # 无论是否有异常，都会执行的代码 (就算把except捕捉移除，报红了，finally下的代码依旧能执行)
    print("哈")             # 哈

#----------------------------------------------------------  
  
# 捕获异常四————完整捕获异常
try:
    n = int(input("请输入一个整数"))
    print(10/n)                      # 分母不得为零，否则会报错
except ValueError:                   # 指定捕获异常
    print("请输入正确的数据")
except Exception as e:               # 万能捕获异常
    print("未知错误 %s "%e)
else:
    print("没有异常时执行的代码")
finally:
    print("无论有无异常都会执行的代码")


#----------------------------------------------------------------------
  
# 手动抛出异常 raise
raise Exception("我抛出了一个异常")  
print("笑啦")                       # 只要执行了raise语法，代码就不会继续往下运行，效果等同真报错

# 应用：当密码长度不足。就报异常
while True:                        # While循环，一直到下面触发break
    try:                           # 需要配合错误捕捉，避免报错打断进程
        pw = input("请输入您的密码")
        if len(pw) < 6:            # 触发报错的条件
            raise Exception("密码长度不足六位。，输入失败")
        else:                      # 如果没触发，就————
            print("密码输入成功")
            break                  # 结束循环
    except Exception as e:         # except和上面的try配合，防止进程被打断
        print(e)
      
# 函数形式：
def login():
    while True:                  
        try:
            pw = input("请输入您的密码")
            if len(pw) >= 6:
                return "密码输入成功"      # 不需要再添加break终止循环，直接return结束函数
            raise Exception("长度不足六位，输入失败")
        except Exception as e:           # 在函数内捕获异常，防止raise结束代码，被迫终止
            print(e)
print(login())                           # return不会显示返回值，需要打印。


#---------------------------------------------------------------------------------------------------------------

# 小扩展

# 异常类型





# 一些罕见的异常属性(...至今没用过)
# .__cause__	    如果是由另一个异常引发的，会记录原异常
# .__context__	    上下文中前一个异常（嵌套异常）
# .__traceback__	包含 traceback 对象（调用栈）, 查源头定位


