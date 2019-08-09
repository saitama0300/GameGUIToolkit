from tkinter import *
from PIL import ImageTk, Image
from random import randint

board = Tk()
board.geometry("1200x900")
board.title('LUDO')

scoreCard = Frame(board)
scoreCard.configure(bg="orange")
scoreCard.place(relx=1,rely=1, width=300, relheight = 1, anchor="se")

#again = Button(scoreCard,text="Again",command= lambda: rollB.config(state= "normal"))
#again.place(x=10,y=10)

turnV = 'r'

rollB = Button(scoreCard,text="Roll Dice !!",command= lambda: roll(dice), bg="Gold", borderwidth=4, relief="solid", font=('Arial', '15', 'bold'))
rollB.configure(width = 20, height = 4)
rollB.place(x=150,y=80, anchor = "center")

playerL = Label(scoreCard, width = 20, height = 2, text= "Active Player : RED", bg = "Coral", fg="Black", font=('Times', '20'), borderwidth=3, relief = "solid")
playerL.place(x=150, y=200, anchor="center")

clrB = Label(scoreCard, width =8, height=4, bg = "Red", borderwidth=4, relief="solid")
clrB.place(x=150, y=480, anchor = "center")

brd = Frame(board)
brd.place(x=900,y=900,width=900,height=900, anchor= "se")

board.update()
turn= ["r","g","y","b"]
s = 55

pointL = Label(scoreCard, width = 100, height = 4, bg="Coral", fg="Black" ,text="Previous Dice Numbers",font=('Times', '20'), borderwidth=3, relief = "solid")
pointL.place(x=150,y=340, anchor="center")

quitB = Button(scoreCard, text= "QUIT", width= 15, height=2, borderwidth=5, relief="solid", bg="LemonChiffon", command= lambda: board.destroy())
quitB.place(x=150, y=820, anchor="center")

now = Label(scoreCard, width = 100, height = 4, bg="Orange", fg="Black" ,text="Roll Dice",font=('Times', '25'))
now.place(x=150, y= 480+170, anchor="center")

flag=False
pt = []

def turnvChange():

    global turnV,pt
    k = len(pt)-1

    if pt[k-1]!=6:
        pt=[] 
    

def roll(btn):

    global num,roll,pt
    num = randint(1,6)
    rollB.config(state = "normal")

    if num == 1:
        Flag=True
        btn.configure(image=dimage1)
        pt.append(1)
        now.configure(text= "Roll Dice", font=('Times', '20'))
        k = len(pt)-1

        if pt[k-1]!=6:
            pt=[] 
        #rollB.config(state=DISABLED)

    elif num==2:
        Flag=True
        btn.configure(image=dimage2)
        pt.append(2)
        now.configure(text= "Roll Dice", font=('Times', '20'))
        k = len(pt)-1

        if pt[k-1]!=6:
            pt=[] 
        #rollB.config(state=DISABLED)

    elif num==3:
        Flag=True
        btn.configure(image=dimage3)
        pt.append(3)
        now.configure(text= "Roll Dice", font=('Times', '20'))
        k = len(pt)-1

        if pt[k-1]!=6:
            pt=[] 
        
        #rollB.config(state=DISABLED)

    elif num==4:
        Flag=True
        btn.configure(image=dimage4)
        pt.append(4)
        now.configure(text= "Roll Dice", font=('Times', '20'))
        k = len(pt)-1

        if pt[k-1]!=6:
            pt=[] 
        #rollB.config(state=DISABLED)

    elif num==5:
        Flag=True
        btn.configure(image=dimage5)
        pt.append(5)
        now.configure(text= "Roll Dice", font=('Times', '20'))
        k = len(pt)-1

        if pt[k-1]!=6:
            pt=[] 
        #rollB.config(state=DISABLED)

    elif num==6:
        btn.configure(image=dimage6)
        pt.append(6)
        now.configure(text= "Roll Dice", font=('Times', '20'))

        k = len(pt)-1

        if pt[k-1]!=6:
            pt=[] 
    if pt==[]:
        pointL.configure(text="Previous Dice Numbers")
    else:
        pointL.configure(text=str(pt))

i= 0

def move(bt):

    global pt,turnV,i
    temp = turnV
    while i <= len(turn):

        turnV=turn[i]

        if turnV == 'r':
            playerL.configure(text = "Active Player : RED")
            clrB.configure(bg='Red')
        elif turnV == 'g':
            playerL.configure(text = "Active Player : GREEN")
            clrB.configure(bg='Green')
        elif turnV == 'y':
            playerL.configure(text = "Active Player : YELLOW")
            clrB.configure(bg='Yellow')
        elif turnV == 'b':
            playerL.configure(text = "Active Player : BLUE") 
            clrB.configure(bg='Blue')

        var = bt.movement(bt)
        
        if var=='keep':
            break
        else:
            if turn[i] == 'b':
                i=0
            else:
                i+=1
                turnV= turn[i]
        
        if temp != turnV:
            pointL.configure(text = "")
            
        
