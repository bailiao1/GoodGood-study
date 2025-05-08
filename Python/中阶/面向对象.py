# 1.面向对象和面向过程的区别(洗衣服类比)

# 面向过程（手洗）: 需要实现一个功能的时候，着重的是过程，分析出一个个步骤，并把一个个步骤用一个个函数实现。
# 强调“过程”和“步骤”，程序设计的重点在于：先分析清楚每一个步骤，比如洗衣服要先装水、加洗衣液、搓洗、冲水、晾干，然后每一个步骤写成一个函数，最后依次调用这些函数来完成任务。你就是流程的执行者，一步步做。

# 面向对象（机洗）：
# 强调“对象”和“职责”，程序设计的重点在于：先抽象出一个“洗衣机”对象，它内部已经定义好了如何完成洗衣服的流程。你只要告诉它“开始洗衣服”，它就会根据内部逻辑自动完成这些操作。你是使用者，只关心结果。

"""
面向对象的“偷懒”不是贬义，而是一种更高级的“封装与复用”思想。
两者并非对立，而是适用于不同规模与需求的项目。
小型程序可以直接用面向过程。
大型程序通常使用面向对象，更方便扩展、维护。
"""

# 2.类和对象
# 类就是一系列具有相同属性和行为的事物的统称，不是真实存在的事物
# 对象是类的具体实现，是类创建出来的真实存在的事物，面向对象思想的核心
# 在开发中，先有类，再有对象。

# 类的三要素
# 1.类名：名字
# 2.属性：对象的特征描述，用来说明是什么样子的
# 3.方法：对象具有的功能（行为），用来说明能做什么

# 定义类
# class 类名:             # 必须符合标识符规定，同时遵循大驼峰命名法，见名知义
#       代码块

# 例子：洗衣机类
class Washer:            #类名
    height = 800         #类属性：就是类所拥有的属性
  
# 查看类属性：类名.属性名
print(Washer.height)     # 800

#  新增类属性：类名.属性名 = 值
Washer.width = 450
print(Washer.width)      # 450

# 创建对象(过程也叫做实例化对象) 基本格式：对象名 = 类名()
wa = Washer()            # 第一次实例化
print(wa)                # <__main__.Washer object at 0x000002B9CA755040> 实例化对象在内发中的地址
wa2 = Washer()           # 第二次实例化
print(wa2)               # <__main__.Washer object at 0x0000026C224FCE80> 内存地址不同，他们是相同类创建的不同的对象


# 实例方法和实例属性
# 由对象调用，至少有一个self参数，执行实例方法的时候，会自动将调动该方法的对象赋值给self
class Washer:            # 创建类
    height = 800         # 赋值类属性
    capacity = 600
    def wash(self):      # 和定义函数一样，但需要self 表示当前调用 类中方法(实例方法) 的对象本身
        print("我会洗衣服")
        print(f"容量为：{Washer.capacity}")
      
wa = Washer()           # 创建实例化对象
wa.wash()               # 我会洗衣服            # 对应的实例方法只能由那个类的实例化对象调用

wa2 = Washer()          # 第二次实例化对象
wa2.wash()              # 我会洗衣服


# 实例属性(实例化对象会继承类的属性，不同实例化对象之间共享类属性，但实例属性不共享)
# 格式： self.属性名
class Person:                     # 类名
    name = "bai"                  # 类属性,定义在类中的属性
    def introduce(self):          # 实例方法
        print(f"大家好，我叫{self.name}，我今年{self.age}岁。")     # self 代表当前对象
      
bai = Person()                    # 实例化对象
bai.age = 18                      # 类中并没有定义age属性，给实例对象 bai 添加实例属性 age

bai.introduce()      # 大家好，我叫bai，我今年18岁。     # 对象调用类中方法
print(bai.age)       # 18                             # 实例属性只能由所属对象名访问,类名或该类的实例化对象都无法访问共享，会报错

# 调动类中方法时，会先查找当前实例化对象的属性，没有的话才会从类属性中调用(即：类属性可覆盖，但无法通过实例化对象修改)

