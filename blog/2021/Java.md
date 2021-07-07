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
  - 
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

  - ``` java
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

  ``` java
  /**
   * -*- coding : utf-8 -*-
   * Time       : 2021/7/7 23:49
   * Author     : MurphyHou
   * Proj_Name  : JavaSE
   * File_Name  : Hello.java
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

  - 类名，变量名，方法名

    | **关键字**   | **含义**                                                     |
    | ------------ | ------------------------------------------------------------ |
    | abstract     | 表明类或者成员方法具有抽象属性                               |
    | assert       | 断言，用来进行程序调试                                       |
    | boolean      | 基本数据类型之一，声明布尔类型的关键字                       |
    | break        | 提前跳出一个块                                               |
    | byte         | 基本数据类型之一，字节类型                                   |
    | case         | 用在switch语句之中，表示其中的一个分支                       |
    | catch        | 用在异常处理中，用来捕捉异常                                 |
    | char         | 基本数据类型之一，字符类型                                   |
    | class        | 声明一个类                                                   |
    | const        | 保留关键字，没有具体含义                                     |
    | continue     | 回到一个块的开始处                                           |
    | default      | 默认，例如，用在switch语句中，表明一个默认的分支。Java8 中也作用于声明接口函数的默认实现 |
    | do           | 用在do-while循环结构中                                       |
    | double       | 基本数据类型之一，双精度浮点数类型                           |
    | else         | 用在条件语句中，表明当条件不成立时的分支                     |
    | enum         | 枚举                                                         |
    | extends      | 表明一个类型是另一个类型的子类型。对于类，可以是另一个类或者抽象类；对于接口，可以是另一个接口 |
    | final        | 用来说明最终属性，表明一个类不能派生出子类，或者成员方法不能被覆盖，或者成员域的值不能被改变，用来定义常量 |
    | finally      | 用于处理异常情况，用来声明一个基本肯定会被执行到的语句块     |
    | float        | 基本数据类型之一，单精度浮点数类型                           |
    | for          | 一种循环结构的引导词                                         |
    | goto         | 保留关键字，没有具体含义                                     |
    | if           | 条件语句的引导词                                             |
    | implements   | 表明一个类实现了给定的接口                                   |
    | import       | 表明要访问指定的类或包                                       |
    | instanceof   | 用来测试一个对象是否是指定类型的实例对象                     |
    | int          | 基本数据类型之一，整数类型                                   |
    | interface    | 接口                                                         |
    | long         | 基本数据类型之一，长整数类型                                 |
    | native       | 用来声明一个方法是由与计算机相关的语言（如C/C++/FORTRAN语言）实现的 |
    | new          | 用来创建新实例对象                                           |
    | package      | 包                                                           |
    | private      | 一种访问控制方式：私用模式                                   |
    | protected    | 一种访问控制方式：保护模式                                   |
    | public       | 一种访问控制方式：共用模式                                   |
    | return       | 从成员方法中返回数据                                         |
    | short        | 基本数据类型之一,短整数类型                                  |
    | static       | 表明具有静态属性                                             |
    | strictfp     | 用来声明FP_strict（单精度或双精度浮点数）表达式遵循[IEEE 754](https://baike.baidu.com/item/IEEE 754)算术规范 |
    | super        | 表明当前对象的父类型的引用或者父类型的构造方法               |
    | switch       | 分支语句结构的引导词                                         |
    | synchronized | 表明一段代码需要同步执行                                     |
    | this         | 指向当前实例对象的引用                                       |
    | throw        | 抛出一个异常                                                 |
    | throws       | 声明在当前定义的成员方法中所有需要抛出的异常                 |
    | transient    | 声明不用序列化的成员域                                       |
    | try          | 尝试一个可能抛出异常的程序块                                 |
    | void         | 声明当前成员方法没有返回值                                   |
    | volatile     | 表明两个或者多个变量必须同步地发生变化                       |
    | while        | 用在循环结构中                                               |

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
  - 

## 类型转换

## 变量 常量

## 运算符

## 包机制、JavaDoc

