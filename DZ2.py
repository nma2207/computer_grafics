import Blender
from Blender import Draw, BGL
from Blender.BGL import *
#Bresenhems algorithm for lines
def event(evt, val):
    if evt == Draw.ESCKEY :
        Draw.Exit()
        return

def gui():
	sw=False
	glClearColor(0,0,0,1)
	global width
	glPointSize(width)
	glClear(BGL.GL_COLOR_BUFFER_BIT)
	glColor3f(0,0,1)
	glBegin(GL_POINTS)
	global x0,x1,y0,y1
	if x0>x1:
		x0,x1=x1,x0
		y0,y1=y1,y0
	dx=x1-x0
	dy=y1-y0
	y=0
	sign=1
	if y1<y0:
		sign=-1
		dy=-dy
	if dy>dx:
		dy,dx=dx,dy
		sw=True


	err=0
	derr=dy
	for x in range(dx+1):
		px,py=0,0

		if sw==True:
			px,py=sign*y+x0,sign*x+y0
		else:
			px,py=x+x0,y+y0
		glVertex2i(px,py)
		err+=derr
		if 2*err>=dx:
			y+=sign
			err-=dx
	glEnd()

print 'write points and width,please'
x0=int(raw_input('x0='))
y0=int(raw_input('y0='))
x1=int(raw_input('x1='))
y1=int(raw_input('y1='))
width=int(raw_input('width='))
Draw.Register(gui,event,None)
