import random
import pygame
# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#敌机添加事件
CREATE_ENEMY_EVENT = pygame.USEREVENT

#子弹事件
CREATE_BULLET_EVENT = pygame.USEREVENT+1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imagename, speed=1):
        super().__init__()  # 调用父类
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()  # 获取围栏
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class EnemySprite(GameSprite):  # 敌机精灵
    def __init__(self):
        imagename = './images/enemy1.png'
        super().__init__(imagename, random.randint(1,10))
        self.rect.bottom = 0#可以让敌机从屏幕上方下来
        #限制飞机初始化屏幕外
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)


    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.height:#判断是否飞出屏幕
            self.kill()





class BackGroundSprint(GameSprite):#背景精灵
    def __init__(self,isalt = True):
        imagename = './images/background.png'
        super().__init__(imagename)
        if not isalt:
            self.rect.bottom = 0

    def update(self):
        super().update()
        if self.rect.top >= SCREEN_RECT.height:#判断移除屏幕
            self.rect.bottom = 0#挪到屏幕上方


class HeroSprint(GameSprite):
    def __init__(self):
        imagename = './images/hero.gif'
        super().__init__(imagename,0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.height - 100
        self.speed1 = 0

    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed1

        if self.rect.left <= 0:
            self.rect.left = 0

        if self.rect.right >= SCREEN_RECT.width:
            self.rect.right = SCREEN_RECT.width  

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_RECT.height:
            self.rect.bottom = SCREEN_RECT.height        


class BulletSprite(GameSprite):
    def __init__(self):
        imagename = 'images/bullet1.png'
        super().__init__(imagename,-30)

    def update(self):
        super().update() 
        if self.rect.bottom <= 0:
            self.kill()   



# 创建精灵类
# 创建精灵对象
# 创建精灵组
# 更新精灵组
# 绘画精灵组        