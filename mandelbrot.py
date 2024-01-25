import PIL.Image as img
import numpy as np

xmin, xmax = -2.0, 1.0
ymin, ymax = -1.0, 1.0
xpix, ypix = 600, 400
maxiter = 50

p = img.new( mode="L", size=(xpix, ypix) )
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
                p.putpixel( (x,y), i*4+25 )
                break
                       
p.show()
