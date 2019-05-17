---
title: pygame游戏开发- 提高
---

## 改进

现在写一个比较完整的猴子抢香蕉游戏。游戏的流程是：

1。显示游戏开发信息画面（如游戏版本号等）。

2。显示游戏使用方法画面。

3。开始游戏。每一级有一定数量的香蕉下落，猴子抢到规定数量的香蕉后就进到下一级。如果一级中所有香蕉都落下了单猴子没有抢到规定的数量，那么就结束。猴子每抢到一根香蕉就得到一定的分数。

4。在游戏的过程中会把当前是第几关，本关还剩几根香蕉和当前的得分情况显示在屏幕上。

5。如果进到规定的级别，就结束整个游戏。

把上面的游戏流程用状态来表示，就可以看出，游戏实际就是一个状态的转换过程。每个状态要知道你的下一个状态是什么，这样在主控程序中就可以从初始的状态开始，控制状态流程，直到游戏的结束状态。

整个程序还是有config.py、banana.py、monkey.py、monkey\_rob\_banana.py和一些图形文件组成。
下面对程序做一个简单的介绍。

```py
config.py
# coding=utf-8

# monkey_rob_banana的配置文件

# 改变这些变量,以便在游戏中使用其它图像
banana_image = 'banana.png'
monkey_image = 'monkey.png'
splash_image = 'splash.png'
info_image = 'info.png'
level_image = 'level.png'
gameover_image = 'gameover.png'
victory_image = 'victory.png'

# 改变这些变量以影响一般的外观
screen_size = 800, 600
background_color = 255, 255, 255
screen_caption = u'猴子抢香蕉'
full_screen = False

# 改变这些设置会影响游戏的行为
drop_speed = 1
speed_increase = 0.2
bananas_per_level = 10
robbed_bananas_per_level = 2
levels_limit = 3
font_size = 48
```


一些主要配置参数：

banana_image香蕉图形文件。

monkey_image猴子图形文件。

splash_image游戏开始画面，显示游戏版本，名称等。

info_image游戏介绍和使用方法的图形文件。

level_image进入到第几级的画面文件。

gameover_image在某一级猴子没有抢到规定的香蕉，结束画面图形文件。

victory_image所有的级别都完成后的图形文件。

drop_speed 香蕉下落的速度

speed_increase 每进一级，速度增量

banana_per_level 每一级可供下落的香蕉数

robbed_bananas_per_level 猴子可以进到下一级必须要抢到的香蕉数

levels_limit 做高能进级的级别，到了这个级别，游戏就结束。


```py
banana.py
# coding=utf-8
import pygame
from random import randrange

class Banana(pygame.sprite.Sprite):
    """
    从天而降的香蕉， 以给定的速度匀速下降。
    """
    def __init__(self, config, speed):
        pygame.sprite.Sprite.__init__(self)
        self.config = config
        self.speed = int(speed)
        # 在绘制香蕉时使用的图像和矩形
        self.image = pygame.image.load(self.config.banana_image)
        self.rect = self.image.get_rect()
        # 屏幕大小
        self.screen_size = self.config.screen_size
        self.reset()

    def reset(self):
        """
        将香蕉放到屏幕顶端(视线外)、水平方向随机的位置
        """
        self.rect.top = -self.rect.height
        self.rect.centerx = randrange(self.screen_size[0])
        # 控制香蕉在屏幕里面
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_size[1]:
            self.rect.right = self.screen_size[1]
        self.landed = False

    def update(self):
        """
        根据它的速度将香蕉垂直移动（下落）一段距离。并且根据它是否触及屏幕底端来设置landed属性。
        """
        self.rect.top += self.speed
        self.landed = self.rect.top >= self.screen_size[1]
```


banana.py跟初级部分介绍的差不多，只是增加了速度控制，游戏级别越高速度就越快。

```py
monkey.py
# coding=utf-8
import pygame

class Monkey(pygame.sprite.Sprite):
    """
    准备抢香蕉的猴子。它停留在屏幕底端。它的水平位置由当前的鼠标位置决定.
    """
    def __init__(self, config):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.monkey_image)
        self.rect = self.image.get_rect()
        self.rect.top = config.screen_size[1] - self.rect.height
        self.rect.centerx = config.screen_size[0] / 2
        self.robbed_bananas = 0
        self.robbed_bananas_per_level = config.robbed_bananas_per_level

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
        return bounds.colliderect(other.rect)
```

monkey.py跟初级部分介绍的一样，没有改动。

<br>

