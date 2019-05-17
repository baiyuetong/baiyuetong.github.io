---
title: pygame游戏开发- 简介
---



## pygame简介

pygame是跨平台python模块，专为电子游戏设计，包括图像、声音。建立在SDL基础上，允许实时电子游戏研发而无需被低级语言束缚， 开发者可以把精力放在游戏的架构上。
 
## pgame中主要模块介绍
(1)	pygame

pygame模块会自动导入其它的pygame相关模块。

pygame模块包括surface函数， 可以返回一个新的surface 对象。
init()函数是pygame游戏的核心，必须在进入游戏的主循环之前调用。init()会自动初始化其它所有模块。

(2)	pygame.locals

包括在你自己的模块作用域内使用的名字（变量）。包括事件类型、键和视频模式等的名字。

(3)	pygame.display

包括处理pygame显示方式的函数。包括普通窗口和全屏模式。
pygame.display中一些常用的方法如下：

flip：更新显示。

update：更新一部分时候使用update。

set_mode：设定显示的类型和尺寸。

set_caption：设定pygame程序的标题。

get_surface：调用flip和blit前返回一个可用于画图的surface对象。

(4)	pygame.font

包括font函数，用于表现不同的字体。

(5)	pygame.sprite

游戏精灵，Group用做sprite对象的容器。调用group对象的update对象，会自动调用所有sprite对象的update方法。

(6)	pygame.mouse

隐藏鼠标光标，获取鼠标位置。

(7)	pygame.event

追踪鼠标单击、按键按下和释放等事件。

(8)	pygame.image

用于处理保存在GIF、PNG或者JPEG文件内的图像。

<br>

## 安装

  使用pip install pygame命令安装pygame。安装后在python解释器界面导入安装好的pygame，检查版本。未报错，表示安装成功。

  \>>> import pygame

  \>>> print(pygame.ver)

  \>>> 1.9.3

<br>

## 游戏介绍

以上介绍了pygame的基本组成，下面已一个实际的游戏例子介绍pygame的用法及游戏步骤。

游戏是香蕉躲秤砣。秤砣从上方掉下来，玩家用鼠标控制屏幕下方的香蕉左右移动以躲避被秤砣砸中。

<br>

## 准备工作

(1)确认pygame已安装好。

(2)准备两张图片。一张是香蕉取名为banana.png，另一张是猴子取名为monkey.png。

<br>

## 创建游戏窗口

下面从简到难一步一步介绍游戏开发。首先创建一个游戏窗口，不做任何事情。

把下面的代码保存到monkey\_rob\_banana.py。monkey\_rob\_banana.py跟上面的两张图放在同一个目录下。

```py
monkey\_rob\_banana.py

01 import pygame

02 import sys

03

04 pygame.init()

05

06 screen\_size = 800, 600

07 screen = pygame.display.set\_mode(screen\_size)

08

09 while True:

10 　　for event in pygame.event.get():

11 　　　　if event.type == pygame.QUIT:

12 　　　　　　sys.exit()

13 　　pygame.display.flip()
```

第1行，导入pygame。

第4行，pygame初始化。

第7行，建立一个大小为800*600像素的屏幕。

第9行是一个无限循环。第10行到12行，判断是不是有QUIT事件(关闭游戏窗口)，如果有就退出整个游戏。第13行显示游戏窗口的内容。pygame.display.flip()把内容显示到屏幕上。

运行该代码就会出现一个游戏窗口了。现在屏幕背景是黑色的，把背景改为白色。增加一个变量bg\_color=(255, 255, 255)，然后调用screen.fill(bg\_color)填充背景色。整个代码如下：

```py
monkey\_rob\_banana.py

01 import pygame

02 import sys

03

04 pygame.init()

05

06 screen_size = 800, 600

07 **bg_color = (255, 255, 255)**

08 screen = pygame.display.set\_mode(screen\_size)

09

10 while True:

11 　　for event in pygame.event.get():

12 　　　　if event.type == pygame.QUIT:

13 　　　　　　sys.exit()

14 　　**screen.fill(bg\_color)**

15 　　pygame.display.flip()

``` 
运行以上代码，背景色为白色。

在pygame中颜色用RGB（红，绿，蓝）三原色的组合。其中（255，0， 0）表示红色；（0，255， 0）表示绿色；（0，0，255）表示蓝色（0，0，0）表示黑色；（255， 255， 255）表示白色。

<br>


