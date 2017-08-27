from reportlab.lib.pagesizes import *
from reportlab.lib.colors import *
from reportlab.lib.units import cm

class canvasSpec:
	def __init__ (self,object):
		self.filename=object.filename
		self.size=object.size
		self.width=object.size[0]
		self.height=object.size[1]
		self.xgap=object.xgap
		self.ygap=object.ygap
		self.xlist=[]
		self.ylist=[]
		self.xStart=0
		self.yStart=0

def draw(object,detailTF,canvas,color,lineWidth):
	def xylist(startPoint,list,max,gap,detailTF):
		i=startPoint*cm
		if detailTF==1:
			while i<max-5*gap*cm:
				for j in range(0,5):
					list.append(i+j*gap*cm)
				i+=5*gap*cm
			list.append(list[-1]+gap*cm)
		elif detailTF==0:
			while i<max-5*gap*cm:
				list.append(i)
				i+=5*gap*cm
			list.append(list[-1]+5*gap*cm)

	def align(max,gap):
		return((converter(max) % (5*gap)) / 2)

	def gridB(object,canvas,color,lineWidth,xlist,ylist):
		canvas.setStrokeColor(color)
		canvas.setLineWidth(lineWidth)
		canvas.grid(xlist,ylist)
		object.xStart=xlist[0]
		object.yStart=ylist[0]
		object.xlist=[]
		object.ylist=[]


	def converter(px):
		return(px * 2.54 / 72)

	xylist(align(object.width,object.xgap),object.xlist,object.width,object.xgap,detailTF)
	xylist(align(object.height,object.ygap),object.ylist,object.height,object.ygap,detailTF)
	gridB(object,canvas,color,lineWidth,object.xlist,object.ylist)
	