```py
monkey\_rob\_banana.py
# coding=utf-8
import sys, pygame
from pygame.locals import *
from banana import Banana
from monkey import Monkey
import config

# 这个模块包括monkey_rob_banana游戏的主要游戏逻辑。

# 全局变量， 总得分
total_score = 0.0

class State:
    """
    游戏状态类，可以处理事件并在给定的表面上显示自身。
    """

    def handle(self, event):
        """
        退出事件作为默认事件处理。
        """
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit()

    def firstDisplay(self, screen):
        """
        用于第一次显示状态。使用背景色填充屏幕。
        """
        screen.fill(config.background_color)
        pygame.display.flip()

    def display(self, screen):
        """
        用于在已经显示过一次状态后再次显示。默认的行为是什么都不做。
        """
        pass
    """
    def get_score(self):
        return total_score

    def set_score(self, score):
        total_score = score
    """
class Level(State):
    """
    游戏等级。用于计算已经落下了多少香蕉，移动子图形以及其他和游戏逻辑相关的任务。
    """
    def __init__(self, number=1):
        self.number = number
        # 本关可供落下香蕉个数
        self.remaining = config.bananas_per_level

        self.speed = config.drop_speed
        self.speed += (self.number - 1.0) * config.speed_increase
        # 创建香蕉和猴子：
        self.banana = Banana(config, self.speed)
        self.monkey = Monkey(config)
        both = self.banana, self.monkey
        self.sprites = pygame.sprite.RenderUpdates(both)

        self.score = 0
        self.number = number
        self.levels_limit = config.levels_limit

    def update(self, game):
        """
        更新游戏状态
        """
        global total_score
        # 更新所有子图形：
        self.sprites.update()
        # 如果猴子抓到了一定数量的香蕉, 则让游戏切换到LevelCleared 状态
        if self.monkey.touches(self.banana):
            self.monkey.robbed_bananas += 1
            self.banana.reset()
            self.score += self.speed*100.0
            if self.monkey.robbed_bananas >= self.monkey.robbed_bananas_per_level:
                if self.number + 1 >= self.levels_limit:
                    total_score += self.score
                    # super.set_score(total_core)
                    game.nextState = Victory(total_score)
                else:
                    game.nextState = LevelCleared(self.number)
        # 否则在香蕉落地时将其复位。
        # 如果在本关内所有香蕉都落完了,告诉游戏切换到GameOver状态
        elif self.banana.landed:
            self.banana.reset()
            self.remaining -= 1
            if self.remaining == 0:
                game.nextState = GameOver(total_score)
                self.score = 0.0

    def display_score(self, screen):
        antialias = 1
        black = 0, 0, 0
        line = '%d  %d  %d'%(self.number, self.remaining, int(self.score))
        # 生成所有行，从计算过的top开始，并且对于每一行向下移动font.get_linesize()像素
        font = pygame.font.Font(None, config.font_size)
        text = font.render(line, antialias, black)
        r = text.get_rect()
        screen.blit(text, r)

    def display(self, screen):
        """
        在第一次显示（只清空屏幕）后显示状态。与firstDisplay不同，这个方法使用pygame.display.update对
        self.sprites.draw提供的、需要更新的矩形列表进行更新。
        """
        screen.fill(config.background_color)
        self.display_score(screen)
        updates = self.sprites.draw(screen)
        pygame.display.flip()

class Paused(State):
    """
    简单的暂停游戏状态，按下键盘上任意键或者点击鼠标都会结束这个状态。
    """
    finished = 0  # 用户结束暂停了吗？
    image = None  # 如果需要图片的话，将这个变量设置为文件名
    text = ''  # 将它设定为一些提示性文本

    def handle(self, event):
        """
        通过对State进行委托（一般处理退出事件）以及对按键和鼠标点击作为反应来处理事件。
        如果键被按下或者鼠标被点击，将self.finished设定为真。
        """
        State.handle(self, event)
        if event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
            self.finished = 1

    def update(self, game):
        """
        更新等级。如果按键被按下或者鼠标被点击（比如self.finished为真），那么告诉我们切换到下一个
        由self.nextState()表示的状态（应该由子类实现）
        """
        if self.finished:
            game.nextState = self.nextState()

    def firstDisplay(self, screen):
        """
        暂停状态第一次出现时，绘制图像（如果有的话）并且生成文本。
        """
        # 首先，使用填充背景色的方式清空屏幕：
        screen.fill(config.background_color)

        # 使用默认的外观和指定的大小创建Font对象
        font = pygame.font.Font(None, config.font_size)

        # 获取self.text中的文本行,忽略开头和结尾的空行：
        lines = self.text.strip().splitlines()

        # 计算文本的高度(使用 font.get_linesize()）以获取每行文本的高度：
        height = len(lines) * font.get_linesize()

        # 计算文本的放置位置（屏幕中心）：
        center, top = screen.get_rect().center
        top -= height // 2
        # 如果有图片要显示的话...
        if self.image:
            # 载入图片：
            image = pygame.image.load(self.image)
            # 获取它的rect:
            r = image.get_rect()  # 为rect(0,0,166,132)
            # 将图像向下移动其高度的一半的距离：
            top += r.height // 2
            # 将图片放置在文本上方20像素处：
            r.midbottom = center, top - 20
            # 将图像移动到屏幕上：
            screen.blit(image, r)

        antialias = 1
        black = 0, 0, 0

        # 生成所有行，从计算过的top开始，并且对于每一行向下移动font.get_linesize()像素
        for line in lines:
            text = font.render(line.strip(), antialias, black)
            r = text.get_rect()
            r.midtop = center, top
            screen.blit(text, r)
            top += font.get_linesize()

        # 显示所有更改
        pygame.display.flip()

class Info(Paused):
    """
    简单的暂停状态，显示有关游戏的信息。在Level状态后显示（第一级）
    """
    nextState = Level
    image = config.info_image
    text = ''

class StartUp(Paused):
    """
    显示展示图片和欢迎信息的暂停状态。在Info状态后显示。
    """
    nextState = Info
    image = config.splash_image
    text = ''

class LevelCleared(Paused):
    """
    提示用户过关的暂停状态。在next level状态后显示。
    """
    def __init__(self, number):
        self.number = number
        self.text = ' %i ' % (self.number + 1)

        self.image = config.level_image

    def nextState(self):
        return Level(self.number+1)

class GameOver(Paused):
    """
    提示用户输掉游戏的状态。在first level后显示。
    """
    global global_score
    def __init__(self, score):
        self.nextState = Level
        self.image = config.gameover_image
        self.text = '%d'%score
        global_score = 0.0


class Victory(Paused):
    """
    提示用户游戏胜利结束。在first level后显示。
    """
    global global_score
    def __init__(self, score):
        self.nextState = Level
        self.image = config.victory_image
        self.text = '%d'%score
        global_score = 0.0


class Game:
    """
    负责主事件循环的游戏对象，任务包括在不同状态间切换。
    """

    def __init__(self, *args):
        # 无状态方式启动：
        self.state = None
        # 在第一个事件循环迭代中移动到StartUp
        self.nextState = StartUp()

    def run(self):
        """
        这个方法动态设定变量。进行一些重要的初始化工作，并且进入主事件循环。
        """
        pygame.init()  # 初始化所有 pygame 模块。

        # 决定以窗口模式还是全屏模式显示游戏
        flag = RESIZABLE  # 默认窗口

        if config.full_screen:
            flag = FULLSCREEN  # 全屏模式

        screen_size = config.screen_size
        screen = pygame.display.set_mode(screen_size, flag)

        pygame.display.set_caption(config.screen_caption)
        pygame.mouse.set_visible(False)

        # 主循环：
        while True:
            # (1) 如果nextState被修改了，那么移动到新状态，并且显示它（第一次）
            if self.state != self.nextState:
                self.state = self.nextState
                self.state.firstDisplay(screen)
            # (2)代理当前状态的事件处理
            for event in pygame.event.get():
                self.state.handle(event)
            # (3) 更新当前状态：
            self.state.update(self)
            # (4) 显示当前状态：
            self.state.display(screen)

if __name__ == '__main__':
    game = Game(*sys.argv)
    game.run()
```

