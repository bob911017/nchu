# -*- coding: utf-8 -*-
from visual import *
scene = display()
g=sphere(color=color.green)
b=sphere(pos=g.pos+(2.5,0,0),color=color.blue)
r=sphere(pos=g.pos+(-2.5,0,0),color=color.red)
total=ellipsoid(pos=g.pos+(0,2.5,0),size=(6.5,2,2))
label_a=label(text=u'q和w調整紅色的比例\na和s調整綠色的比例\nz和x調整藍色的比例',pos=g.pos-(0,3,0),border=10,color=color.black,background=color.white,font='sans')
label_b=label(text='(0.0,0.0,0.0)',pos=total.pos,border=10,color=color.black,background=color.white)
step=0.01
while True:
    key=scene.kb.getkey()
    if key=='q':
        if r.color[0]-step<0:
            r.color=(0,0,0)
        else:
            r.color=tuple([r.color[0]-step,r.color[1],r.color[2]])
    if key=='w':
        if r.color[0]+step>1:
            r.color=(1,0,0)
        else:
            r.color=tuple([r.color[0]+step,r.color[1],r.color[2]])
    if key=='a':
        if g.color[1]-step<0:
            g.color=(0,0,0)
        else:
            g.color=tuple([g.color[0],g.color[1]-step,g.color[2]])
    if key=='s':
        if g.color[1]+step>1:
            g.color=(0,1,0)
        else:
            g.color=tuple([g.color[0],g.color[1]+step,g.color[2]])
    if key=='z':
        if b.color[2]-step<0:
            b.color=(0,0,0)
        else:
            b.color=tuple([b.color[0],b.color[1],b.color[2]-step])
    if key=='x':
        if b.color[2]+step>1:
            b.color=(0,0,1)
        else:
            b.color=tuple([b.color[0],b.color[1],b.color[2]+step])
    total.color=tuple([r.color[0],g.color[1],b.color[2]])
    label_b.text=str(tuple([round(r.color[0],2),round(g.color[1],2),round(b.color[2],2)]))
    key=0
