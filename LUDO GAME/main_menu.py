from tkinter import *
from PIL import ImageTk, Image

main = Tk()

main.geometry("1200x714")
main.title('LUDO')
main.resizable(width=False, height=False)

image = ImageTk.PhotoImage(file="/media/tanmay/DATA/Programs/LUDO GAME/maxresdefault.png")
back_image = Label(main, image=image)
back_image.place(relx=0.5,rely=0.5, relwidth =1, relheight=1, anchor="center")

def board():
    global main
    main.destroy()
    import board.py

label1= Label(main, text="LUDO", font= ('Times',56), fg="#f4ea17", bg="#ae3b20")
label1.config(width=100)
label1.place(relx=0.5, rely= 0.1, anchor="center")

btStart = Button(main, text= "START GAME", font= ('Arial', 20), command= lambda : board())
btStart.config(width=40, highlightbackground = "Black", highlightthickness = 8)
btStart.place(relx=0.5, rely=0.7, anchor="center")

btinstr = Button(main, text= "INSTRUCTIONS", font= ('Arial', 20))
btinstr.config(width=40, highlightbackground = "Black", highlightthickness = 8)
btinstr.place(relx=0.5, rely=0.8, anchor="center")

btquit = Button(main, text= "QUIT", font= ('Arial', 20))
btquit.config(width=40, highlightbackground = "Black", highlightthickness = 8, command = lambda: main.destroy())
btquit.place(relx=0.5, rely=0.9, anchor="center")

main.update()

print(btquit.winfo_y())

main.mainloop()