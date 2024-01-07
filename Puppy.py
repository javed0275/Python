#A python program to display images in the canvas 

from tkinter import *
#create root window
root=Tk()
#create canvas as a child to root window
c=Canvas(root,bg="white",height=700,width=1200)
#copy images into files 
file1= PhotoImage(file="cat.gif")
file2= PhotoImage(file="puppy.gif")
#display the image in the canvas in NE direction
#When mouse is placed on CAT image,we can see puppy image
id=c.create_image(500,200,anchor=NE,image=file1,activeimage=file2)
#display some text below the image 
id=c.create_text(500,500,text="This is a thrilling photo",font=('Helvetica',30,'bold'),fill="blue")
#add canvas to the root
c.pack()
#wait for any events
root.mainloop()
