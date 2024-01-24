import PIL.Image as img
import numpy as np

xmin = -2.0 
xmax = 1.0
ymin = -1.0 
ymax = 1.0
xpix = 600
ypix = 400
maxiter = 40

pict = img.new( mode="RGB", size=(xpix, ypix) )
z = np.zeros( (xpix,ypix), dtype=complex )

for x in range(xpix): 
    for y in range(ypix):
        z[x][y] = complex( (xmax-xmin)/xpix*x+xmin, -((ymax-ymin)/ypix*y+ymin) )

print(z[0][0], z[xpix-1][ypix-1])

for x in range(xpix):  
    for y in range(ypix):
        c = z[x][y]
        for i in range(maxiter):
            zn = z[x][y] ** 2 + c
            if ( abs(zn) > 2.0 ):
                pict.putpixel( (x,y), (255,i*6+15,0) )
                break
            else:
                z[x][y] = zn
                       
pict.show()
