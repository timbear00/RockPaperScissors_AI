'''
python Rock Paper Scissors Game (GUI)
1번째와 2번째 전 플레이어의 선택을 고려하는 AI
'''
from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter.font import families

import pandas as pd
import random

# value: 3*3의 2차원 마르코프 행렬, index값 0은 가위, 1은 바위, 2는 보
values = [ 
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
]

player_input = 1    # 현재 선택
pre1_input = 0      # 1번째 전 선택
pre2_input = 0      # 2전째 전 선택

user_win = 0 # 사용자가 이긴 판 수
com_win = 0 # 컴퓨터가 이긴 판 수
win_rate = 0 # 컴퓨터의 승률
count = 0 # 진행된 판 수

index = ['가위', '바위', '보']

def RSP(user_input) :
    global user_win
    global com_win
    global count
    global win_rate
    global pre1_input
    global pre2_input

    if count==0 or count==1 :
        com = random.randrange(0, 3) # 첫 판이면 컴퓨터는 랜덤으로 냄
    else :
        com = com_decision(values, pre1_input, pre2_input)
        values[pre2_input][pre1_input][user_input] += 1

    res = judge(user_input, com)        # 승패 판단

    if (user_win+com_win)==0 :
        win_rate = 0
    else :
        win_rate = round(com_win / (user_win+com_win) * 100, 2)

    if __name__ == '__main__' :
        label_winrate.config(text=f'Player Win : {user_win} / Computer Win : {com_win} / Win Rate : {win_rate}% ({count})')
        label_select.config(text=f'Player : {index[user_input]}, Computer : {index[com]}')   
        label_result.config(text=f'Result : {res}')

        label_values[pre2_input][pre1_input][user_input].config(text=str(values[pre2_input][pre1_input][user_input]))
    
    pre2_input = pre1_input
    pre1_input = user_input
    

def com_decision(data, pre1_user, pre2_user) :
    next = data[pre2_user][pre1_input].index( max(data[pre2_user][pre1_user]) )

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
    
    win_num = (com + 1) % 3 # 사용자가 컴퓨터를 이기는 값
    
    count += 1
    
    if(player == com) :
        return '비김'
    elif(player == win_num) :
        user_win += 1
        return '승리'
    else :
        com_win += 1
        return '패배'

def rock() :
    RSP(1)

def paper() :
    RSP(2)

def scissors() :
    RSP(0)

def get_test_result_and_reset() :
    global user_win
    global com_win
    global count
    global win_rate
    test_result = [user_win, com_win, count, win_rate]
    
    values = [ 
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    ]

    player_input = 1    
    pre1_input = 0      
    pre2_input = 0      
    user_win = 0 
    com_win = 0 
    win_rate = 0 
    count = 0 

    return test_result


if __name__ == '__main__' :
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

    # Values 행렬 나타내는 Label
    label_scissors = Label(text='scissors', font=('Arial', 10)).place(x=570, y=140, anchor='center')
    label_rock = Label(text='rock', font=('Arial', 10)).place(x=645, y=140, anchor='center')
    label_paper = Label(text='paper', font=('Arial', 10)).place(x=720, y=140, anchor='center')

    label_values = [
            [ [ Label(text='0', font=('Arial', 10)) for a in range(0, 3) ] for b in range(0, 3) ] for c in range(0, 3)
        ]

    for i in range(0, 3) :
        for j in range(0, 3) :
            for k in range(0, 3) :
                label_values[i][j][k].place(x=550+(k*20)+(i*75), y=160+(j*20), anchor='center')


    root.mainloop()