## 事件处理	

  在pygame中，移动鼠标，按下或松开鼠标按钮，按下或松开键盘，改变窗口的大小，关闭窗口等动作都会产生事件。事件检测是游戏中一个重要的环节。你可以根据这些事件作相应的处理。譬如如果检测到鼠标移动事件，那么就让目标随鼠标一起移动。

  pygame通过一个事件队列来控制所有事件消息。来自系统的事件都有一个事件的类型和对应的成员属性,以下是每个事件类型以及对应的成员属性列表：

<table>
 <tr><th>事件类型</th><th>成员属性</th></tr>
 <tr><td>QUIT</td><td>None</td></tr>
 <tr><td>ACTIVEEVENT</td><td>gain,state</td></tr>
 <tr><td>KEYDOWN</td><td>uncode,key,mod</td></tr>
 <tr><td>KEYUP</td><td>key,mod</td></tr>
 <tr><td>MOUSEMOTION</td><td>pos,rel,button</td></tr>
 <tr><td>MOUSEBUTTONUP</td><td>pos,button</td></tr>
 <tr><td>JOYAXISMOTION</td><td>joy,axis,value</td></tr>
 <tr><td>JOYBALLMOTION</td><td>joy,ball,rel</td></tr>
 <tr><td>JOYHATMOTION</td><td>joy,hat,value</td></tr>
 <tr><td>JOYBUTTONUP</td><td>joy,button</td></tr>
 <tr><td>JOYBUTTONDOWN</td><td>joy,button</td></tr>
 <tr><td>VIDEORESIZE</td><td>size,w,h</td></tr>
 <tr><td>VIDEOEXPOSE</td><td>None</td></tr>
 <tr><td>USEREVENT</td><td>Code</td></tr>
</table>


函数pygame.event.get()从队列中获取事件。

为了对pygame事件有感性的认识，现把显示事件类型加到monkey\_rob\_banana.py中。在窗口中移动鼠标,按鼠标按钮或按键盘，看看输出。

```py
monkey\_rob\_banana.py

01 import pygame

02 import sys

03

04 pygame.init()

05

06 screen\_size = 800, 600

07 bg\_color = (255, 255, 255)

08 screen = pygame.display.set\_mode(screen\_size)

09

10 while True:

11 　　for event in pygame.event.get():

12 　　　　**print('event type: %d'%event.type)**

13 　　　　if event.type == pygame.QUIT:

14 　　　　　　sys.exit()

15 　　screen.fill(bg\_color)

16 　　pygame.display.flip()
```
 
## 掉香蕉动画
通过以上介绍，你对pygame有了一定的了解。下面开始制作猴子抢香蕉游戏的原型。第一步做一个简单的天上掉香蕉的动画。一个香蕉从屏幕顶部随意的一个位置匀速往屏幕下方掉落，掉落到底部后，另一个香蕉再从屏幕顶部随意的一个位置匀速往屏幕下方掉落，重复这一过程。

```py
monkey\_rob\_banana.py

01 # coding=utf-8

02 import pygame

03 import sys

04 from random import randrange

05

06 class Banana(pygame.sprite.Sprite):

07 　　def \__init\__(self):

08 　　　　pygame.sprite.Sprite.\__init\__(self)

09 　　　　# 在绘制sprite时使用的图像和矩形

10 　　　　self.image = banana\_image

11 　　　　self.rect = self.image.get\_rect()

12 　　　　self.reset()

13

14 　　def reset(self):

15 　　　　"""

16 　　　　将香蕉放到屏幕顶端(视线外)的随机位置

17 　　　　"""

18 　　　　self.rect.top = -self.rect.height

19 　　　　self.rect.centerx = randrange(screen\_size[0])

20

21 　　def update(self):

22 　　　　"""

23 　　　　更新香蕉, 显示下一帧

24 　　　　"""

25 　　　　self.rect.top += 1

26 　　　　if self.rect.top > screen\_size[1]:

27 　　　　　　self.reset()

28

29 # 初始化

30 pygame.init()

31 screen_size = 800, 600

32 pygame.display.set_mode(screen\_size)

33 pygame.mouse.set\_visible(0)

34

35 # 载入香蕉图像

36 banana_image = pygame.image.load('banana.png')

37 

38

39 # 创建一个子图组(sprite group), 增加Banana

40 sprites = pygame.sprite.RenderUpdates()

41 sprites.add(Banana())

42

43 # 获取屏幕并填充

44 screen = pygame.display.get\_surface()

45 bg = (255, 255, 255)

46 screen.fill(bg)

47 pygame.display.flip() # 全屏更新

48

49 # 用于清除子图形

50 def clear_callback(surf, rect):

51 　　surf.fill(bg, rect)

52

53 while True:

54 　　# 检查退出事件

55 　　for event in pygame.event.get():

56 　　　　if event.type == pygame.QUIT:

57 　　　　　　sys.exit()

58 　　　　elif event.type == pygame.KEYDOWN and \

59 　　　　　　event.key == pygame.K\_ESCAPE:

60 　　　　　　sys.exit()

61 　　# 清除前面的位子图形

62 　　sprites.clear(screen, clear\_callback)

63 　　# 更新所有子图形

64 　　sprites.update()

65 　　# 绘制所有子图形

66 　　updates = sprites.draw(screen)

67 　　# 更新所需的显示部分

68 　　pygame.display.update(updates)
```

