import Blender
from Blender import Draw, BGL
from Blender.BGL import *
#Bresenhems algorithm for lines
def event(evt, val):
    if evt == Draw.ESCKEY :
        Draw.Exit()
        return
def drawline(x0,y0,x1,y1,width):
	glPointSize(width)
	glColor3f(0,0,1)

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
	sw=False
	if dy>dx:
		dy,dx=dx,dy
		sw=True
	err=0
	derr=dy
	glBegin(GL_POINTS)
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



def gui():
	global x0,y0,x1,y1,width,is_line_point
	print is_line_point
	if is_line_point==False:
		Draw.PushButton("Write points and width",1,100,100,200,50,"Write point and width of line,please")
	else:
		glClearColor(0,0,0,1)
		glClear(BGL.GL_COLOR_BUFFER_BIT)
		drawline(x0,y0,x1,y1,width)



def button_event(evt):
	global x0,y0,x1,y1,width,is_line_point
  	if evt == 1:
		x_start=Draw.Create(0)
		y_start=Draw.Create(0)
		x_end=Draw.Create(0)
		y_end=Draw.Create(0)
		width_line=Draw.Create(0)
		block=[]
		block.append(("X0= ",x_start,0,800))
		block.append(("Y0= ",y_start,0,800))
		block.append(("X1= ",x_end,0,800))
		block.append(("Y1= ",y_end,0,800))
		block.append(("width= ",width_line,1,20))
		retVal=Draw.PupBlock("Line coords",block)
		x0=x_start.val
		y0=y_start.val
		x1=x_end.val
		y1=y_end.val
		width=width_line.val
		print x0,y0,x1,y1,width
		is_line_point=True
		Draw.Redraw(1)
		return

is_line_point=False
Draw.Register(gui, event, button_event)
