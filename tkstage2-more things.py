#Stage 2 - more things
import tkinter as tk

#Your application must inherit from Frame
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)  #call parent constructor
        self.grid()  #necessary to make it appear on the screen!
        self.createWidgets()
        
    def createWidgets(self):
        #Add stuff to my application
        #bg is background colour
        self.testButton = tk.Button(self,text="Test",bg="#00ff00",command=self.myTest)
        self.quitButton = tk.Button(self,text="Quit",command=self.myQuit)
        self.testButton.grid(column = 0,row=0,padx=20,pady=20) #places the button on the app frame
        self.quitButton.grid(column = 1,row=0,padx=20,pady=20)
    
    def myTest(self):
        print("In here")
        
    def myQuit(self):
        quit()
        
app = Application()
app.master.title("TK Helloworld")
app.mainloop()
