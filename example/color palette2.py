# -*- coding: utf-8 -*-
from visual import *
from visual.controls import *
c=controls(width=300, height=300)
g=sphere(color=color.green)
b=sphere(pos=g.pos+(2.5,0,0),color=color.blue)
r=sphere(pos=g.pos+(-2.5,0,0),color=color.red)
total=ellipsoid(pos=g.pos+(0,2.5,0),size=(6.5,2,2))
l=label(text='(0.0,0.0,0.0)',pos=total.pos,border=10,
              color=color.black,background=color.white)
gs=slider(min=0,max=1.0,length=60,width=20)
rs=slider(min=0,max=1.0,pos=gs.pos+(0,60),length=60,width=20)
bs=slider(min=0,max=1.0,pos=gs.pos+(0,-60),length=60,width=20)
botg=button(pos=gs.pos+(-50,0),text='green')
botr=button(pos=botg.pos+(0,60),text='red')
botb=button(pos=botg.pos+(0,-60),text='blue')
while True:
    total.color=(rs.value,gs.value,bs.value)
    l.text=str([round(total.color[0],2),
                      round(total.color[1],2),round(total.color[2],2)])  
