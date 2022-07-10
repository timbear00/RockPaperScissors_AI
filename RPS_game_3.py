'''
python Rock Paper Scissors Game (GUI)
이전 판단값과 이전 승패의 데이터로 사용자의 현재 판단값을 예측하는 가위바위보 알고리즘
'''

from cProfile import label
from cgitb import text
from msilib.schema import Font
from tkinter import *
from tkinter.font import families

#import pandas as pd
import random

# rsp_matrix: 3*3의 2차원 마르코프 행렬, index값 0은 가위, 1은 바위, 2는 보, 행은 이전 판단값, 열은 현재 판단값
rsp_matrix = [ 
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# res_matrix: 3*3의 2차원 마르코프 행렬, index값 0은 승리, 1은 패배, 2는 무승부, 행은 이전 승패, 열은 유저가 이전에 낸 것에 대해 유저가 현재 낸 것이 가지는 승패 결과
res_matrix = [ 
    [0,0,0],
    [0,0,0],
    [0,0,0]
]



previous_input = 0 # 유저 이전 입력값

previous_result = '승리' # 이전 승패
rel_value = 0 # 유저가 이전에 낸 것에 대해 유저가 현재 낸 것이 가지는 승패 결과

user_win = 0 # 사용자가 이긴 판 수
com_win = 0 # 컴퓨터가 이긴 판 수
win_rate = 0 # 컴퓨터의 승률
count = 0 # 진행된 판 수

rsp_index = ['가위', '바위', '보'] # GUI 구현 시 판단값을 문자열로 변환할 때에만 사용
res_index = ['승리', '패배', '무승부'] # GUI 구현 시 승패값을 문자열로 변환할 때에만 사용

def RSP(user_input) :
    global user_win
    global com_win
    global count
    global previous_input
    global previous_result

    if count==0 :
        com = random.randrange(0, 3) # 첫 판이면 컴퓨터는 랜덤으로 냄
    else :
        com = com_decision(rsp_matrix, res_matrix, previous_input, previous_result)
        rsp_matrix[previous_input][user_input] += 1
        res_matrix[previous_result][judge(user_input, previous_input)] += 1

    previous_input = user_input
    
    previous_result = judge(user_input, com) # 승패 판단

    if (previous_result == 0):
        user_win += 1
    elif (previous_result == 1):
        com_win += 1
    
    count += 1

    if (user_win + com_win) == 0 :
        win_rate = 0
    else :
        win_rate = round(com_win / (user_win+com_win) * 100, 2)

    label_winrate.config(text=f'Player Win : {user_win} / Computer Win : {com_win} / Win Rate : {win_rate}% ({count})')
    label_select.config(text=f'Player : {rsp_index[user_input]}, Computer : {rsp_index[com]}')
    label_result.config(text=f'Result : {res_index[previous_result]}')

    matrix11.config(text=str(rsp_matrix[0][0]))
    matrix12.config(text=str(rsp_matrix[0][1]))
    matrix13.config(text=str(rsp_matrix[0][2]))

    matrix21.config(text=str(rsp_matrix[1][0]))
    matrix22.config(text=str(rsp_matrix[1][1]))
    matrix23.config(text=str(rsp_matrix[1][2]))

    matrix31.config(text=str(rsp_matrix[2][0]))
    matrix32.config(text=str(rsp_matrix[2][1]))
    matrix33.config(text=str(rsp_matrix[2][2]))



# 마르코프 행렬과 유저의 이전 판단값을 매개변수로 받아서, 컴퓨터의 다음 판단값을 반환
def com_decision(rsp_matrix, res_matrix, previous_input, previous_result) :
    possibilities = [i * (j := res_matrix[previous_result][judge(previous_input,i)]) if j != 0 else 1 for i in rsp_matrix[previous_input]]
    return (possibilities.index(max(possibilities)) + 1) % 3



# a와 b, 두 판단값을 매개변수로 받아서 a의 승패를 판정 후 반환
def judge(a, b) :
    
    win_num = (b + 1) % 3 # a가 b를 이기는 값
    
    if(a == b) :
        return 2 # 무승부
    elif(a == win_num) :
        return 0 # 승리
    else :
        return 1 # 패배



def reverse_judge(result, a) :
    k = 1



def scissors() :
    #label_select.config(text="Player : scissors")
    RSP(0)

def rock() :
    #label_select.config(text="Player : rock")
    RSP(1)

def paper() :
    #label_select.config(text="Player : paper")
    RSP(2)



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

# rsp_matrix 행렬 나타내는 Label
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
