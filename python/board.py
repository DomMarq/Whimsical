#!/usr/bin/python3
import random
# from card import Card

class Board:
    def __init__(self):
        self.board = []
        for i in range(6):
            temp = []
            for j in range(6):
                temp.append(None)
            self.board.append(temp)

    def place_cards(self, stack):
        placed = False
        for card in stack.get_stack():
            placed = False
            while placed == False:
                x = random.randrange(6)
                y = random.randrange(6)
                if self.board[y][x] == None:
                    self.board[y][x] = card
                    placed = True
<<<<<<< HEAD
                    # print("Placed: \n{}\n".format(card.stringify()))
=======
                    print("Placed: \n{}\n".format(card.stringify()))
>>>>>>> 2b03632f83b1d06a77e5a20ccd8c2daf9c5cbd69

    def print_board(self):
        # print(self.board)
        for r in self.board:
            row = ''
            for c in r:
                if c:
                    row += '{:>8}'.format(c.id)
                else:
                    row += '{} '.format(c)

            print(row)
