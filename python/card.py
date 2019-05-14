#!/usr/bin/python3
import json
import random

class Card:
    def __init__(self, name="", house="", id=0, house_id=0):
        self.name = name
        self.house = house
        self.id = id
        self.house_id = house_id

    def stringify(self):
        return "Name: {}\nHouse: {}\nID: {}\nHouse_ID: {}".format(self.name, self.house, self.id, self.house_id)


class CardStack:
    def __init__(self, filename):
        self._stack = []
        self.load_stack(filename)
        self.shuffle_stack()

    def load_stack(self, filename):
        f = open(filename, mode="r")
        cards = json.load(f)
        for card in cards:
            name = card["name"]
            house = card["house"]
            id = card["id"]
            house_id = card["house_id"]
            self._stack.append(Card(name, house, id, house_id))

    def shuffle_stack(self):
        random.shuffle(self._stack)

    def print_stack(self):
        for card in self._stack:
            print(card.stringify())
            print()

    def get_stack(self):
        return self._stack