实现香蕉从天而降的代码流程如下：

(1)	使用pygame.init、pygame.display.set_mode和pygame.mouse.set_visible方法初始化代码主框架。使用pygame.display.get_surface获取屏幕表面。使用白色填充屏幕（利用fill方法），然后调用pygame.diaplay.flip显示修改后的屏幕。

(2)	载入香蕉图像。

(3)	创建自定义的Banana类（Sprite类的子类）的实例。当对象添加到名为sprites（名字随便定义）对象的RenderUpdates组中。

(4)	使用pygame.event.get获取事件，并以此对事件检查。如果发现有QUIT事件， 或发现有按了Esc键（K\_ESCAPE）而触发的KEYDOWN事件，那么就推出程序。

(5)	调用sprites组的clear和update方法。Clear使用回调来清除所有的sprite对象（本例是Banana），update方法调用Banana实例的update方法。

(6)	用屏幕表面作为参数调用sprites.draw方法，在当前位置绘制Sprite类对象Weight（Banana的位置在每次调用update时改动)。

(7)	使用从sprites.draw返回的矩形作为参数调用pygame.display.update, 只在需要的位置更新。也可以使用pygame.display.flip更新整个显示区域，只是效率要比pygame.display.update要低得多。

(8)	重复（4）到（7）步。

运行monkey\_rob\_banana.py可以看到有香蕉从屏幕顶部下落。

<br>

## 配置文件

在程序中会用到一些配置参数， 如屏幕尺寸、背景色、图像文件名称等。可以把这些配置变量收集到一个文件中(config.py)，从而跟程序隔离出来，这也对项目的维护和使用带来极大的方便，如想换一个香蕉图形、改变屏幕大小，就只要修改配置文件而不要改动原代码。

把以下config.py跟monkey\_rob\_banana.py放在同一个目录。

```py
config.py

01 # coding=utf-8

02 #　monkey\_rob\_banana的配置文件

03 

04 # 改变这些变量,以便在游戏中使用其它图像

05 banana_image = 'banana.png'

06

07 # 改变这些变量以影响一般的外观

08 screen_size = 800, 600

09 background\_color = 255, 255, 255
 
monkey\_rob\_banana.py只要直接使用config.py中定义的配置参数。

monkey\_ro\b_banana.py

01 # coding=utf-8

02 import pygame

03 import sys

04 from random import randrange

05 import config

06 class Banana(pygame.sprite.Sprite):

07 　　def \__init\__(self):

08 　　　　pygame.sprite.Sprite.\__init\__(self)

09 　　　　# 在绘制sprite时使用的图像和矩形

10 　　　　self.image = weight\_image

11 　　　　self.rect = self.image.ge\t_rect()

12 　　　　self.reset()

13

14 　　def reset(self):

15 　　　　"""

16 　　　　将香蕉放到屏幕顶端(视线外)的随机位置

17 　　　　"""

18 　　　　self.rect.top = -self.rect.height

19 　　　　self.rect.centerx = randrange(screen\_size[0])

20

21 　　def update(self):

22 　　　　"""

23 　　　　更新香蕉, 显示下一帧

24 　　　　"""

25 　　　　self.rect.top += 1

26 　　　　if self.rect.top > screen\_size[1]:

27 　　　　　　self.reset()

28

29 # 初始化

30 pygame.init()

31 **screen_size = config.screen_size**

32 pygame.display.set_mode(screen_size)

33 pygame.mouse.set\_visible(0) #隐藏光标

34

35 # 载入香蕉图像

36 **banana_image = pygame.image.load(config.banana_image)**

37 

38

39 # 创建一个子图组(sprite group), 增加Banana

40 sprites = pygame.sprite.RenderUpdates()

41 sprites.add(Banana())

42

43 # 获取屏幕并填充

44 screen = pygame.display.get\_surface()

45 **bg = config.background_color**

46 screen.fill(bg)

47 pygame.display.flip() # 全屏更新

48

49 # 用于清除子图形

50 def clear\_callback(surf, rect):

51 　　surf.fill(bg, rect)

52

53 while True:

54 　　# 检查退出事件

55 　　for event in pygame.event.get():

56 　　　　if event.type == pygame.QUIT:

57 　　　　　　sys.exit()

58 　　　　elif event.type == pygame.KEYDOWN and \

59 　　　　　　event.key == pygame.K\_ESCAPE:

60 　　　　　　sys.exit()

61 　　# 清除前面的子图形

62 　　sprites.clear(screen, clear\_callback)

63 　　# 更新所有子图形

64 　　sprites.update()

65 　　# 绘制所有子图形

66 　　updates = sprites.draw(screen)

67 　　# 更新所需的显示部分

68 　　pygame.display.update(updates)
```

 
<br>

