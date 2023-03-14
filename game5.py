class Room:
    def __init__(self, name, dict_rooms = {}):
        self.name = name
        self.dict_rooms = dict_rooms
        self.character = None
        self.item = None
        self.description = None

    def set_description(self, description):
        self.description = description

    def link_room(self, other, direction):
        self.dict_rooms[direction] = [other, self.name]

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, __o: object) -> bool:
        return self.name == __o

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def get_character(self):
        return self.character

    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.description)
        for i in list(self.dict_rooms.keys()):
            if self.dict_rooms[i][1] == self.name:
                print(f"The {self.dict_rooms[i][0]} is {i}")
        return ' '
    def move(self, direction):
        return self.dict_rooms[direction][0]

class Character:
    pass
class Friend(Character):
    pass
class Enemy(Character):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.counter = 0
    def set_conversation(self, phrase):
        self.phrase = phrase
    def set_weakness(self, weakness):
        self.weakness = weakness
    def get_description(self):
        return self.description
    def describe(self):
        print(f'{self.name} is here!')
        print(self.description)
    def talk(self):
        print(f"[{self.name} says]: {self.phrase}")
    def fight(self, with_f):
        self.fight = with_f == self.weakness
        self.counter += 1
        return self.fight
    def get_defeated(self):
        return counter

class Item:
    def __init__(self, item):
        self.item = item
    def set_description(self, description):
        self.description = description
    def describe(self):
        print(f'The [{self.item}] is here - {self.description}')
    def get_name(self):
        return self.item

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up, dude! I'm hungry.")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

cheese = Item("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

current_room = kitchen
backpack = []

dead = False

while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                    if inhabitant.get_defeated() == 2:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)