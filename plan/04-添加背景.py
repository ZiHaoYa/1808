import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))#创建游戏窗口
bg = pygame.image.load('./images/background1.png')#加载图像
screen.blit(bg,(0,0))#贴图像
pygame.display.update()#更新
while True:
    pass
pygame.quit()