## 重构--建立Banana.py

主控程序monkey\_rob\_banana.py显得太凌乱.现在把Banana剥离出来生成banana.py，这样可以使得主控程序monkey\_rob\_banana.py功能单一.

```py
banana.py

01 # coding=utf-8

02 import pygame

03 from random import randrange

04

05 class Banana(pygame.sprite.Sprite):

06 　　def \__ini\t__(self, **image, config**):

07 　　　　pygame.sprite.Sprite.\__init\__(self)

08 　　　　# 在绘制sprite时使用的图像和矩形

09 　　　　self.image = image

10 　　　　# 屏幕尺寸

11 　　　　self.screen_size = config.screen\_size

12 　　　　self.rect = self.image.get\_rect()

13 　　　　self.reset()

14

15 　　def reset(self):

16 　　　　"""

17 　　　　将香蕉放到屏幕顶端的随机位置

18 　　　　"""

19 　　　　self.rect.top = -self.rect.height

20 　　　　self.rect.centerx = randrange(screen\_size[0])

21

22 　　def update(self):

23 　　　　"""

24 　　　　更新香蕉, 显示下一帧

25 　　　　"""

26 　　　　self.rect.top += 1

27 　　　　if self.rect.top > screen\_size[1]:

28 　　　　　　self.reset()

29
```

代码基本上是从原来的monkey\_rob\_banana.py拷过来的。生成实例的时候要把香蕉图像和配置对象带进来，在reset和update时使用。 banana剥离后，在money\_rob\_banana.py中需要导入banana.

```py
monkey_rob_banana.py:
 
01 # coding=utf-8

02 import pygame

03 import sys

04 from banana import Banana

05 import config

06 # 初始化

07 pygame.init()

08 screen\_size = config.screen\_size

09 pygame.display.set_mode(screen\_size)

10 pygame.mouse.set\_visible(0)

11

12 # 载入香蕉图像

13 banana\_image = pygame.image.load(config.banana\_image)

14

15

16 # 创建一个子图组(sprite group), 增加Banana

17 sprites = pygame.sprite.RenderUpdates()

18 sprites.add(Weight(**banana\_image, config**))

19

20 # 获取屏幕并填充

21 screen = pygame.display.get\_surface()

22 bg = config.background\_color

23 screen.fill(bg)

24 pygame.display.flip() # 全屏更新

25

26 # 用于清除子图形

27 def clear\_callback(surf, rect):

28 　　surf.fill(bg, rect)

29

30 while True:

31 　　# 检查退出事件

32 　　for event in pygame.event.get():

33 　　　　if event.type == pygame.QUIT:

34 　　　　　　sys.exit()

35 　　　　elif event.type == pygame.KEYDOWN and \

36 　　　　　　event.key == pygame.K\_ESCAPE:

37 　　　　　　sys.exit()

38 　　# 清除前面的位子图形

39 　　sprites.clear(screen, clear\_callback)

40 　　# 更新所有子图形

41 　　sprites.update()

42 　　# 绘制所有子图形

43 　　updates = sprites.draw(screen)

44 　　# 更新所需的显示部分

45 　　pygame.display.update(updates)
```
 
monkey\_rob\_banana.py首先要导入banana，然后在建立Banana的时候要带入香蕉图像和配置参数。

<br>

## 建立猴子类

主控程序monkey\_rob\_banana.py和香蕉类程序banana.py都建立好了，现在建立猴子类程序monkey.py，这样就可以有一个完整的猴子抢香蕉游戏了。

