import PIL.Image as img
import numpy as np

xmin = -2.0 
xmax = 1.0
ymin = -1.0 
ymax = 1.0
xpix = 600
ypix = 400
maxiter = 255

pict = img.new( mode="RGB", size=(xpix, ypix) )
c = np.zeros( (xpix,ypix), dtype=complex )

for x in range(xpix): 
    for y in range(ypix):
        c[x][y] = complex( (xmax-xmin)/xpix*x+xmin, -((ymax-ymin)/ypix*y+ymin) )

for x in range(xpix):  
    for y in range(ypix):
        z = 0
        for i in range(maxiter):
            z = z ** 2 + c[x][y]
            if ( abs(z) > 2.0 ):
                pict.putpixel( (x,y), (255-i,0,i) )
                break
                       
pict.show()