hei = Person()       # 第二次实例化对象
print(hei.name)      # bai                           # 类属性，为公共属性。
print(hei.age)      # 实例化属性为私人属性，无法调用bai的，hei需要自己再定义一个。


#---------------------------------------------------------------------------------------------------------------------------------

# 每实例化一次就需要添加一次，效率不高，但是 ———— 构造函数__init__()登场！
# 作用:通常用来做属性初始化或者赋值操作。和包中自带的init文件类似，都是自动调用，完成初始化。即：在类实例化对象的时候，会被自动调用
class Test:
    def __init__(self):
        print("这是__init__()函数")
      
pr = Test()  # 这是__init__()函数                      #init被自动调用

# 例子一: 有类属性
class Person:                                          # 构建人类
    game = "鸣潮"                                       # 定义鸣潮为这类人的默认游戏
    def __init__(self,name,age,height,game=None):      # 定义 init 并加入形参，现在创建实例化对象时，必须要传入形参，game默认为空值(可以不填，默认使用类的属性)
        self.name = name                               # 明确定义 self(实例化对象) 的xx属性为传入的实参
        self.age = age
        self.height = height
        self.game = game if game else Person.game     # 转换实例属性，如果未传入game，使用类属性(判断是一定必要的，上面的game=None，如果没有就会直接被None覆盖掉，无法追溯类属性)
      
    def play(self):                                   # 类中方法
        print(f"{self.name}在玩{self.game}")
    def introduce(self):
        print(f"{self.name}的年龄是{self.age}岁，身高为{self.height}")
      
bai = Person("bai",99,170,"元神")      # 实例化对象，并定义实例属性
bai.play()                            # bai在玩元神
bai.introduce()                       # bai的年龄是99岁，身高为170

# 或更简单，类中不定义属性(全交给init默认参数)
class Person:
     def __init__(self,name,age,game="鸣潮"):     # 鸣潮为默认参数，可以输入，也可以不输
         self.name = name
         self.age = age
         self.game = game                        # 类属性需要通过显式赋值才能成为实例属性
     def play(self):
         print(f"{self.name} 在玩{self.game}")
bai = Person("bai",19)
bai.play()                                       # bai 在玩鸣潮


#-------------------------------------------------------------------------------------------------------

# 析构函数__del__()：删除对象的时候，解释器会默认调用__del__()方法，主要是表示该程序块或者函数已经全部执行结束
class Person:
    def __init__(self):
        print("我是init")
    def __del__(self):
        print("被销毁了")
      
p = Person()                # 我是init/end/被销毁了       # # 正常运行时，不会调用__del__(),当执行结束之后,系统才会自动执行它
del p                       # 但加入这行代码后，__del__() 被立刻调用，p被销毁，内存回收    # 我是init/被销毁了/end
print("end")              

#-------------------------------------------------------------------------------------------------------

# 面向对象的三大特性：封装、继承、多态

#---------------------------------------------------------------------------------------------------------

# 一、封装：隐藏对象中一些不希望被外部所访问到的属性或者方法
class Person:
    name = "bai"
pe = Person()
print(pe.name)
Person.name = "hei"            # hei , 通常类属性是可以在外部随意修改

# 私有属性/方法
# 1.xxx:普通属性/方法，如果是类中定义的，则类可以在任意地方使用
# 2._xxx:单下划线开头，声明私有属性/方法，如果定义在类中，外部可以使用，子类也可以继承
#        但是在另一个py文件中通过from xxx import * 导入时，无法导入（ 一般是为了避免于Python关键字冲突而采用的命名方法 ）
# 3.__xxx:双下划线开头，隐藏属性，如果定义在类中，无法在外部直接访问，子类不会继承，
#         要访问只能通过间接的方式，当另一个py文件中通过from xxx import *导入的时候，也无法导入（ 这种命名一般是python中的魔术方法或属性，都是有特殊含义或者功能的，不能轻易定义 ）

# 私有方法(文件内调用)
class Girl:
    def _buy(self):
        print("买买买")
wo = Girl()
wo._buy()                      # 买买买  对象可以调用，但在其他文件导入时无法使用

