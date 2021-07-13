# 前言

- Java用途
  - 网站后台
  - SaaS云
  - app
  - 大数据平台
  - 系统
  - 桌面工具
- 生态
  - 后端
  - 全栈
- 95年诞生于Sun公司，Sun后来被Oracle收购
- 封装！
- TEIOBE网站

- C：底层
  - 内存，指针
- Java摒弃了很多C/C++的问题
- C++：游戏开发
- 相关学习
  - Java基础
    - 语法
    - 面向对象
    - GUI
    - 多线程
    - 网络编程
    - JVM
    - JUC
  - 数据库
    - MySQL
    - JDMC
    - UML
  - 前端
    - HTML
    - CSS
    - JS(JavaScript)
    - jQurery
    - Vue
  - JavaWeb
    - 网站后台
  - SSM框架
    - MyBatis
    - Spring
    - SpringMVC
    - Git
  - Linux
    - 基础
    - Redis
    - Nginx
    - Docker
  - SpringBoot
    - 微服务
  - SpringCloud
    - 微服务，微服务架构
  - Hadoop
    - 大数据的入门





# 预科

- 博客
- markdown
- 计算机
- 硬件

  - 冯·诺依曼体系结构
- 软件

  - 系统
    - DOS
    - Windows
    - Linux
    - Unix
    - Mac
    - Android
    - IOS
- Dos命令

``` bash
 # 盘符切换
  C:\Users\DELL>D:
  
  D:\>dir
   驱动器 D 中的卷是 DATA
   卷的序列号是 90FF-156C
   
   
  # 查看当前目录下的所有文件 dir
  D:\>dir
   驱动器 D 中的卷是 DATA
   卷的序列号是 90FF-156C
  
   D:\ 的目录
  
  2021/07/02  15:50    <DIR>          !!!Learn
  2021/07/07  20:46    <DIR>          !!!Learning_Recording
  2021/06/10  10:20    <DIR>          !!!Master
  2021/07/06  22:21    <DIR>          !!!Temp
  2021/06/04  20:42    <DIR>          !!!Temp_Learn
  2020/03/09  18:06    <DIR>          Adobe Acrobat DC
  2021/03/28  18:26    <DIR>          AE
  
  
  # 切换目录 cd
  D:\>cd PS
  
  D:\PS>cd ..
  
  D:\>cd \d c:
  文件名、目录名或卷标语法不正确。
  
  D:\>cd /d C:   # /d：参数
  
  C:\Users\DELL>
  
  # 清屏
  cls
  
  #退出
   exit
   
   
  # IP查看
  ipconfig
  ipconfig/all
  
  # 打开应用
  C:\Users\DELL>calc
  
  C:\Users\DELL>mspaint
  
  C:\Users\DELL>notepad
  
  # ping 
  
  # 桌面
  C:\Users\DELL>cd /d C:\Users\DELL\Desktop
  
  C:\Users\DELL\Desktop>
  
  # 创建文件夹（make dir）
  md 文件夹名称
  # 删除文件夹（remove dir）
  rd 文件夹名称
  
  #创建文件
  cd>文件名
  #删除文件
  del 文件名
```



- 发展史
  - 机器语言：二进制，计算机直接使用
  - 汇编语言
    - 应用：逆向工程，机器人，病毒
  - 高级语言
    - 面向过程
    - 面向对象

# 入门

- 72年：C
- 82年：C++
  - 复杂
  - 图形领域
  - 游戏领域
- 95年：Java
  - 语法类似于C
  - 面向对象
  - 无指针
  - 无内存管理
  - 可移植性
  - 高性能
  - 分布式
  - 动态性
  - 多线程
  - Hadoop：大数据
  - Android
- 三大版本
  - JavaSE 标准版
  - JavaME 嵌入式开发（几乎消失了）
  - JavaEE 企业级
- JDK：Java开发工具
- JRE：Java运行环境
- JVM：Java虚拟机（作用：实现跨平台编译）
- 安装JDK8

``` bash 
PS C:\Users\DELL> java -version
  java version "1.8.0_291"
  Java(TM) SE Runtime Environment (build 1.8.0_291-b10)
  Java HotSpot(TM) 64-Bit Server VM (build 25.291-b10, mixed mode)
```

  - 安装文件夹下的文件
    - bin：可执行文件
      - jav.exe
      - javac.exe
    - include :于C语言相关
    - jre
    - lib
      - 库

