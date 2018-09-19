import pygame
# 游戏屏幕大小
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
#敌机添加事件
CREATE_ENEMY_EVENT = pygame.USEREVENT

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
        super().__init__(imagename, 5)


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






# 创建精灵类
# 创建精灵对象
# 创建精灵组
# 更新精灵组
# 绘画精灵组        