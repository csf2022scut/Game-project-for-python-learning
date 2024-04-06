# -*- coding = utf-8 -*-
# @Time : 2024/3/28 16:56
# @Author : csf
# @File : settings.py
# @Software : PyCharm

class Settings:
    '''存储游戏中所有设置的类'''
    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)