# 隐藏属性（私有权限），值允许在 类(class) 的内部使用，无法在外部通过 对象(self) 访问，实现：在属性名或者方法名前面加上两个下划线__
class Person:
    name = "bai"               # 类属性
    
    __age = 18                 # 隐藏属性
    def __play(self):          # 隐藏方法
        print("玩手机")
        
    def introduce(self):       # 实例方法
        print(f"{Person.name}的年龄是{Person.__age}")   # 在实例方法中可以访问到类属性和隐藏属性
        
    def funa(self):            # 再设置个平平无奇的实例方法
        Person.__play(self)    # 在实例方法中调用私有方法 
        self.__play()          # 或直接让 实例对象(self) 调用
        
pe = Person()                  
# print(pe.age)                  # 报错，无法在类外访问


# 如何在外部访问：第一种：（不正规）隐藏属性实际上是将名字修改为了：_类名__属性名  _Person__age
print(pe._Person__age)         # 18 成功访问到了
pe._Person__play()             # 玩手机  隐藏方法同样适用

pe._Person__age = 16        # 尝试修改
print(pe._Person__age)      # 16 被修改并打印

# 第二种：(正规) 在类的内部访问(就是调用之前在类中明确定义的方法，不翻墙) 
pe.introduce()              # bai的年龄是18  隐藏属性被访问
pe.funa()                   # 玩手机         隐藏方法同样被访问

#------------------------------------------------------------------------------------------

# 二、继承(不止实例化对象(self)可共享类(class)，新建类(class)同样也可以继承旧类(class))
# 让类与类之间转变为父子关系，子类默认继承父类的属性和方法
# 单继承
class Person:               # 父类
    def eat(self):
        print("我会吃饭")
    def sing(self):
        print("唱歌")
        
class Girl(Person):         # 子类
    def dance(self):
        print("跳舞")
        
girl = Girl()
girl.eat()                  # 我会吃饭  # 继承方法
girl.dance()                # 跳舞     # 自己的方法

class Boy(Person):pass      # 子类可以不止一个 / pass：占位符，代码区为空，不执行任何操作
boy = Boy()
boy.sing()                  # 唱歌
# 子类可以继承父类的属性和方法，就算没有，也可以使用父类的

# 继承的传递（多重继承）
class Father():
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")
        
class Son(Father):
    def eat(self):      # 方法重写并传承给子类
        print("大口吃饭")
        
class Grandson(Son): pass
    
bai = Grandson()
bai.eat()           # 大口吃饭      # 继承于父类
bai.sleep()         # 睡觉         # 起始于父类的父类(爷爷类)


# 父类的方法是可扩展的：继承父类的方法，子类也可以增加自己的功能
# supper是一个特殊的类，super()是使用super类创造出来的对象，可以调用父类中的方法
class Father():                   # 父类
    def money(self):              # 父类方法
        print("一百万")
        
class Son(Father):
    def money(self):              # 定义子类同名方法(默认覆盖)
        Father.money(self)        # 第一种方法：手动调用父类方法(Father这是类名啊，不是固定的)
        super().money()           # 第二种方法，super调用父类————简写版
        super(Son,self).money()   # 或 supper 完整写法(class(指定类),self(实例对象))
        
        print("一千万")           ＃ 这行才是子类自己的代码块
        
bai = Son()
bai.money()     # 一百万 / 一千万

class Grandson(Son):            # 孙类——子类的子类
    def money(self):            # 传家之法
        super().money()
#       super(Son,self).money() # 可跳过父亲直接调用爷爷         
        print("一个亿")
        
hei = Grandson()
hei.money()                     # 一百万 /n 一千万 /n 一个亿


# 多继承
# 子类可以拥有多个父类，并且具有所有父类的属性和方法
class Father(object):       # 父类一
    def money(self):
        print("一百万")
class Mother(object):       # 父类二
    def appearance(self):
        print("好看")
        
class Son(Father, Mother):  # 子类
    pass
    
bai = Son()
bai.money()         # 一百万      # 继承父类一
bai.appearance()    # 好看        # 继承父类二

