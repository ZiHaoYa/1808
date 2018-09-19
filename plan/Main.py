import pygame
from GameSprite import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 创建游戏窗口
        self.clock = pygame.time.Clock()  # 游戏时钟
        self.__create_sprites()  # 创建精灵和精灵组

        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#定时器

        self.enemy_group = pygame.sprite.Group()

    def start_game(self):
        print("开始游戏...")
        while True:
            self.clock.tick(60)  # 每秒刷新60次
            self.__event_handler()
            self.__check_collide()
            self.__update_sprites()

            pygame.display.update()#更新



    def __create_sprites(self):#创建精灵的
        bgs = BackGroundSprint()
        bgs1 = BackGroundSprint(False)#这个隐藏在屏幕上面
        self.bgsg = pygame.sprite.Group(bgs,bgs1)
       

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)


    def __check_collide(self):
        """碰撞检测"""
        pass


    def __update_sprites(self):
        """更新精灵组"""
        self.bgsg.update()
        self.bgsg.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """游戏结束"""
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 开始游戏
    game.start_game()
