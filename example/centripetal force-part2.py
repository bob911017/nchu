# -*- coding: utf-8 -*-
from visual import *
from visual.controls import *
import numpy as np

w=np.pi #rad/s
dt=0.001  #s
t=0 #s
 
scene1=display(title='data')    #建立視窗紀錄數值
background=box(size=(2,2,0.02),material=materials.wood)
l_f=label(border=10,color=color.black,background=color.white,pos=(0,0.5,0))
l_r=label(border=10,color=color.black,background=color.white,pos=l_f.pos+(0,-0.5,0))
l_m=label(border=10,color=color.black,background=color.white,pos=l_f.pos+(0,-1,0))

scene2=display(title='show',background=(0.6,1,0.8))    #建立視窗模擬實際狀況
#center=sphere(radius=0.05)  #中心點
a=sphere(radius=0.1,color=(1,0,0))   #繞中心點進行圓周運動的物體a
b=sphere(radius=0.1,color=(0,0,1))  #繞中心點進行圓周運動的物體b
rod=cylinder(pos=a.pos,radius=0.03,color=(0.7,0.7,0.7))#連結兩物體的桿子
rod2=cylinder(axis=(0,0,-1),radius=0.03,color=(0.7,0.7,0.7)) #還是竿子
rod3=cylinder(pos=(0,0,-1),axis=(0,0,-0.03),color=(0.7,0.7,0.7)) #底下的圓盤
fa=arrow(fixedwidth = True,shaftwidth=0.03) #a物體的向心力

c=controls(width=330, height=440)   #建立控制視窗
r=slider(min=0.3,max=3.0,length=70,width=20) #radius(m)
m=slider(min=1.0,max=20.0,length=70,width=20,pos=(0,-60,0)) #mass(kg)
bot_r=button(pos=r.pos+(-50,0),text='radius(m)')    #控制半徑的東東
bot_m=button(pos=bot_r.pos+(0,-60),text='mass(kg)') #控制質量的東東

while True:
    rate(1/dt)
    a.pos.x=r.value*np.cos(w*t) #x=r*cos(w*t)
    a.pos.y=r.value*np.sin(w*t) #y=r*sin(w*t)
    fa.pos.x=1.3*r.value*np.cos(w*t-np.pi/10)   #把箭頭放在物體a旁邊，所以加一個相位差，避免重疊
    fa.pos.y=1.3*r.value*np.sin(w*t-np.pi/10)
    fa.axis=-1.2*a.pos*(m.value/m.max)
    fa.color=(1-r.value/r.max,1-r.value/r.max,1-r.value/r.max)
    b.pos.x=r.value*np.cos(w*t+np.pi) #b物體在a對面所以加一個180度的相位差
    b.pos.y=r.value*np.sin(w*t+np.pi) 
    rod.pos=a.pos
    rod.axis=b.pos-a.pos
    l_f.text=u'Centripetal force='+str(round(m.value*w*w*np.sqrt(a.pos.x**2+a.pos.y**2),2))+'N'
    l_r.text=u'radius='+str(round(r.value,2))+' m'
    l_m.text=u'mass='+str(round(m.value,2))+' kg'
    t+=dt
