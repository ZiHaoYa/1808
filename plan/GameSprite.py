import pygame


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
        super().__init__(imagename, 10)
