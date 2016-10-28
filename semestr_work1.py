import Blender
from Blender import Draw, BGL
from Blender.BGL import *
import time
import math

x_circle=[]
y_circle=[]
is_draw=1

def changeR():
	global R
	R+=1
	if R>1000:
		Draw.Exit()
	time.sleep(0.1)
	Draw.Redraw(1)
def circle_coords(R,center):
	global x_circle, y_circle
	del x_circle[0:]
	del y_circle[0:]
	n=100
	dx=2*R/n
	for i in range(n):
		x_circle.append(dx*i+center[0]-R)
		y_circle.append((R*R-(dx*i-R)**2)**0.5+center[1])
	for i in range(n):
		x_circle.append(R-dx*i+center[0])
		y_circle.append(-(R*R-(dx*i-R)**2)**0.5+center[1])


def event(evt, val):
	global is_draw
	if evt == Draw.ESCKEY :
		Draw.Exit()
	if evt==Draw.RKEY:
		is_draw=1
		Draw.Register(gui, event,button_event)

		return
def mid(x0,x1):
	return [(x0[0]+x1[0])/2, (x1[1]+x0[1])/2]

def vector(x0,x1):
	return [x1[0]-x0[0], x1[1]-x0[1]]


def dPoint(R, n,mid,x0):
	if n[1]!=0:
		if n[0]==0:
			sign=1
		else:
			sign=-(n[0]/n[1])/math.fabs(n[0]/n[1])
		len=R*R-(dist_p_to_p_sqr(mid,x0))
		dx=sign*(((len*n[1]*n[1])/(n[0]**2+n[1]**2))**0.5)
		dy=((len*n[0]*n[0])/(n[0]**2+n[1]**2))**0.5
		return [dx,dy]
	else:
		return [0,math.sqrt(R*R-(x0[0]-mid[0])**2)]

def counter(x0,x1,R,sign):
	global x_circle,y_circle
	midl=mid(x0,x1)
	norm=vector(x0,x1)
	dp=dPoint(R,norm,midl,x0)
	center=[midl[0]+sign*dp[0], midl[1]+sign*dp[1]]
	circle_coords(R,center)

def dist_p_to_p_sqr(x0,x1):
	return (x1[0]-x0[0])**2+(x1[1]-x0[1])**2

def gui():
	global x_circle,y_circle,x0,x1,R, is_draw
	if is_draw==1:#we make PupBlock
		glClear(GL_COLOR_BUFFER_BIT)
		Draw.PushButton("Write points and R",1,100,100,200,50,"Write point and raduis,please")
		glRasterPos2f(100.0,200.0)
		Draw.Text("Press ESC to exit and R to restart")
	elif is_draw==2:#we draw circles
		glClearColor(0,0,0,1)
 		glClear(GL_COLOR_BUFFER_BIT)
		glLineWidth(2)
		glColor3f(1.0,0,0)
		glBegin(GL_LINE_LOOP)
		counter(x0,x1,R,1)
		for i in range(len(x_circle)):
			glVertex2f(x_circle[i],y_circle[i])
		glEnd()
		glColor3f(0,0,2)
		glBegin(GL_LINE_LOOP)
		counter(x0,x1,R,-1)
		for i in range(len(x_circle)):
			glVertex2f(x_circle[i],y_circle[i])
		glEnd()
		glColor3f(0, 1.0, 0.5)
		glPointSize(5)
		glBegin(GL_POINTS)
		glVertex2f(x0[0],x0[1])
		glVertex2f(x1[0],x1[1])
		glEnd()
		changeR()
	elif is_draw==3:#error: diametr is less distance between points
		glClear(GL_COLOR_BUFFER_BIT)
		glColor3f(1.0,0,0)
		glRasterPos2f(100.0,200.0)
		Draw.Text("ERROR! Diametr of cicle is less distance between points!!!!   Press ESC to exit and R to restart")

def button_event(evt):
	global x0,x1,R, is_draw
  	if evt == 1:

		x_start=Draw.Create(0.0)
		y_start=Draw.Create(0.0)
		x_end=Draw.Create(0.0)
		y_end=Draw.Create(0.0)
		R_circle=Draw.Create(0.0)
		block=[]
		block.append(("X0= ",x_start,0.0,800.0))
		block.append(("Y0= ",y_start,0.0,800.0))
		block.append(("X1= ",x_end,0.0,800.0))
		block.append(("Y1= ",y_end,0.0,800.0))
		block.append(("R= ",R_circle,0.0,1000.0))
		retVal=Draw.PupBlock("Line coords",block)
		x0=[x_start.val, y_start.val]
		x1=[x_end.val,y_end.val]
		R=R_circle.val
		if(dist_p_to_p_sqr(x0,x1)>4*R*R):
			is_draw=3
		else:
			is_draw=2
		Draw.Redraw(1)
		return


Draw.Register(gui, event,button_event)
