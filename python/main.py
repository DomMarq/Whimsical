#!/usr/bin/python3
from card import Card
from card import CardStack
from board import Board


board = Board()
cards = CardStack("resources/cards.json")
# cards.print_stack()
board.print_board()
print()
board.place_cards(cards)
board.print_board()
