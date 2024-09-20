#Stage 2 - more things
import tkinter as tk
import random

#Your application must inherit from Frame
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)  #call parent constructor
        self.grid()  #necessary to make it appear on the screen!
        self.createWidgets()
        self.config(cursor="circle")
        
    def createWidgets(self):
        #Add stuff to my application
        #bg is background colour
        #canvas bd is border width for canvas
        self.testButton = tk.Button(self,text="Test",bg="#00ff00",command=self.myTest)
        self.quitButton = tk.Button(self,text="Quit",command=self.myQuit)
        self.canvas1 = tk.Canvas(self,height=100,width=60,bd=10,relief=tk.RIDGE)
        self.testButton.grid(column = 0,row=0,padx=20,pady=20) #places the button on the app frame
        self.quitButton.grid(column = 1,row=0,padx=20,pady=20)
        self.canvas1.grid(row=2)
    
    def myTest(self):
        if(self.cursorType == "arrow"):
            self.cursorType = "watch"
        else:
            self.cursorType = "arrow"
            
        self.config(cursor=self.cursorType)
        
        #Draw on the canvas1
        self.canvas1.delete("all")
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        self.canvas1.create_rectangle(1,1,20+randx,30+randy)
        
    def myQuit(self):
        quit()
        
    cursorType = "arrow"
        
app = Application()
app.master.title("TK Helloworld")
app.mainloop()