monkey\_rob\_banana.py改动比较大，现在做详细的介绍。
total_core是一个全局变量，因为在游戏过程中和游戏结束时都要用到。
State类是一个表示状态的基类。前面讲过了，游戏就是一系列的状态转换，所以要定义一个基本的状态类作为以后个状态类的基类。

Paused类也是一个基类，用来定义游戏暂停时的状态。比如游戏开始或结束时要暂停，等待用户决定是重新开始新的游戏还是结束整个游戏。

StartUup类，这是整个游戏的初始状态。显示游戏版本信息等，转到Info状态。

Info类，显示游戏的使用方法，转到Level状态。

Level类。游戏的主要部分，决定游戏的下一步走向。

1. 如果这一级所有的香蕉都落下，而猴子没有抢到规定的香蕉数，则转换到gameover状态。

2. 如果猴子抢到了规定数量的香蕉，则转到进级（LevelCleared）状态。

3. 如果最高级别都通过了，则转到Victory状态。

4. 其它情况，显示当前级别、还剩香蕉数和当前的得分。下一个状态仍然是Level.

LevelCleared类，显示进级信息，然后转到Level状态。

gameOver类，显示总的分。然后根据有用户确认是继续游戏还是结束游戏。

Victory类，达到了最高级别，由用户确定是是继续游戏还是结束游戏。

Game类，主控程序。

1.  __init__(),指出下一个状态是StartUp。

2.  run(),首先调用pygame.init()初始化pygame, 然后显示游戏窗口，最后就是从StartUp状态开始控制游戏的进行，直到按下ESC键。

主程序就是生成一个game类的实例，再调用game类的run方法开始游戏。

以上介绍了游戏的代码功能，你可以调整config.py中的配置参数（如每一级香蕉的数量，要进级需要抢够的香蕉数，最高级别，香蕉和猴子的图形文件等）已满足你的需求。

<br>

## 进一步探讨

现在实现了游戏的最基本功能，还可以增加音响效果（如香蕉下落时和猴子抢到香蕉时）、猴子抢到香蕉时显示猴子得意的画面等等。

以上以猴子抢香蕉为例简单介绍了pygame的基本功能和游戏开发的步骤及方法，希望通过以上的介绍能让你对用pygame编制游戏程序有一个基本的了解。



{% include sharepost.html %}