```py
monkey.py
 
01 # coding=utf-8

02 import pygame

03

04 class Monkey(pygame.sprite.Sprite):

05 　　"""

06 　　准备抢香蕉的猴子。它使用SquishSprite构造函数设置猴子的图像，

07 　　并且会停留在屏幕底端。它的水平位置由当前的鼠标位置决定.

08 　　"""

09 　　

10 　　def \__init\__(self, image, config):

11 　　　　pygame.sprite.Sprite.\__init\__(self)

12 　　　　self.image = image

13 　　　　self.rect = self.image.get\_rect()

14 　　　　self.rect.top = config.screen\_size[1] - self.rect.height

15 　　　　self.rect.centerx = config.screen\_size[0] / 2

16 　　　　

17

18 　　def update(self):

19 　　　　"""

20 　　　　将Banana中心点的横坐标设定为当前鼠标指针的横坐标，

21 　　　　并且使用rec的clamp方法确保Banana停留在所允许的范围内。

22 　　　　"""

23 　　　　self.rect.centerx = pygame.mouse.get\_pos()[0]

24

25 　　def touches(self, other):

26 　　　　"""

27 　　　　使用rec的colliderect方法确定香蕉是否触碰到了另外的子图形（比如香蕉）。

28 　　　　"""

29 　　　　bounds = self.rect

30 　　　　# 检查边界是否和其他对象的rect交叉。

31 　　　　return bounds.colliderect(other.rect) 
```

  初始化的时候设定光标和香蕉的位置在屏幕底部中间。游戏的时候鼠标控制香蕉左右移动躲避秤砣。函数touches()检测香蕉和另外的物体是不是有交叉，有交叉就说明两个物体发生了碰撞。

  把banana导入到monkey\_rob\_banana.py，如果检测到猴子接着了香蕉，则作相应的处理。

```py
monkey\_rob\_banana.py

01 # coding=utf-8

02 import pygame

03 import sys

04 from weight import Weight

05 from banana import Banana

06 import config

07 # 初始化

07 pygame.init()

08 screen\_size = config.screen\_size

09 pygame.display.set_mode(screen\_size)

10 pygame.mouse.set\_visible(0)

11

12 # 载入香蕉图像

13

14 banana\_image = pygame.image.load(config.banana\_image)

15 

16 # 载入猴子图像

17 monkey\_image = pygame.load(config.monkey\_image))

18 

19

20 # 创建一个子图组(sprite group), 增加banana和monkey

21 banana = Banana(banana\_image, comfig)

22 monkey = Monkey(monkey\_image, config)

22 sprites = pygame.sprite.RenderUpdates()

23 sprites.add(monkey)

24 sprites.add(banana)

25 

26

27 # 获取屏幕并填充

28 screen = pygame.display.get\_surface()

29 bg = config.background\_color

30 screen.fill(bg)

31 pygame.display.flip() # 全屏更新

32

33 # 用于清除子图形

34 def clear_callback(surf, rect):

35 　　surf.fill(bg, rect)

36

37 count = 1

38 while True:

39 　　# 检查退出事件

40 　　for event in pygame.event.get():

41 　　　　if event.type == pygame.QUIT:

42 　　　　　　sys.exit()

43 　　　　elif event.type == pygame.KEYDOWN and \

44 　　　　　　event.key == pygame.K\_ESCAPE:

45 　　　　　　sys.exit()

46 　　# 清除前面的子图形

47 　　sprites.clear(screen, clear\_callback)

48 　　# 更新所有子图形

49 　　sprites.update()

50 　　# 绘制所有子图形

51 　　updates = sprites.draw(screen)

52 　　# 更新所需的显示部分

53 　　# pygame.display.update(updates)

54 　　# 更新整个屏幕

55 　　pygame.display.flip()

56 　　**if banana.touches(weight)**:

57 　　　　print('touch:%d'%count)

58 　　　　count += 1

59 　　　　# 创建一个子图组(sprite group),

60 　　　　# 增加猴子和香蕉到sprite group

61 　　　　sprites.remove(weight)

62 　　　　sprites.remove(banana)

63 　　　　banana = Banana(banana\_image, config)

64 　　　　monkey = Monkey(monkey\_image, config)

65 　　　　sprites = pygame.sprite.RenderUpdates()

66 　　　　sprites.add(monkey)

67 　　　　sprites.add(banana)

68 　　　　screen.fill(bg)

69 　　　　pygame.display.flip()

70
```

