#Stage 2 - more things
import tkinter as tk
import random,sqlite3

#good guide
#https://github.com/StevePaget/ActivitiesDatabase

CANVAS_BORDER = 5

#Your application must inherit from Frame
class Application(tk.Frame):
    def __init__(self,master=None):
        tk.Frame.__init__(self,master)  #call parent constructor
        self.grid()  #necessary to make it appear on the screen!
        self.createWidgets()
        self.config(cursor="hand2")
        
    def createWidgets(self):
        #Add stuff to my application
        #bg is background colour
        #canvas bd is border width for canvas
        self.testButton = tk.Button(self,text="Test",bg="#00ff00",command=self.myTest)
        self.dbTest = tk.Button(self,text="Test DB",bg="#aa00ff",command=self.myDBTest)
        self.quitButton = tk.Button(self,text="Quit",command=self.myQuit)
        
        self.canvas1 = tk.Canvas(self,height=100,width=60,bd=CANVAS_BORDER,relief=tk.RIDGE)
        self.testButton.grid(column = 0,row=0,padx=20,pady=20) #places the button on the app frame
        self.dbTest.grid(column = 1,row=0,padx=20,pady=20)
        self.quitButton.grid(column = 2,row=0,padx=20,pady=20)
        self.canvas1.grid(row=2)
    
    def create_sqlite_database(self,filename):
        """ create a database connection to an SQLite database """
        #https://www.sqlitetutorial.net/sqlite-python/creating-tables/
        
        self.dbConn = None
        try:
            self.dbConn = sqlite3.connect(filename)
            print(sqlite3.sqlite_version)
        except sqlite3.Error as e:
            print(e)
        finally:
            if self.dbConn:
                self.dbConn.close()
    
    def myDBTest(self):
        print("DB testing...")
        self.create_sqlite_database("testDB.db")
    
    def myTest(self):
        if(self.cursorType == "hand2"):
            self.cursorType = "umbrella"
        else:
            self.cursorType = "hand2"
            
        self.config(cursor=self.cursorType)
        
        #Draw on the canvas1
        self.canvas1.delete("all")
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        theID = self.canvas1.create_rectangle(CANVAS_BORDER+3,CANVAS_BORDER+3,20+randx,30+randy)
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        theID = self.canvas1.create_arc(CANVAS_BORDER+3,CANVAS_BORDER+3,20+randx,30+randy,style=tk.ARC)
        randx=random.randint(10,20)
        randy=random.randint(10,20)
        theID = self.canvas1.create_bitmap(CANVAS_BORDER+3+randx,CANVAS_BORDER+3+randy,bitmap="warning")

         
        print(theID)
        somecoords = self.canvas1.coords(theID)
        print(somecoords)

        somecoords = self.canvas1.bbox(theID)
        print(somecoords)

        someResult = self.canvas1.find_all()
        print(someResult)

        someResult = self.canvas1.type(theID)
        print(someResult)
        
        
    def myQuit(self):
        quit()
        
    cursorType = "hand2"
    
    dbConn = None
        
app = Application()
app.master.title("TK Helloworld")
app.mainloop()
