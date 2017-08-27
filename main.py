from reportlab.pdfgen import canvas
from GridPdf.myfunc import *
from settings import Settings

#Create a canvas
setting=Settings()
cSpec=canvasSpec(setting)
c = canvas.Canvas(cSpec.filename+".pdf",cSpec.size)

#Main draw func with inputs (object,detailTF,canvas,color,lineWidth)
draw(cSpec,1,c,setting.colorMinor,setting.lineWidthMinor)
if setting.majorLine==True:
	draw(cSpec,0,c,setting.colorMajor,setting.lineWidthMajor)

#Footer
c.setFont("Times-Roman", 7)
c.drawString(cSpec.xStart,cSpec.yStart/2,setting.footer)

c.showPage()
c.save()