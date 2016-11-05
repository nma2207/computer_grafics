import os
import Blender
from Blender import Draw
from Blender.BGL import *
import time
from Blender.Mathutils import *
import math
from math import sin,cos
import random

changeColor=False
c1,c2,c3=0,0,0
colorA=0.0
signK=1
signA=1
A=0.0
k=1.0;

def changeA():
	da=.025
	dk=da/(2*math.pi)
	global changeColor,A,k,colorA,signK,signA;
	if A>2*math.pi:
		A-=math.pi*2
		signA*=-1
	if colorA>math.pi/2:
		changeColor=True
		colorA-=math.pi/2
	if k>2 or k<1:
		signK*=-1
	A+=da
	colorA+=da
	time.sleep(0.003)
	k+=signK*dk;
	#print k
	Draw.Redraw(1)



def rotMatr(ang): # ??????? ????????
	mtr=Matrix([cos(ang),-sin(ang)],[sin(ang),cos(ang)])
	return mtr

def sizeChangeMat(k):
	mtr=Matrix([k,0.0],[0.0,k])
	return mtr

def event(evt, val):
	if evt == Draw.ESCKEY :
		Draw.Exit()
	return

def randomColor():
	global changeColor,c1,c2,c3;
	#print c1,c2,c3
	if changeColor==True:
		c1,c2,c3=random.random(),random.random(),random.random()
		changeColor=False;
	glColor3f(c1,c2,c3)

def gui():
	global k,A,pc0,pc1,pc2,pc3,mid,signA
	glClearColor(1.0,1.0,1.0,1) # background color
	glClear(GL_COLOR_BUFFER_BIT) # clear image buffer
	glColor3f(0,0,0)
	rotMat=rotMatr(signA*A)
	sizeMat=sizeChangeMat(k)

	pn0=sizeMat*rotMat*pc0+mid
	pn1=rotMat*sizeMat*pc1+mid
	pn2=rotMat*sizeMat*pc2+mid
	pn3=rotMat*sizeMat*pc3+mid
	randomColor()
	glBegin(GL_QUADS)
	glVertex2f(*pn0)
	glVertex2f(*pn1)
	glVertex2f(*pn2)
	glVertex2f(*pn3)
	glEnd()
	print ((pn0[0]-pn1[0])**2+(pn0[1]-pn1[1])**2)**0.5
	changeA()
def pupBlock():
	global pc0,pc1,pc2,pc3,mid
	x=Draw.Create(500.0)
	y=Draw.Create(500.0)
	a=Draw.Create(100.0)
	block=[]
	block.append(("X= ", x, 0.0, 1000.0))
	block.append(("Y= ", y, 0.0, 1000.0))
	block.append(("a= ", a, 0.1, 1000.0))
	retVal=Draw.PupBlock("write coord of left top angle, and party of quard",block)
	mid=Vector(x.val+a.val/2, y.val-a.val/2)
	pc0=Vector(-a.val/2, a.val/2)
	pc1=Vector(a.val/2, a.val/2)
	pc2=Vector(a.val/2, -a.val/2)
	pc3=Vector(-a.val/2, -a.val/2)
	Draw.Register(gui, event, None)

Draw.Register(pupBlock, event, None)
#point =[float(i) for i in raw_input("write coord of left top angle:\n").split()]
#a=float(raw_input("write the praty of qard\n"))

#p0=Vector(point[0],point[1])
#p1=Vector(point[0]+a,point[1])
#p2=Vector(point[0]+a,point[1]-a)
#p3=Vector(point[0],point[1]-a)
#mid=Vector(point[0]+a/2, point[1]-a/2)

#pc0=p0-mid
#pc1=p1-mid
#pc2=p2-mid
#pc3=p3-mid
#Draw.Register(gui, event,None)
