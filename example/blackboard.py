# -*- coding: utf-8 -*-
"""
@author: Bo-Yin,Chen

"""
from visual import *
scene = display(background=(1,1,1))
play=1000.0 #播放速率
add=0 #新增一個用來產生線的變數
label=label(text=u'點擊滑鼠開始繪圖',border=10,color=color.black,background=color.white)
board=box(size=(5,2,0.1),pos=(0,0,-0.051),color=(0,0.2,0))
bottom=box(size=(5,0.1,0.2),pos=(0,-0.05-1,0),color=(0.4,0.2,0))
while True:
    rate(play)
    #當滑鼠點擊次數為2n次且add為0時，產生一條新的線
    if scene.mouse.clicked%2.0==0 and add==0:
        label.visible=True
        line=curve() #新增一條線       
        add=1   #將add改為1，避免一直產生新的線

    #當滑鼠點擊次數為2n+1次
    if scene.mouse.clicked%2.0==1:
        if abs(scene.mouse.pos.x)<=2.5 and abs(scene.mouse.pos.y)<=1 and scene.mouse.pos.z<0.001:            
            label.visible=False
            line.append(pos=scene.mouse.pos)    #將滑鼠所在位置記錄在line裡面
            add=0   #刷新產生線的變數
