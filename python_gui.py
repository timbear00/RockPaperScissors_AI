'''
python GUI programming test
'''
from tkinter import *



#GUI
root = Tk()
root.title("GUI Test")
root.geometry("800x500+400+200")

photo_rock = PhotoImage(file='rock.png')
btn_rock = Button(root, image = photo_rock)
btn_rock.pack()

photo_scissors = PhotoImage(file='scissors.png')
btn_scissors = Button(root, image = photo_scissors)
btn_scissors.pack()

photo_paper = PhotoImage(file='paper.png')
btn_paper = Button(root, image = photo_paper)
btn_paper.pack()

root.mainloop()