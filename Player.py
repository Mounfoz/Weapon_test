import sys
import time

class Player:
    def __init__ (self, name = None , health = None, wound = None, conscious = None):
        self.name = name
        self.health = health
        self.wound = wound
        self.conscious = conscious


class Body_armors:
    def __init__ (self, armor = None, protection = None):
        self.armor = armor
        self.protection = protection


def create_name():
    player_name = input("What your name? ")
    return Player(name=player_name)

player = create_name()
print("Your name is " + player.name)

Player_health = 100
player.wound = True

body_armors = {
      "small": Body_armors(armor = 50, protection = 25),
      "medium": Body_armors(armor = 75, protection = 50), 
      "large": Body_armors(armor = 100, protection = 75 )


}




def body_armor(bodyarmor_name):
    if bodyarmor_name in body_armors:
        print("The body armor you have chosen" + body_armors)
        print (body_armors[bodyarmor_name])       
    else:
        print("Your don't choose body armor")

def player_health_check(Player_health):
    if Player_health <= 0:
        print (player.name + ", Your die")
    sys.exit()

player_health_check(Player_health)
body_armor()