- hello world

``` java
    public class Hello //hello是类名要与.java文件名对应
    {
        public static void main(String[] args) //public 小写
        {
            System.out.print("hello world!"); //大写System
        }
    }
```

  - ![image-20210707223016702](Java.assets/image-20210707223016702.png)

- java 运行机制
  - 编译型       complie
    - 全部翻译——操作系统
    - C/C++
  - 解释型
    - 边读边翻译——网页
    - python
  - 两者区别：时机不同

![image-20210707223710807](Java.assets/image-20210707223710807.png)

- 使用IDEA作为集成开发环境

# 基础语法

## 注释

- 单行注释

- 多行注释

- 文档注释

```java
package Base_knowledge;

/**
 * -*- coding : utf-8 -*-
 * Time       : 2021/7/7 23:49
 * Author     : MurphyHou
 * Proj_Name  : JavaSE
 * File_Name  : Base_knowledge.Hello.java
 * Software   : IntelliJ IDEA
 * =======Here We Go!=======
 */

public class Hello {
    public static void main(String[] args) {
        System.out.println("hello world");


        //单行注释


        /*多行注释*/
        /*
        这是注释
        这是注释
        这是注释
         */


        //JavaDoc:
        /**
         * 注释
         * 注释
         * 注释
         */
    }
}

```

## 标识符和关键字

- 关键字

  - 类名，变量名，方法


- 标识符

  - 所有的标识符都应该以字母，美元$，或下划线_开头
  - 首字母之后是任意的字母，或美元$，或下划线_或数字
  - 不使用关键字
  - 注意大小写，A与a不代表同一个变量
  - 可以用中文作为标识符，但是不建议
  - 类名也可以用中文，但也不建议

## 数据类型

- 强类型语言
  - 要求变量的使用严格符合规定
  - 所有的变量都必须先定义后才能使用
  - 高安全性
  - 速度慢
  - 强类型语言：C/C++
  - 弱类型语言：python，JS，VB
  
- 数据类型

  - 基本类型
    - 数值类型
      - 整数类型
        - byte  一个字节
        - short  两个字节
        - int  四个字节
        - long  八个字节
      - 浮点类型
        - float  四个字节
        - double 八个字节
      - 字符类型
        - char   两个字节
    - Boolean类型
      - 占1位，其值只有true和false两个

``` java
package Base_knowledge;

/**
 * -*- coding : utf-8 -*-
 * Time       : 2021/7/8 20:32
 * Author     : MurphyHou
 * Proj_Name  : JavaSE
 * File_Name  : Base_knowledge.Value_type.java
 * Software   : IntelliJ IDEA
 * =======Here We Go!=======
 */

public class Value_type {
    public static void main(String[] args) {
        byte a=1;
        short b=2;
        int c=3;
        long d=4L;   //long类型要在数字后面加上l/L

        float e=50.1f;  //float后面加上F/f
        double f=3.1415926;

        char g='a';

        String h="dwaawdawd";//String 不是关键词，是一个类

        boolean flag=true;
        boolean flag1=false;
    }
}

```

``` java
import java.math.BigDecimal;

/**
 * -*- coding : utf-8 -*-
 * Time       : 2021/7/8 20:53
 * Author     : MurphyHou
 * Proj_Name  : JavaSE
 * File_Name  : Data_expand.java
 * Software   : IntelliJ IDEA
 * =======Here We Go!=======
 */

public class Data_expand {
    public static void main(String[] args) {
        //整数拓展//进制//二进制：0b//十进制//八进制 0//十六进制 0x
        int n1=10;
        int n2=010;
        int n3=0x10;
        System.out.println(n1);
        System.out.println(n2);
        System.out.println(n3);
        System.out.println("==================================");
        //浮点数拓展
        //folat 有限 离散 舍入误差  大约  接近但不等于
        //double

        //最好完全使用浮点数进行比较

        float f=0.1f;
        double d=1.0/10;

        System.out.println(f==d);
        System.out.println(f);
        System.out.println(d);

        float d1=53485468864f;
        float d2=d1+1;

        System.out.println(d1==d2);


        //BigDecimal 数学工具类



        // 字符类型拓展
        System.out.println("==================================");

        char c1='a';
        char c2='中';
        System.out.println(c1);
        System.out.println((int)c1); //强制类型转换

        System.out.println(c2);
        System.out.println((int)c2);


        //字符本身就是数字
        //char 编码：Unicode 2字节  0-65536

        char c3='\u0061';
        System.out.println(c3);  //a

        System.out.println("==================================");
        //转义字符
        System.out.println("hello\tworld");
        // \t:table
        // \n:换行


        System.out.println("==================================");

        String sa=new String("hello world");//对象：内存分析
        String sb=new String("hello world");

        System.out.println(sa==sb);


        String sc="hello world";
        String sd="hello world";
        System.out.println(sc == sd);

        System.out.println("==================================");
        //布尔值拓展
        boolean flag=true;
        if (flag){
            System.out.println("true");
        }

        if(flag==true){
            System.out.println("true");
        }
    }
}
```



  - 引用类型
    - 类
    - 接口
    - 数组

