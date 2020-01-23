"""
2020年1月22日

1. 
File "d:\Python\alien_invasion\ship.py", line 11, in __init__
    self.image = pygame.image.load('images/ship.bmp')
pygame.error: Couldn't open images/ship.bmp
= 将路径中写成 反斜杠，无效
= self.image = pygame.image.load(r'images/ship.bmp') ,无效
= 修改路径有效：(alien_invasion\images\ship.bmp)

原因如下：工作的主文件是python, 而图片路径是('image\ship.bmp'),
系统直接在主文件Python下面找图片路径，结果肯定找不到，补充完整：
'alien_invasion\images\ship.bmp',搞定
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

3. 报错：TypeError: '>=' not supported between instances of 'int' and 'pygame.Rect'
= 拼写错误；

2020年1月23日
    13 章，外星人代码设置


"""