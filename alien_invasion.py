# -*- coding = utf-8 -*-
# @Time : 2024/3/26 22:40
# @Author : csf
# @File : alien_invasion.py
# @Software : PyCharm


import sys
import pygame

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # 让最近绘制的屏幕可见
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()