# 如果不同的父类存在同名的方法(实际情况下，尽量避免这种情况)
class Father(object):       # 父类一
    def money(self):
        print("一百万")
class Mother(object):       # 父类二
    def money(self):
        print("两百万")
        
class Son(Father,Mother):pass
bai = Son()
bai.money()  # 一百万

class Son(Mother,Father):pass
bai = Son()
bai.money()  # 两百万        # 优先继承括号中位置靠前的类(MRO顺序)

# 方法的搜索顺序(__mro__)
print(Son.__mro__)          # (<class '__main__.Son'>, <class '__main__.Mother'>, <class '__main__.Father'>, <class 'object'>) 位置越靠前，优先级越高         
# 搜索方法时，从左往右，找到了方法就执行，如果找到最后一个类还是没有找到，就报错
# 多继承的弊端：容易引发冲突，会导致代码设计的复杂度变高

#-----------------------------------------------------------------------------------------------------------------

# 多态：指同一种行为具有不同的表现形式。
# 本质：“写统一的代码，调用不同对象的实现” —— 是代码可扩展性的基础。
print(10+10)                # 20         # + 作为算术运算符：可以实现整型之间的相加操作
print("10"+"10")            # 1010       # + 作为字符串拼接：实现字符串之间的拼接操作

# 多态的前提：继承 、重写(覆盖)
class Animal(object):       # 父类：动物类
    def shout(self):        # 原始shout方法
        print("叫")
        
class Cat(Animal):          # 子类一：猫猫类
    def shout(self):        # 猫的shout是喵喵
        print("喵喵喵")
class Dog(Animal):          # 子类二：狗狗类
    def shout(self):        # 狗的shout是汪汪
        print("汪汪汪")
        
cat = Cat()
cat.shout()         # 喵喵喵
dog = Dog()                                    # 都是shout，但在不同类下的表现不同
dog.shout()         # 汪汪汪 


# 多态性：一种调用方式，不同的执行结果（定义一个统一的接口，一个接口多种实现）
def test(obj):      
    obj.shout()
    
test(cat)           # 喵喵喵
test(dog)           # 汪汪汪

# test函数传入不同的对象，执行不同对象的shout方法


#--------------------------------------------------------------------------------------------------------------------

# 小扩展


# 静态方法
# 使用@staticamethod来进行修饰，静态方法没有 self(实例对象) 与 cls(类) 参数的限制
# 静态方法与类无关，可以被转换成函数使用
class Person(object):
    @staticmethod
    def study(name):                # 静态方法也可以设置形参(就和正常函数一样了，但只能由类或实例对象调用。否则会报错)
        print(f"{name}会学习")
# 优势是：取消了不必要的参数传递，有利于减少不必要的内存占用和性能消耗)
Person.study("人")                  # 人会学习
man = Person()                      # 调用方法时传参数
man.study("bai")                    # bai会学习

# 类方法
# 使用装饰器 @classmethod 来标识为类方法，对于类方法，第一个参数必须是类对象，一般是以cls作为第一个参数
# 类方法内部可以访问类属性，或者调用其他的类方法
class Person(object):
    name = "bai"        # 内属性
    @classmethod
    def sleep(cls):     # cls代表类对象本身，类本质上是也是一个对象
        print("人类在睡觉")
        print(cls.name)
Person.sleep()      # 人类在睡觉
# 当方法中需要使用到类对象（如访问私有类属性等），定义类方法


# 经典类与新式类
class A: pass            # 经典类：不由任意内置类型派生出的类
class Animal:            # 但Python3中，这一概念被废弃，所有类都默认为新式类，继承object
    def walk(self):
        print("走路")
class Dog(Animal):       # 派生类，继承父类，但拥有不同于父类的属性或方法
    name = "小灰"
    def bite(self):
        print("嗷呜")
        
# object，python为所有对象提供的基类（顶级父类），提供了一些内置的属性和方法,可以使用dir()查看
print(dir(object))       # 所有类都继承object类，就算它什么都没继承，也默认继承object类

