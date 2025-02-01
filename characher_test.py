from character import Character, Enemy

player_inventory = [1, 2, 3]

ivan = Enemy("Ivan", "A smelly zombie")
ivan.describe()

ivan.set_conversation("I am human ...")
print(ivan.talk())

ivan.set_weakness("cheese")

fight_with = input("What are you going to fight with?: ")
print(ivan.fight(fight_with))


print(player_inventory)