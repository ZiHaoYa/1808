import pygame
from GameSprite import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode((480, 700))  # 创建游戏窗口
        self.clock = pygame.time.Clock()  # 游戏时钟
        self.__create_sprites()  # 创建精灵和精灵组

    def start_game(self):
        print("开始游戏...")
        while True:
            self.clock.tick(60)  # 每秒刷新60次

    def __create_sprites(self):
        pass

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()

    def __check_collide(self):
        """碰撞检测"""
        pass

    def __update_sprites(self):
        """更新精灵组"""
        pass

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