## 类型转换

- 强制类型转换
- 自动类型转换

``` java
/**
 * -*- coding : utf-8 -*-
 * Time       : 2021/7/8 21:19
 * Author     : MurphyHou
 * Proj_Name  : JavaSE
 * File_Name  : Type_conversion.java
 * Software   : IntelliJ IDEA
 * =======Here We Go!=======
 */

public class Type_conversion {
    public static void main(String[] args) {
        //强制类型转换
        int i=128;
        byte b =(byte)i;

        System.out.println(i); //128
        System.out.println(b);  //-128

        //自动类型转换
        int j=128;
        double c =i;

        System.out.println(j); //128
        System.out.println(c);  //-128

        /*
        不对布尔值进行转换
        不能把对象类型转换为不相干的类型
        高容量到低容量：强制转换
        转换：内存溢出，精度问题
         */
    }
}

```



## 变量 常量

- 变量名
- 变量类型
- 作用域
  - 类变量  static
  - 实例变量
  - 局部变量

``` java
/**
 * -*- coding : utf-8 -*-
 * Time       : 2021/7/8 21:33
 * Author     : MurphyHou
 * Proj_Name  : JavaSE
 * File_Name  : Variable.java
 * Software   : IntelliJ IDEA
 * =======Here We Go!=======
 */
//类
public class Variable {
    //属性：变量

    //实例变量：从属于对象;不初始化自动会有默认值
    //数值类型的默认值：0  0.0
    //布尔值默认值是false
    //处理基本类型，其他的默认值都是null
    String name;
    int age;

    //类变量,从属于类
    static double salary=2500;


// 定义常量
    static final double PI=3.14;
    final static double PI1=3.14;
    //final 是修饰符，不存在先后顺序


    //main方法
    public static void main(String[] args) {
        //局部变量：定义在方法里的变量，必须声明和初始化
        //寿命就是在这个方法里

        //变量类型 变量名字=new Variable();
        Variable variable = new Variable();
        System.out.println(variable.age);
        System.out.println(variable.name);

        System.out.println(salary);



        //定义常量

        final
    }

    //其他的方法
    public void add(){

    }
}

```

![image-20210708215409533](Java.assets/image-20210708215409533.png)

## 运算符

![image-20210708215630496](Java.assets/image-20210708215630496.png)

``` java
package Base_knowledge;

/**
 * -*- coding : utf-8 -*-
 * Time       : 2021/7/8 21:55
 * Author     : MurphyHou
 * Proj_Name  : JavaSE
 * File_Name  : Base_knowledge.Operator.java
 * Software   : IntelliJ IDEA
 * =======Here We Go!=======
 */

public class Operator {
    public static void main(String[] args) {
        //二元运算符

        int a=10;
        int b=20;
        int c=30;
        int d=40;

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a/b);
        System.out.println(a*b);

        long n1=1554687436848656356L;
        int n2=123;
        short n3=10;
        byte n4=8;
        System.out.println("==================================");
        System.out.println(n1+n2+n3+n4);//long  有long则为long，有double则为double
        System.out.println(n2+n3+n4);//int  无long则为int
        System.out.println(n3+n4);//int

        System.out.println("==================================");
        //Math类
        double pow=Math.pow(2,3);
        System.out.println(pow);

        System.out.println("==================================");

        boolean aaa=true;
        boolean bbb=false;

        System.out.println("aaa&&bbb="+(aaa&&bbb));
        System.out.println("aaa||bbb="+(aaa||bbb));
        System.out.println("!(aaa&&bbb)"+!(aaa&&bbb));

        //短路运算
        System.out.println("==================================");
        int ccc=5;
        boolean ddd=(ccc<4)&&(ccc++<4);
        System.out.println(ddd);
        System.out.println(ccc);
        System.out.println("==================================");

        
        //字符串连接符   +
        int num1=10;
        int num2=20;
        System.out.println(""+num1+num2);
        System.out.println(num1+num2);
        System.out.println(num1+num2+"");

    }
}

```



