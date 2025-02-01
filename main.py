from room import Room
from character import Enemy, Character

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate golden decorations")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

library = Room("Library")
library.set_description("A quiet place filled with old, dusty books")

dining_hall.link_room(library, "north")
library.link_room(dining_hall, "south")

sarah = Enemy("Sarah", "Acunning thief")
sarah.set_conversation("Shhhh ... I am busy at the moment")
sarah.set_weakness("pizza")

library.set_character(sarah)

ivan = Enemy("Dave", "A smelly zoombie")
ivan.set_conversation("Brrlgrh... rgrhl..., I am human")
ivan.set_weakness("cheese")

dining_hall.set_character(ivan)

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    
    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)

    elif command == "talk" and inhabitant is not None:
        inhabitant.talk()

    elif command == "fight" and inhabitant is not None:
        print("What will you fight with?")
        fight_with = input()
        if inhabitant.fight(fight_with)
            print("Congratulations, you won the fight!")
            current_room.set_character(None)
            
        else:
            print("Looseerrrrrrrrr!!! Ahahahahaha!")
            print("Game Over!")
            break

    elif command == "bribe" and inhabitant is not None:
        print("How much will you bribe with?")
        bribe_amount = int(input())
        print(inhabitant.bribe(bribe_amount))

    elif command == "steal" and inhabitant is not None:
        print(inhabitant.steal())

    elif command == "sleep" and inhabitant is not None:
        print(inhabitant.send_to_sleep())