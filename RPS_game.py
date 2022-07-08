'''
python Rock Paper Scissors Game (GUI)
'''
from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter.font import families

import pandas as pd
import random

values = [
    [0,0,0],    # 가위 0
    [0,0,0],    # 바위 1
    [0,0,0]     # 보   2
]

player_input = 1
previous_input = 0

user_win = 0
com_win = 0
win_rate = 0
count=0

index = ['가위', '바위', '보']

def RSP(user_input) :
    global user_win
    global com_win
    global count
    global previous_input

    if count==0 :
        com = random.randrange(0, 3)
    else :
        com = com_decision(values, previous_input)
        values[previous_input][user_input] += 1

    previous_input = user_input
    res = judge(user_input, com)

    if (user_win+com_win)==0 :
        win_rate = 0
    else :
        win_rate = round(com_win / (user_win+com_win) * 100, 2)

    label_winrate.config(text=f'Player Win : {user_win} / Computer Win : {com_win} / Win Rate : {win_rate}% ({count})')
    label_select.config(text=f'Player : {index[user_input]}, Computer : {index[com]}')   
    label_result.config(text=f'Result : {res}')

    matrix11.config(text=str(values[0][0]))
    matrix12.config(text=str(values[0][1]))
    matrix13.config(text=str(values[0][2]))

    matrix21.config(text=str(values[1][0]))
    matrix22.config(text=str(values[1][1]))
    matrix23.config(text=str(values[1][2]))

    matrix31.config(text=str(values[2][0]))
    matrix32.config(text=str(values[2][1]))
    matrix33.config(text=str(values[2][2]))

def com_decision(data, pre_user) :
    next = data[pre_user].index( max(data[pre_user]) )

    if next==0 :
        return 1
    elif next==1 :
        return 2
    else :
        return 0
    

def judge(player, com) :
    global count 
    global user_win
    global com_win

    count += 1
    if(player==com) :
        return '비김'
    elif( (player==0 and com==2) or ( player==1 and com==0 ) or (player==2 and com==1) ) :
        user_win += 1
        return '승리'
    else :
        com_win+= 1
        return '패배'

def rock() :
    #label_select.config(text="Player : rock")
    RSP(1)

def paper() :
    #label_select.config(text="Player : paper")
    RSP(2)

def scissors() :
    #label_select.config(text="Player : scissors")
    RSP(0)


#Gui
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("800x500+400+200")

# Title Text
label_title = Label(root, text = 'Rock Paper Scissors Game', width=50, height=1, font=('Arial', 35))
label_title.pack()

# label1
label_winrate = Label(root, text = 'Player win : 0 / Computer win : 0 / Win Rate : 0.00%', font=('Arial', 15))
label_winrate.pack(pady=20)

# Label2
label_select = Label(root, text='Player : -, Computer : -', font=('Arial',15))
label_select.pack(pady=20)

# Label3
label_result = Label(root, text='Result : --', font=('Arial', 30, 'bold'))
label_result.pack(pady=10)

# 가위바위보 버튼
photo_rock = PhotoImage(file='rock.png')
btn_rock = Button(root, image = photo_rock, width=150, height=150, command=rock)            # 바위
btn_rock.place(x=160, y=380, anchor='center')

photo_paper = PhotoImage(file='paper.png')
btn_paper = Button(root, image = photo_paper, width=150, height=150, command=paper)           # 보
btn_paper.place(x=400, y=380, anchor='center')

photo_scissors = PhotoImage(file='scissors.png')
btn_scissors = Button(root, image = photo_scissors, width=150, height=150, command=scissors)     # 가위
btn_scissors.place(x=640, y=380, anchor='center')

matrix11 = Label(text='0', font=('Arial', 15))
matrix11.place(x=600, y=160, anchor='center')
matrix12 = Label(text='0', font=('Arial', 15))
matrix12.place(x=650, y=160, anchor='center')
matrix13 = Label(text='0', font=('Arial', 15))
matrix13.place(x=700, y=160, anchor='center')

matrix21 = Label(text='0', font=('Arial', 15))
matrix21.place(x=600, y=200, anchor='center')
matrix22 = Label(text='0', font=('Arial', 15))
matrix22.place(x=650, y=200, anchor='center')
matrix23 = Label(text='0', font=('Arial', 15))
matrix23.place(x=700, y=200, anchor='center')

matrix31 = Label(text='0', font=('Arial', 15))
matrix31.place(x=600, y=240, anchor='center')
matrix32 = Label(text='0', font=('Arial', 15))
matrix32.place(x=650, y=240, anchor='center')
matrix33 = Label(text='0', font=('Arial', 15))
matrix33.place(x=700, y=240, anchor='center')


root.mainloop()