## 包机制、JavaDoc

![image-20210708223509417](Java.assets/image-20210708223509417.png)

![image-20210708223937723](Java.assets/image-20210708223937723.png)

![image-20210708224317554](Java.assets/image-20210708224317554.png)



# 流程控制



## 用户交互 scanner

```java
java.util.Scanner
```

- Scanner类中的方法

``` markdown
1. next()
	a.一定要读取到有效字符后才可以结束输入
	b.对输入有效字符之前遇到的空白，next()方法会自动将其去掉
	c.只有输入有效字符后才将其后面输入的空白作为分隔符或者结束符
	d.next()不能得到带有空格的字符串
2.hasNext()

3. nextLine()
	a.以ENTER为结束符，也就是说，nextLine()方法输入回车之前的所有字符。
	b.可以获得空白。
4.hasNextLine()

5. nextInt()
6.nextFloat()
7.



```

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/8 23:16
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : scanner.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package Process_Control;

import java.util.Scanner; //导入Scanner包

public class ScannerDemo {
    public static void main(String[] args) {
        //创建一个扫描器，用于接收键盘数据
        Scanner scanner = new Scanner(System.in);


        System.out.println("=====使用next方式接收=====");

        //判断用户有没有输入字符串
        if (scanner.hasNext()){
            //使用next方式接收
            String str=scanner.next();
            System.out.println("输入的内容："+str);

            /*
            =====使用next方式接收=====
            hello world
            输入的内容：hello
             */
        }
        System.out.println("===使用nextLine方式接收===");

        if (scanner.hasNextLine())
        {
            String str1=scanner.nextLine();
            System.out.println("输入的内容："+str1);

            /*
            ===使用nextLine方式接收===
            hello world
            输入的内容：hello world
             */
        }
        scanner.close();//凡是属于IO流的类如果不关闭会一直占用资源，因此用完应该立刻关闭
    }
}

```

## 顺序结构

## 选择结构

if-else

switch-case结构：支持byte，short,int,char,String（JDK7之后）类型

## 循环结构

while

do--while

for

for_增强型

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/9 21:09
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : ForStrength.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package Process_Control;

public class ForStrength {
    public static void main(String[] args) {
        int[] num={10,20,30,40,50,60};
        //遍历数组元素
        for (int x:num)
        {
            System.out.println(x);
        }
        System.out.println("=======================");

        int i;

        for (i=0;i<6;i++){
            System.out.println(num[i]);
        }
    }
}

```

## break&continue

break:终止循环

continue：终止某次循环

goto：无

``` markdown
在C/C++中，goto常被用于跳出多重循环。但goto 语句的使用往往会使程序的可读性降低，所以 Java 不允许 goto 跳转。实际上，自从“goto有害论”提出后，软件开发就不建议使用goto了，但是Java中依然保留了goto这个关键字留作备用，但这个关键字没有任何作用，只是为了将来可能的扩展，防止使用goto作为程序中的标识符。
　　类似地，Java中的const也只是一个不起作用的保留关键字（不具备C语言中定义常量的作用，Java中要想定义常量使用final关键字），与goto一样防止作为程序中的标识符。
```
# 方法

类似于其他语言中的函数

## 定义及调用

``` markdown
System.out.println()
    System:类
    out:对象
    println():方法
```

``` markdown
1.方法是解决一类问题的步骤的有序组合
2.方法包含于类或对象中
3.方法在程序中被创建，在其他地方被引用
```

``` markdown
修饰符 返回值类型 方法名（参数类型 参数名）
{
	方法体；
	
	return 返回值；
}

```

## 方法重载

重载就是在一个类中，有相同的函数名称，但形参不同的函数

``` markdown
规则
1.方法的名称相同
2.参数列表不同
3.方法的返回值可以相同也可以不同
4.仅仅返回值不同不足以成为方法的重载


实现理论
方法名称相同，编译器会根据调用方法的参数的个数、参数的类型等去逐个匹配，以选择对应的方法，如果匹配失败，则编译器报错
```

## 命令行传参数

