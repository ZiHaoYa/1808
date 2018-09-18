import pygame
from GameSprite import *

pygame.init()
screen = pygame.display.set_mode((480, 700))  # 创建游戏窗口
bg = pygame.image.load('./images/background.png')  # 加载图像

hero = pygame.image.load('./images/hero.gif')

time = pygame.time.Clock()  # 游戏时钟

rect = pygame.Rect(200, 200, 100, 126)

enemy = EnemySprite()  # 创建一个敌机精灵对象
enemy1 = EnemySprite()  # 创建一个敌机精灵对象
enemy1.rect.y = 100
enemy1.rect.x = 100
enemy_group = pygame.sprite.Group(enemy, enemy1)  # 把精灵加到精灵组中

while True:
    time.tick(60)  # 每秒刷新100次
    rect.y -= 10
    screen.blit(bg, (0, 0))  # 贴图像
    screen.blit(hero, rect)  # 贴图像

    if rect.bottom <= 0:  # 飞出屏幕外
        rect.top = 700
    # 事件监听
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()

    enemy_group.update()  # 调用精灵组的update
    enemy_group.draw(screen)  # 刷新到屏幕上

    pygame.display.update()  # 更新
