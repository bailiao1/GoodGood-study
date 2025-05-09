# 元编程（Metaprogramming） 是一种让程序可以“操作程序本身”的编程方式。简单来说，就是 —— 写代码的代码。
# 普通编程:写代码，操作数据
#  元编程 :写代码，操作"代码本体"，不是写出结果，而是写出会生成结果的逻辑。

# Python中常见的元编程手段：
# 反射
# getatter(obj,"name")                    # 动态获取属性名

# 动态添加属性
# obj.new_att r = 123                      # 在运行时添加变量

# 装饰器
# @log_timr                               # 给函数套功能，修改它的行为

# 魔术方法            
# __getatter__,__call__                   # 控制对象行为的底层接口

# 类的创建控制
# type(）、__new__、元类                    # 动态生成类、控制类创建过程

#-----------------------------------------------------------------------------------------

# 用元编程动态创建一个类
def create_class(name):
    return type(name,(object,),{"say_hi : lambda self: print(f"Hi from {name}") "})          # type()不止用于查看类型，还可以创建类: type(类名(内部名), 父类元组(父类可以不止一个), 属性字典)
                                                                                             
MyClass = create_class("MyClass")        # type定义的内部名可通过__name__查看，此时定义的是引用变量名
obj = MyClass()                          # 实例化对象
obj.say_hi()                             # 调用实例方法 输出 Hi from MyClass (此时的自建类还不完整，无法使用对象名 类中是name而不是self.name)




