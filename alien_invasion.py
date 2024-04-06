# -*- coding = utf-8 -*-
# @Time : 2024/3/26 22:40
# @Author : csf
# @File : alien_invasion.py
# @Software : PyCharm


import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()  # 创建Settings实例并将其赋给self.settings便于之后可以便捷地改变设置值
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)  # 创建飞船实例【其中Ship(self)中的self表示AlienInvasion实例】

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
