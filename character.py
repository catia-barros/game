class Character():

    #Creater Character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print(f"{self.name} is in this room!")
        print(self.description)

    # Set what this character will say when being talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to the character
    def talk(self):
        if self.conversation is not None:
            return f"[{self.name} says]: {self.conversation}"
        else:
            return f"[{self.name} doesn't want to talk to you]"

    # Fight with this chaaracter
    def fight(self, combat_item):
        return f"{self.name} doesn't want to fight you"
    

class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            return f"You have defeated {self.name} with the {combat_item}"
        else:
            return f"{self.name} has defeated you! Puny adventurer!"
        
    def set_bribe_amount(self, amount):
        self.set_bribe_amount = amount

    def get_bribe_amount(self):
        return self.bribe_amount
    
    def bribe(self, amount):
        if amount >= self.bribe_amount:
            return f"{self.name} has accepted your bribe and will let you pass."
        
        else:
            return f"{self.name} laughs at your attempt to bribe with such a small amount."
    
    def steal(self):
        return f"You stole an item from {self.name}!"
    
    def send_to_sleep(self):
        return f"{self.name} has been sent to sleep."

    def main():
        enemy = Enemy("A green creature with ugly feet!")
        enemy.set_weakness("Cheese")

        combat_item = "gun" 
        fight_result, survived = enemy.fight(combat_item)

        print(fight_result)
        if not survived:
            print("You looser!  :)")

    if __name__ == "__main__":
        main()