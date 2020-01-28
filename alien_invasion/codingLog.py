"""
2020年1月28日
1. python 文件有改动且未保存，文件名在VSCODE 标签上显示斜体字

2020年1月22日

1. 
File "d:\Python\alien_invasion\ship.py", line 11, in __init__
    self.image = pygame.image.load('images/ship.bmp')
pygame.error: Couldn't open images/ship.bmp
= 将路径中写成 反斜杠，无效
= self.image = pygame.image.load(r'images/ship.bmp') ,无效
= 修改路径有效：(alien_invasion\images\ship.bmp)

原因如下：工作的主文件是python, 而图片路径是('image\ship.bmp'),
系统直接在主文件Python下面找图片，结果肯定找不到，补充完整路径：
'alien_invasion\images\ship.bmp'

这个答案是在英文网站上看到的，第一次看的不是很明白，按照提示修改之后，
反复查看，才搞懂了。

Use print os.getwd() as the first line of your script/py program 
to see which folder you are actually starting from. If your image 
happens to be in a sub-directory of the main folder (which happens
not to appear on the output of os.getwd()), make sure to include 
it in your image path such that instead of writing only 'ship.bmp'
when loading the image, you write 'subdirectory/ship.bmp' as your
path.
（https://stackoverflow.com/）

2. os 模块的使用
    1. 引入模块：import os
    2. 获取当前工作目录，并打印：print(os.getcwd())
    3. 注意打印语法： 打印内容，加括号
    4. 任何一个script.py都可以，比如ship.py

3. 报错：TypeError: '>=' not supported between instances of 'int' and 'pygame.Rect'
= 拼写错误；

2020年1月23日
    13 章，外星人代码设置

2020年1月24日

1. rect, 首字母大写
self.rect = pygame.Rect(0, 0, self.width, self.height)

pygame中Rect(left, top, width, height)

2. 没有报错，但是屏幕是黑色的
= update_screen 少了参数：stats
= 无法判断问题在哪里，猜测不到；可能是个很基础的问题，因为之前的元素也无法显示了
= 和书本核对了两遍，没找到问题；重点核对了主框架，没发现问题
    先放过，下次再检查

2020年1月25日

1. (延续昨天的问题)= ailen_invasion.py
主循环中，如果不添加“if stats.game_active:”，则可以显示飞船，但是PLAY按钮直接出现了，
也就是按钮判断生效导致了问题。

= 将update_screen 移出if 判断之后，可以正常显示PLAY

原因：update_screen 函数放在了 if stats.game_active 之中；正确的写法是不放入，
因为在游戏没有激活的时候，也是需要update_screen 的。

2. 如何确定函数的参数？
    根据函数内部，参数出现的顺序，依次排列参数
    即使是嵌套函数的参数，也要写入函数中

3. 多动手写写“动手试一试”，可以帮助理解代码；一味的抄写代码，难免陷入无聊的境地

2020年1月26日

1. intersect:  相交; 交叉; 横穿; 贯穿; 横断;

2. pygame.sprite.groupcollide() 返回值会有这3种。
    1. 精灵组无碰撞发生则返回空字典（{}的布尔值是Flase）
    2. 发生碰撞则返回字典，其中子弹为键，外星人为值。每当检测到碰撞发生都会返回一个这样的字典。
    3. 如果一个子弹击中多个，则包含多个外星人（值）
查看文档吧：groupcollide(group1, group2, dokill1, dokill2, collided = None) -> Sprite_dict
If either dokill argument is True, the colliding Sprites will be removed from
 their respective Group

举例：
1 {}; 没有击中
2 {<Bullet sprite(in 0 groups)>: [<Alien sprite(in 0 groups)>]}；击中一个
3 {<Bullet sprite(in 0 groups)>: [<Alien sprite(in 0 groups)>, 
<Alien sprite(in 0 groups)>, <Alien sprite(in 0 groups)>, 
<Alien sprite(in 0 groups)>, <Alien sprite(in 0 groups)>, 
<Alien sprite(in 0 groups)>]}；一个子弹击中了多个
注意格式：键-值，键用的是<>, 值，用的是[]，可以存放多个值；


pygame documentation: http://www.pygame.org/docs/ref/sprite.html

不懂的模块，可以找官方文档查看；或者打印模块的返回值；

3.函数round()， 圆整
通常让小数精确到小数点后多少位，其中小数位数是由第二个实参指定的。然
而，如果将第二个实参指定为负数，round()将圆整到最近的10、100、1000等整数倍。

4. ship 耗尽之后，界面依然会显示遗留的外星人、子弹，是否正常？

5. 为啥突然游戏速度变慢了，为啥？
= 改天重新启动程序，没有这个问题了。

2020年1月28日
1. 添加了显示等级模块
2. 目前代码已经写到一定程度，停一停，好好理解一下已经完成的代码
    理解好了之后，再继续写。



"""