跟香蕉相似，把猴子实例加进来。在无限循环中使用monkey.touches(banana)判断猴子跟香蕉是不是发生了碰撞，如果发生碰撞，则输出碰撞次数，并重新初始化猴子和香蕉实例。在本例中把pygame.display.update(updates)换成了pygame.display.flip()，降低了性能，要不然秤砣下降太快。

运行monkey\_rob\_banana.py就可以用鼠标的移动控制猴子抓香蕉了。

## 窗口标题
代码没有对窗口加标题,所以使用的是默认标题"pygame window"。现在给它起一个合适的标题叫"猴子抢香蕉"。步骤如下：

在config.py中增加screen\_caption = u'猴子抓香蕉'。在monkey\_rob\_banana.py增加pygame.display.set\_caption(config.screen\_caption)。

整个游戏完整代码如下：

```py
config.py

# coding=utf-8
#Squish的配置文件

# 改变这些变量,以便在游戏中使用其它图像
banana_image = 'banana.png'
monkey_image = 'monkey.png'

# 改变这些变量以影响一般的外观
screen_size = 800, 600
background_color = 255, 255, 255
screen_caption = u'猴子抢香蕉'
drop_speed = 1</code>





monkey\_rob\_banana.py

# coding=utf-8
import pygame
import sys
from banana import Banana
from monkey import Monkey
import config

# 初始化
pygame.init()
screen_size = 800, 600
pygame.display.set_mode(screen_size)
pygame.display.set_caption(config.screen_caption)


# 创建一个子图组(sprite group), 增加Banana和Monkey
sprites = pygame.sprite.RenderUpdates()
banana_drop_speed = config.drop_speed
sprites.add([Banana(config, banana_drop_speed), Monkey(config)])

# 获取屏幕并填充
screen = pygame.display.get_surface()
bg = config.background_color
screen.fill(bg)
pygame.display.flip() # 全屏更新

# 用于清除子图形
def clear_callback(surf, rect):
   surf.fill(bg, rect)

while True:
    # 检查退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()
    # 清除当前的位置
    sprites.clear(screen, clear_callback)
    # 更新所有子图形
    sprites.update()
    # 绘制所有子图形
    updates = sprites.draw(screen)
    # 更新所需的显示部分
    pygame.display.update(updates)





banana.py

# coding=utf-8
import pygame
from random import randrange

class Banana(pygame.sprite.Sprite):
    def __init__(self, config, speed):
        pygame.sprite.Sprite.__init__(self)
        self.config = config
        # 在绘制sprite时使用的图像和矩形
        self.image = pygame.image.load(self.config.banana_image)
        # 屏幕大小
        self.screen_size = self.config.screen_size
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        """
        将香蕉放到屏幕顶端(视线外)、水平方向随机的位置
        """
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(self.screen_size[0])

    def update(self):
        """
        更新香蕉, 显示下一帧
        """
        self.rect.top += 1
        if self.rect.top > self.screen_size[1]:
            self.reset()


monkey.py

# coding=utf-8
import pygame

class Monkey(pygame.sprite.Sprite):
    """
    准备抢香蕉的猴子。它使用SquishSprite构造函数设置猴子的图像，
    并且会停留在屏幕底端。它的水平位置由当前的鼠标位置决定.
    """
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.monkey_image)
        self.rect = self.image.get_rect()
        self.rect.top = config.screen_size[1] - self.rect.height
        self.rect.centerx = config.screen_size[0] / 2
        pygame.mouse.set_pos([self.rect.centerx, self.rect.top])

    def update(self):
        """
        将猴子中心点的横坐标设定为当前鼠标指针的横坐标。
        """
        self.rect.centerx = pygame.mouse.get_pos()[0]

    def touches(self, other):
        """
        使用rec的colliderect方法确定香蕉是否触碰到了另外的
        子图形（比如香蕉）。
        """
        bounds = self.rect
        # 检查边界是否和其他对象的rect交叉。
        return bounds.colliderect(other.rect)</code>


```

运行monkey\_rob\_banana.py，可以看到窗口标题是猴子抢香蕉。

<br>

## 进一步完善

现在已经学会了pygame的基本用法和写游戏程序的方法。程序基本完成了猴子抓香蕉的游戏原型，香蕉从窗口顶部的随意位子下降, 玩家用鼠标控制猴子抓下落的香蕉。但还有许多地方需要改进，例如现在游戏没有结束功能、没有进级和计分等，这些都需要改进。


{% include sharepost.html %}