运行一个程序的时候再传递给它消息，这需传递命令行参数给main函数实现

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/9 23:17
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : Demo4.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package Method;

public class Demo4 {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }
}

```



![image-20210709232606771](Java.assets/image-20210709232606771.png)

## 可变参数

``` markdown
又名不定项参数

JDK1.5之后版本开始支持

在方法的声明中，在指定参数类型后面加一个省略号（...）

一个方法中只能指定一个可变参数，它必须是方法的最后一个参数。

任何普通参数必须在它之前声明
```



## 递归

递归头

递归体

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/9 23:38
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : Recursion.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package Method;

import java.util.Scanner;

public class Recursion {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n;
        n=scanner.nextInt();

        System.out.println(fun(n));

    }

    public static int fun(int n)
    {
        if (n==1){
            return 1;
        }
        else
        {
            return n*fun(n-1);
        }

    }
}

```



# 数组

## 数组创建

![image-20210710202406611](Java.assets/image-20210710202406611.png)

![image-20210710205715578](Java.assets/image-20210710205715578.png)

``` java
        两句完成
        int[] numbers; //数组的声明
        numbers=new int[10];// 创建一个数组

		一句完成
        int[] numbers=new int[10];//声明并创建
```

``` markdown
java 内存分析
1.堆
	存放new的对象和数组
	可以被所有的线程共享，不会存放别的对象引用
2.栈
	存放基本变量类型（会包含这个基本类型的具体数值）
	引用对象的变量（会存放这个引用在堆里面的具体地址）
3.方法区
	可以被所有的线程共享
	包含了所有的class和static变量
```

## 初始化

### 静态初始化

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/10 20:35
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : Demo02.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package ArrayDemo;

public class Demo02 {
    public static void main(String[] args) {
        // 静态初始化:创建+赋值
        int[] a = {1,2,3,4,5};

        int i;
        for (i=0;i<a.length;i++)
        {
            System.out.println(a[i]);
        }
    }
}

```



### 动态初始化

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/10 20:52
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : Demo03.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package ArrayDemo;

public class Demo03 {
    public static void main(String[] args) {
        // 动态初始化:声明+创建
        //动态初始化中包含了默认初始化

        int[] b= new int[10];
        int i;
        for (i=0;i<b.length;i++)
        {
            System.out.println(b[i]);
        }

    }
}

```



### 默认初始化

数组是引用类型，它的元素相当于类的实例变量，因此数组一经分配空间，其中的每个元素也被按照实例变量同样的方式被隐式初始化

``` java
```

特点

- 数组的长度是确定的，数组一旦被创建，其大小是不可以改变的

- 数组中的元素必须是相同的元素
- 数组中的元素可以是任何数组类型，包括基本类型和引用类型
- 数组变量属于引用类型，数组也可以看成是对象，数组中的每个元素相当于该对象的成员变量
  - 数组本身就是对象，Java中对象是在堆中的，因此数组无论保存原始类型还是其他对象类型，数组对象本身是在堆中的



数组的边界问题：0 ~ length-1

## 数组使用

For-Each循环

数组作方法入参

数组作返回值

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/10 21:34
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : Demo07.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package ArrayDemo;

public class Demo07 {
    public static void main(String[] args) {
        int[] array={1,2,3,4,5};

        int[] rev=reverse(array);
        for (int i = 0; i < rev.length; i++) {
            System.out.println(rev[i]);
        }
    }

    public static int[] reverse(int[] arr)
    {
        int[] re=new int[arr.length];
        for (int i = 0,j=arr.length-1; i < arr.length; i++,j--) {
            re[j]=arr[i];
        }
        return re;
    }
}

```



## 多维数组

``` java
/**
 * -*- coding : utf-8 -*-
 *
 * @Time : 2021/7/10 21:45
 * @Author : MurphyHou
 * @Proj_Name : JavaSE
 * @File_Name : Demo08.java
 * @Software : IntelliJ IDEA
 * =======Here We Go!=======
 */

package ArrayDemo;

public class Demo08 {
    public static void main(String[] args) {
        //int[][] arr=new int[2][5];

        int[][] arr={{1,2},{3,4},{5,6}};//三行，两列


        for (int i = 0; i < arr.length ; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.println(arr[i][j]);

            }
        }


    }
}

```

## Arrays类

![image-20210710215336621](Java.assets/image-20210710215336621.png)

## 冒泡排序



## 稀疏数组

# 面向对象
