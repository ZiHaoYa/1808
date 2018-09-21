import pygame
from GameSprite import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # 创建游戏窗口
        self.clock = pygame.time.Clock()  # 游戏时钟
        

        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)#定时器
        pygame.time.set_timer(CREATE_BULLET_EVENT,100)#定时器1

        self.enemy_group = pygame.sprite.Group()

        self.bullet_group = pygame.sprite.Group()

        self.__create_sprites()  # 创建精灵和精灵组

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


        self.hero = HeroSprint()
        self.hero_group = pygame.sprite.Group(self.hero)

    

    def __event_handler(self):
        """事件监听"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = EnemySprite()
                self.enemy_group.add(enemy)
            elif event.type == CREATE_BULLET_EVENT:
                bullet = BulletSprite()
                bullet.rect.x = self.hero.rect.centerx 
                bullet.rect.y = self.hero.rect.top - 25

                bullet1 = BulletSprite()
                bullet1.rect.x = self.hero.rect.centerx -35
                bullet1.rect.y = self.hero.rect.top +35

                bullet2 = BulletSprite()
                bullet2.rect.x = self.hero.rect.centerx +35
                bullet2.rect.y = self.hero.rect.top +35


                self.bullet_group.add(bullet,bullet1,bullet2)  

        keys = pygame.key.get_pressed()
        self.hero.speed1 = 0
        self.hero.speed = 0
        if keys[pygame.K_RIGHT]:
            self.hero.speed = 4
        elif keys[pygame.K_LEFT]:
            self.hero.speed = -4
        elif keys[pygame.K_DOWN]:
            self.hero.speed1 = 4
        elif keys[pygame.K_UP]:
            self.hero.speed1 = -4
        else:
            self.hero.speed = 0 
            self.hero.speed1 = 0      
                



    def __check_collide(self):
        """碰撞检测"""
         # 1. 子弹摧毁敌机
        pygame.sprite.groupcollide(self.bullet_group, self.enemy_group, True, True)

        # 2. 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)

        # 判断列表时候有内容
        if len(enemies) > 0:

        # 让英雄牺牲
            self.hero.kill()

                # 结束游戏
            PlaneGame.__game_over()


    def __update_sprites(self):
        """更新精灵组"""
        self.bgsg.update()
        self.bgsg.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)


        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.bullet_group.update()
        self.bullet_group.draw(self.screen)

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
