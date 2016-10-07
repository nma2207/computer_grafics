import Blender
from Blender import Draw, BGL
from Blender.BGL import *
import time
x=0
y=0
def event(evt, val):
    if evt == Draw.ESCKEY :
        Draw.Exit()
        return

def gui():
	sw=False
	glClearColor(0,0,0,1)
	glPointSize(2)
	glClear(BGL.GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	glBegin(GL_POINTS)
	dx=x1-x0
	dy=y1-y0
	x2=x1-x0
	y2=y1-y0
	sign=1
	if y1<y0:
		sign=-1
		dy=-dy
		y2=-y2
	if y2>x2:
		y2,x2=x2,y2
		dx,dy=dy,dx
		sw=True
	err=0
	print x2
	print y2
	derr=dy
	y=0
	for x in range(0,x2+1):
		px,py=0,0

		if sw==True:
			px,py=y+y0,x+x0
		else:
			px,py=x+x0,y+y0
		glVertex2i(px,py)
		err+=derr
		if 2*err>=dx:
			y+=sign
			err-=dx
	glEnd()

print 'write points,please'
x0=int(raw_input())
y0=int(raw_input())
x1=int(raw_input())
y1=int(raw_input())
Draw.Register(gui,event,None)
