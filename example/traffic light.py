# -*- coding: utf-8 -*-
"""
@author: Bo-Yin,Chen
工作單:
    一開始信號燈為閃爍黃燈，亮暗各0.5秒
    點擊滑鼠後亮綠燈2秒，接著亮黃燈1秒，接著亮紅燈5秒，不斷循環
    若途中第二次點擊滑鼠則變成閃爍間格1秒的黃燈
    第三次點擊滑鼠恢復正常紅綠燈的狀態，第四次則為閃黃燈.....依此類推
"""
from visual import *
scene = display(background=color.black,center=(0,-2,0))
y=sphere(color=color.gray(0.5))
g=sphere(pos=y.pos+(2.5,0,0),color=color.gray(0.5))
r=sphere(pos=y.pos+(-2.5,0,0),color=color.gray(0.5))
body=box(pos=y.pos+(0,0,-0.5),size=(8,3,1.5),material=materials.silver)
leg=cylinder(pos=body.pos,axis=(0,-8,0),radius=0.2)
label=label(text=u'點擊滑鼠啟動紅綠燈',pos=y.pos+(0,3,0),border=10,color=color.black,background=color.white)

play=100.0 #播放速率
t=9*play #紀錄時間，因為可能在閃黃燈途中切換模式，因此不設定為零

while True:
    rate(play)
    #點擊滑鼠2n次，進入閃黃燈模式#############################################
    if scene.mouse.clicked%2.0==0:  
        label.text=u'點擊滑鼠啟動紅綠燈'
        if t<9*play:   #避免切換為正常模式時，非綠燈開始
            t=(9*play)
        else:
            if r.color==color.red or g.color==color.green:
                r.color=color.gray(0.5)
                g.color=color.gray(0.5)
            if t%(play/2)==0:   #每0.5秒切換一次
                if y.color==color.yellow:
                    y.color=color.gray(0.5)
                else:
                    y.color=color.yellow
            t+=1    #用(1/play)來記數的話，取餘數常出錯，因此改用1
            
    #點擊滑鼠2n+1次，進入正常模式############################################
    if scene.mouse.clicked%2.0==1:          
        if t<=2*play:   #亮綠燈兩秒
            label.text=u'點擊滑鼠轉為閃黃燈'+'\n            '+str(2-t/play)
            g.color=color.green
            r.color=color.gray(0.5)
            y.color=color.gray(0.5)
            t+=1
        elif t<=3*play: #亮黃燈一秒
            label.text=u'點擊滑鼠轉為閃黃燈'+'\n            '+str(3-t/play)
            y.color=color.yellow
            g.color=color.gray(0.5)
            t+=1
        elif t<=8*play: #亮紅燈五秒
            label.text=u'點擊滑鼠轉為閃黃燈'+'\n            '+str(8-t/play)
            r.color=color.red
            y.color=color.gray(0.5)
            t+=1
        else:           #第(2+1+5)秒後重新計時
            t=0
            t+=1
