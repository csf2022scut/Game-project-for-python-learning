# -*- coding = utf-8 -*-
# @Time : 2024/3/28 16:43
# @Author : csf
# @File : ship.py.py
# @Software : PyCharm

import pygame

class Ship:
    '''管理飞船的类'''
    def __init__(self, ai_game):  # ai_game是AlienInvasion类的实例
        """ 初始化飞船并设置其初始位置 """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()

        # 对于每一艘新飞船，都将其放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom

    # 绘制飞船的函数
    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)