Simple mandelbrot set image generator written in Python. Uses Numpy for complex numbers and the PIL Image library for generating a PNG full color image. It is not fast. The image size, coordinates, and maximum number of iterations can be changed. On UNIX systems this program will open the image using the xv viewer when completed. To run it:

$ python mandelbrot.py

Here's an ASCII depiction of the Mandelbrot set. This is similar to the very first visualization of the Mandelbrot set that was produced in 1979 by J. Peter Matelski using a UNIVAC mainframe.


                                            @  @                            
                                             @@@@@                          
                                             @@@@@                          
                                              @@@                           
                                    @@@  @@@@@@@@@@@@@                      
                                     @@@@@@@@@@@@@@@@@@@@@@                 
                                    @@@@@@@@@@@@@@@@@@@@@@                  
                                  @@@@@@@@@@@@@@@@@@@@@@@@@                 
                        @        @@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                     @@  @@      @@@@@@@@@@@@@@@@@@@@@@@@@@@                
                     @@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                    @@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                   
                 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                 
                    @@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                     @@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@                
                     @@  @@      @@@@@@@@@@@@@@@@@@@@@@@@@@@                
                        @        @@@@@@@@@@@@@@@@@@@@@@@@@@@@               
                                  @@@@@@@@@@@@@@@@@@@@@@@@@                 
                                    @@@@@@@@@@@@@@@@@@@@@@                  
                                     @@@@@@@@@@@@@@@@@@@@@@                 
                                    @@@  @@@@@@@@@@@@@                      
                                              @@@                           
                                             @@@@@                          
                                             @@@@@                          
                                            @  @

A fast interactive Mandelbrot explorer is available here:

https://math.hws.edu/eck/js/mandelbrot/MB.html

Also there are tons of "Mandelbrot Zoom" videos on Youtube.