# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# n = input()
# n = n.split()
# f = ''.join((filter(lambda x: 'абв' not in x, n)))

# print(f)

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# string = input()
# count = 1
# for i in range(len(string) - 1):

#     if string[i] == string[i + 1]:
#         count += 1
#     else:
#         print(f'{count}x{string[i]}', end=' ')
#         count = 1
# print(f'{count}x{string[i + 1]}')

# Создайте программу для игры в ""Крестики-нолики"".

# from tkinter import *
# import random
# root = Tk()
# root.title('Крестики - Нолики')
# game_run = True
# field = []
# cross_count = 0

# def new_game():
#     for row in range(3):
#         for col in range(3):
#             field[row][col]['text'] = ' '
#             field[row][col]['background'] = 'lavender'
#     global game_run
#     game_run = True
#     global cross_count
#     cross_count = 0

# def click(row, col):
#     if game_run and field[row][col]['text'] == ' ':
#         field[row][col]['text'] = 'X'
#         global cross_count
#         cross_count += 1
#         check_win('X')
#         if game_run and cross_count < 5:
#             computer_move()
#             check_win('O')

# def check_win(smb):
#     for n in range(3):
#         check_line(field[n][0], field[n][1], field[n][2], smb)
#         check_line(field[0][n], field[1][n], field[2][n], smb)
#     check_line(field[0][0], field[1][1], field[2][2], smb)
#     check_line(field[2][0], field[1][1], field[0][2], smb)

# def check_line(a1,a2,a3,smb):
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb:
#         a1['background'] = a2['background'] = a3['background'] = 'pink'
#         global game_run
#         game_run = False

# def can_win(a1,a2,a3,smb):
#     res = False
#     if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ':
#         a3['text'] = 'O'
#         res = True
#     if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb:
#         a2['text'] = 'O'
#         res = True
#     if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb:
#         a1['text'] = 'O'
#         res = True
#     return res

# def computer_move():
#     for n in range(3):
#         if can_win(field[n][0], field[n][1], field[n][2], 'O'):
#             return
#         if can_win(field[0][n], field[1][n], field[2][n], 'O'):
#             return
#     if can_win(field[0][0], field[1][1], field[2][2], 'O'):
#         return
#     if can_win(field[2][0], field[1][1], field[0][2], 'O'):
#         return
#     for n in range(3):
#         if can_win(field[n][0], field[n][1], field[n][2], 'X'):
#             return
#         if can_win(field[0][n], field[1][n], field[2][n], 'X'):
#             return
#     if can_win(field[0][0], field[1][1], field[2][2], 'X'):
#         return
#     if can_win(field[2][0], field[1][1], field[0][2], 'X'):
#         return
#     while True:
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
#         if field[row][col]['text'] == ' ':
#             field[row][col]['text'] = 'O'
#             break
# for row in range(3):
#     line = []
#     for col in range(3):
#         button = Button(root, text=' ', width=4, height=2,
#                         font=('Verdana', 20, 'bold'),
#                         background='lavender',
#                         command=lambda row=row, col=col: click(row,col))
#         button.grid(row=row, column=col, sticky='nsew')
#         line.append(button)
#     field.append(line)
# new_button = Button(root, text='Новая игра', command=new_game)
# new_button.grid(row=3, column=0, columnspan=3, sticky='nsew')
# root.mainloop()

# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# ОТВЕТ: Первому  игроку  надо первым ходом забрать остаток от целочисленного деления
# имеющегося количества конфет на то, которое можно взять за 1 ход максимально + 1
# В дальнейшем первому игроку нужно повторять стратегию, хотя без калькулятора не всегда это удобно посчитать))))
# Пример :  2021 % ( 28 + 1 ) = 20 , первый игрок первым ходом должен взять 20 конфет.
# если вторым ходом второй игрок взял 10 конфет, то первый должен взять 28 + 1 - 10 = 19 и так далее..

# from random import *

# message = ['твоя очередь', 'да бери уже',
#            'бери', 'конфетки сладкие', 'возьми одну =)']

# candies_total = 2021
# max_take = 28
# count = 0
# player_1 = input('\nКак тебя зовут?: ')
# player_2 = input('\nА твоего соперника?: ')

# print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
# print('\nДля начала опеределим кто первый начнет игру.\n')

# x = randint(1, 2)
# if x == 1:
#     lucky = player_1
#     loser = player_2
# else:
#     lucky = player_2
#     loser = player_1
# print(f'Поздравляю {lucky} ты ходишь первым !')

# while candies_total > 0:
#     if count == 0:
#         step = int(input(f'\n{choice(message)} {lucky} = '))
#         if step > candies_total or step > max_take:
#             step = int(input(f'\nНе жадничай можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
#         candies_total = candies_total - step
#     if candies_total > 0:
#         print(f'\nна кону еще {candies_total}')
#         count = 1
#     else:
#         print('Все кончились конфетки')

#     if count == 1:
#         step = int(input(f'\n{choice(message)}, {loser} = '))
#         if step > candies_total or step > max_take:
#             step = int(input(f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
#         candies_total = candies_total - step
#     if candies_total > 0:
#         print(f'\nна кону еще {candies_total}')
#         count = 0
#     else:
#         print('Все кончились конфетки')

# if count == 1:
#     print(f'{loser} ПОБЕДИЛ!!!')
# if count == 0:
#     print(f'{lucky} ПОБЕДИЛ!!!')
