import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))#创建游戏窗口
bg = pygame.image.load('./images/background.png')#加载图像

hero = pygame.image.load('./images/hero.gif')

time = pygame.time.Clock()#游戏时钟

rect = pygame.Rect(200,200,100,126)
while True:
	time.tick(60)#每秒刷新100次
	rect.y -= 10
	screen.blit(bg,(0,0))#贴图像
	screen.blit(hero,rect)#贴图像

	if rect.bottom <= 0:#飞出屏幕外
		rect.top = 700
	#事件监听
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print("退出游戏")
			pygame.quit()
			exit()


	pygame.display.update()#更新


