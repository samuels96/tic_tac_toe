# -*- coding: utf-8 -*-
import os
import sys
from builtins import input
from random import randint
from colorama import init
from colorama import Fore

init()

class Board():
    def __init__(self):
        self.cells = [" " for x in range(9)]

    def update(self,num,player,single=False):
        if self.cells[num-1] != " ":
            if single == True:
                return player_move("X",single)
            if player == "X":
                return player_move("X",single)
            else:
                return player_move("O",single)
        else:
            self.cells[num-1] = player
            return

    def win_check(self,player):
        for row in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            res = True
            for n in row:
                if self.cells[n] != player:
                    res = False
            if res == True:
                for x in row:
                    self.cells[x] = Fore.GREEN+self.cells[x]+Fore.WHITE
                refresh()
                return True

        return False

    def result(self):
        if board.win_check("X"):
            print ("\n\t\t     Player X wins the game.\n")
            repeat()

        if board.win_check("O"):
            print ("\n\t\t     Player O wins the game.\n")
            repeat()

        if " " not in board.cells:
            print("\n\t\t\t      Tie!")
            repeat()


    def display(self):
        print("\n  Numeric cell representation")
        print ("\t╔═══╦═══╦═══╗")
        print ("\t║ {} ║ {} ║ {} ║".format((1),(2),(3)))
        print ("\t╠═══╬═══╬═══╣")
        print ("\t║ {} ║ {} ║ {} ║".format((4),(5),(6)))
        print ("\t╠═══╬═══╬═══╣")
        print ("\t║ {} ║ {} ║ {} ║".format((7),(8),(9)))
        print ("\t╚═══╩═══╩═══╝")

        print("\n\t\t\t  Tic-Tac-Toe")
        print ("\t\t\t ╔═══╦═══╦═══╗")
        print ("\t\t\t ║ {} ║ {} ║ {} ║".format((self.cells[0]),(self.cells[1]),(self.cells[2])))
        print ("\t\t\t ╠═══╬═══╬═══╣")
        print ("\t\t\t ║ {} ║ {} ║ {} ║".format((self.cells[3]),(self.cells[4]),(self.cells[5])))
        print ("\t\t\t ╠═══╬═══╬═══╣")
        print ("\t\t\t ║ {} ║ {} ║ {} ║".format((self.cells[6]),(self.cells[7]),(self.cells[8])))
        print ("\t\t\t ╚═══╩═══╩═══╝")


    def ai(self,player):
        c = [0,0,None]

        for row in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            for n in row:
                if self.cells[n] == "X":
                    c[0] += 1
                if self.cells[n] == "O":
                    c[1] += 1
                else:
                    if self.cells[n] == " ":
                        c[2] = n+1

            if (c[0] == 2 or c[1] == 2) and c[2] != None:
                return self.update(c[2],player)

            c = [0,0,None]




        if self.cells[4] == " ":
            return self.update(5,player)

        if randint(1,2)==1:
            for n in [1,3,4,6,7,9]:
                if self.cells[n-1]==" ":
                    return self.update(n,player)
        else:
            for n in range(9,0,-1):
                if self.cells[n-1]==" ":
                    return self.update(n,player)




    def reset(self):
        self.cells = [" " for x in range(9)]
        refresh()


def refresh():
    os.system('cls' if os.name == "nt" else "clear")
    board.display()

def main():

    single = False
    print("-"*18+"Tic-Tac-Toe"+"-"*18)
    print("\nDo you wish to play multiplayer or singleplayer?\n")
    while True:
        mode = input("Enter 1 for singleplayer, 2 for multiplayer > ")
        if mode not in ["1","2"]:
            print("Wrong input entered")
            continue
        else:
            print(mode)
            if mode == "1":
                single = True
            break

    while True:
        refresh()
        if os.name!="nt":
            os.system("clear")
        player_move("X",single)
        refresh()
        board.result()
        player_move("O",single)
        board.result()


def repeat():
    repeat = input("Enter Y if you want play again or N to quit > ")
    while True:
        if repeat in ["YES","yes","y","Y"]:
            board.reset()
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif repeat in ["NO","no","n","N"]:
            sys.exit(0)
        else:
            print("Wrong input entered")
            repeat = input("Enter Y if you want play again or N to quit > ")
            continue

def player_move(player,single):
    if single == True and player == "O":
        return board.ai("O")

    if " " not in board.cells:
        print("\n\t\t\t       Tie!")
        return repeat()
    print("\n\t\t\t|Player X turn|\n")

    x = (input("Enter number from 1-9, depending on which you want to place your {} > ".format(player)))
    while True:
        try:
            x = int(x)
            if x >= 1 and x <= 9:
                break
            else:
                x = int("error")
        except:
            print("Wrong number entered")
            x = (input("Enter number from 1-9, depending on which you want to place your {} > ".format(player)))
    if player == "X":
        board.update(x, "X") if single == False else board.update(x, "X",True)
    else:
        board.update(x, "O")


if __name__ == "__main__":
    board = Board()
    main()
