# -*- coding: utf-8 -*-
from visual import *
from visual.controls import *
import numpy as np

w=np.pi #rad/s
dt=0.001  #s
t=0 #s

scene1=display(title='data')    #建立視窗紀錄數值
background=box(size=(2,2,0.02),material=materials.wood)
lf=label(border=10,color=color.black,background=color.white,pos=(0,0.5,0))
lr=label(border=10,color=color.black,background=color.white,pos=lf.pos+(0,-0.5,0))
lm=label(border=10,color=color.black,background=color.white,pos=lf.pos+(0,-1,0))

scene2=display(title='show')    #建立視窗模擬實際狀況
center=sphere(radius=0.05)
a=sphere(pos=center.pos+(1,0,0),radius=0.1,color=(1,0,0))

c=controls(width=330, height=440)   #建立控制視窗
r=slider(min=0.3,max=3.0,length=70,width=20) #m
m=slider(min=1,max=20,length=70,width=20,pos=(0,-60,0)) #m
botr=button(pos=r.pos+(-50,0),text='radius(m)')
botm=button(pos=botr.pos+(0,-60),text='mass(kg)')

while True:
    rate(1/dt)
    a.pos.x=r.value*np.cos(w*t) #x=r*cos(w*t)
    a.pos.y=r.value*np.sin(w*t) #y=r*sin(w*t)
    lf.text=u'Centripetal force='+str(round(m.value*w*w*np.sqrt(a.pos.x**2+a.pos.y**2),2))+'N'
    lr.text=u'radius='+str(round(r.value,2))+' m'
    lm.text=u'mass='+str(round(m.value,2))+' kg'
    t+=dt
