# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#python ./dice.py
import sys
import random

def getMines(mines, rows, column):
    list_mines=[]
    for i in range(mines):
        a=random.randint(1,rows)
        b=random.randint(1, column)
        if [a,b] not in list_mines:
            list_mines.append([a,b])
        else:
            i-=1
    
    return list_mines

def getNumbers(mines_list, rows, columns):
    N={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            a=0
            if [i+1,j] in mines_list:
                a+=1
            if [i , j+1 ] in mines_list:
                a+=1
            if [i+1 , j+1 ] in mines_list:
                a+=1
            if [i -1, j ] in mines_list:
                a+=1
            if [i , j-1 ] in mines_list:
                a+=1
            if [i -1, j -1] in mines_list:
                a+=1
            if [i +1, j-1 ] in mines_list:
                a+=1
            if [i -1, j+1 ] in mines_list:
                a+=1
            N[a].append([i,j])
    return N

def endGame():
    global a
    a=0
    return a
    
rows=int(input('how many rows? '))
columns = int(input('how many columns? '))
num_mines = int(input('how many mines? '))
mines_list=getMines(num_mines,rows,columns)
number_list = getNumbers(mines_list,rows, columns)
if rows*columns<num_mines:
    print('mines more than blocks')
    sys.exit()
flaged=[]
opened=[]
for i in range(rows+1):
    opened.append([])
    for j in range(columns+1):
        opened[i].append(9)
a=1
for i in range(rows+1):
    for j in range(columns+1):
        if i==0:
            print(str(j)+' ', end='')
        else:
            if j==0:
                print(str(i)+' ',end='')
            else:
                if [i,j] in flaged:
                    print('! ', end='') 
                elif opened[i][j] != 9 :
                    print(opened[i][j], end='')
                else:
                    print('P ', end='')
    print('')
while a:
    action = input('exit = press any key or click=1 or flag=2? ')
    if action != '1' and action != '2':
        action=input('Do you really want to exit? Yes = 1 ')
        if action!='1':
            pass
        else:
            sys.exit()
    row = int(input('row '))
    column = int(input('column '))
    if action == '2':
        flaged.append([row,column])
    elif action == '1':
        if [row, column] in mines_list:
            opened[row][column]='B '
            endGame()
        else:
            for i in range(9):
                if [row,column] in number_list[i]:
                    opened[row][column]=str(i)+' '
                    break
    for i in range(rows+1):
        for j in range(columns+1):
            if i==0:
                print(str(j)+' ', end='')   
            else:
                if j==0:
                    print(str(i)+' ',end='')
                else:
                    if [i,j] in flaged:
                        print('! ', end='')
                        
                    elif opened[i][j] != 9 :
                        print(opened[i][j], end='')
                    else:
                        print('P ', end='')
        print('')
print('the end')
    