class createbt:

    def __init__(self,color):
        
        if color=='r':

            self.img = ImageTk.PhotoImage(file= '/media/tanmay/DATA/Programs/LUDO GAME/redP.png')
            self.obj = Button(brd, image= self.img)
            self.obj.configure(bg="white")
        
        elif color=='g':

            self.img = ImageTk.PhotoImage(file= '/media/tanmay/DATA/Programs/LUDO GAME/greenP.png')
            self.obj = Button(brd, image= self.img)
            self.obj.configure(bg="white")
        
        elif color=='y':

            self.img = ImageTk.PhotoImage(file= '/media/tanmay/DATA/Programs/LUDO GAME/yellowP.png')
            self.obj = Button(brd, image= self.img)
            self.obj.configure(bg="white")
        
        elif color=='b':

            self.img = ImageTk.PhotoImage(file= '/media/tanmay/DATA/Programs/LUDO GAME/blueP.png')
            self.obj = Button(brd, image= self.img)
            self.obj.configure(bg="white")
        
        self.obj.config(command = lambda: move(self))
        self.stat = 'i'
        self.color=color
        if self.color == 'r':
            self.index = 1
            self.index_h = 0

        elif self.color == 'y':
            self.index = 27
            self.index_h = 26

        elif self.color == 'g':
            self.index = 14
            self.index_h = 13

        elif self.color == 'b':
            self.index = 40
            self.index_h = 39   

        self.cordinates = {
        'r' : [ (375,765),
                (375,710),
                (375,655),
                (375,600),
                (375,545),
                (320,485),
                (265,485),
                (210,485),
                (155,485),
                (100,485),
                (45,485),
                (45,430),
                (45,375),
                (100,375),
                (155,375),
                (210,375),
                (265,375),
                (320,375),
                (375,315),
                (375,260),
                (375,205),
                (375,150),
                (375,90),
                (375,35),
                (430,35),
                (485,35),
                (485,95),
                (485,150),
                (485,205),
                (485,265),
                (485,320),
                (545,375),
                (600,375),
                (655,375),
                (710,375),
                (765,375),
                (825,375),
                (825,430),
                (825,485),
                (765,485),
                (710,485),
                (655,485),
                (600,485),
                (545,485),
                (490,540),
                (490,595),
                (490,650),
                (490,710),
                (490,765),
                (490,820),
                (435,820),
                (375,820),
                (375,765)
            ]
    }

    def step(self):
        global index
        self.obj.place(x=self.cordinates['r'][self.index][0], y = self.cordinates['r'][self.index][1], anchor = 'nw')
        self.index=self.index+1    
 
    def movement(self,bt):
        global pt
        print(pt)
        global loc
        if bt.color == turnV :
            if (6 in pt) and self.stat=='i':
                h = pt.index(6)
                self.stat='m'
                self.obj.place(x=self.cordinates['r'][self.index_h][0],y=self.cordinates['r'][self.index_h][1], anchor="nw")
                
                try:
                    pt = pt[h+1:]

                except Exception:
                    pt = [0]
                
            elif self.stat=='m':
                h = 0
                if pt==[]:
                    return 'change'
                else:
                    for j in range(pt[h]):
                        self.step()

                try:
                    pt = pt[h+1:]

                except Exception:
                    pt = [0]
            if pt!=[]:
                return 'keep'
            else:
                return 'change'
        else :
            return 'keep'


image = ImageTk.PhotoImage(file="/media/tanmay/DATA/Programs/LUDO GAME/ludoBoard.png")
board_image = Label(brd, image=image)
board_image.place(relx=0.5,rely=0.5, relwidth =1, relheight=1, anchor="center")

greenP =  []
d=510

a= createbt('g')

greenP.append(createbt('g'))
greenP[0].obj.place(x=140,y=145, anchor="center")

greenP.append(createbt('g'))
greenP[1].obj.place(x=250,y=145, anchor="center")

greenP.append(createbt('g'))
greenP[2].obj.place(x=140,y=245, anchor="center")

greenP.append(createbt('g'))
greenP[3].obj.place(x=250,y=245, anchor="center")

yellowP = []

yellowP.append(createbt('y'))
yellowP[0].obj.place(x=140+d,y=145, anchor="center")

yellowP.append(createbt('y'))
yellowP[1].obj.place(x=250+d,y=145, anchor="center")

yellowP.append(createbt('y'))
yellowP[2].obj.place(x=140+d,y=245, anchor="center")

yellowP.append(createbt('y'))
yellowP[3].obj.place(x=250+d,y=245, anchor="center")

redP=[]

redP.append(createbt('r'))
redP[0].obj.place(x=140,y=145+d, anchor="center")

redP.append(createbt('r'))
redP[1].obj.place(x=250,y=145+d, anchor="center")

redP.append(createbt('r'))
redP[2].obj.place(x=140,y=245+d, anchor="center")

redP.append(createbt('r'))
redP[3].obj.place(x=250,y=245+d, anchor="center")

blueP = []

blueP.append(createbt('b'))
blueP[0].obj.place(x=140+d,y=145+d, anchor="center")

blueP.append(createbt('b'))
blueP[1].obj.place(x=250+d,y=145+d, anchor="center")

blueP.append(createbt('b'))
blueP[2].obj.place(x=140+d,y=245+d, anchor="center")

blueP.append(createbt('b'))
blueP[3].obj.place(x=250+d,y=245+d, anchor="center")

num=0

dimage1= ImageTk.PhotoImage(file = "/media/tanmay/DATA/Programs/LUDO GAME/d1.png")
dimage2= ImageTk.PhotoImage(file = "/media/tanmay/DATA/Programs/LUDO GAME/d2.png")
dimage3= ImageTk.PhotoImage(file = "/media/tanmay/DATA/Programs/LUDO GAME/d3.png")
dimage4= ImageTk.PhotoImage(file = "/media/tanmay/DATA/Programs/LUDO GAME/d4.png")
dimage5= ImageTk.PhotoImage(file = "/media/tanmay/DATA/Programs/LUDO GAME/d5.png")
dimage6= ImageTk.PhotoImage(file = "/media/tanmay/DATA/Programs/LUDO GAME/d6.png")

dice = Button(brd, image = dimage1)
dice.place(relx=0.5,rely=0.5,anchor="center")
    
board.mainloop()