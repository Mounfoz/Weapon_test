import time
import sys

class Food():
    def __init__(self, name, type, regeneration, et): #et - eating time
        self.naming = name
        self.type = type
        self.regeneration = regeneration
        self.et = et

foods = {
"meat": Food(name = "meat", type = "meat", regeneration = 1.0, et = 10),
"water": Food(name = "water", type = "water", regeneration = 2.0, et = 3),
"fried meat": Food(name = "fried meat", type = "meat", regeneration = 3.5, et = 10)
}


def eating(food_name): 
    if food_name in foods:
        print(food_name + " annihilated...")
        time.sleep(foods[food_name].et)
        print(food_name + " annihilated")
        return foods[food_name]       
    else:
        print("It's food not find")


def choose_food():
    food_names = input("Enter food: ")
    if food_names in foods:
        chosen_food = foods[food_names]
        print(f"Name: {chosen_food.naming}, Type: {chosen_food.type}, Regeneration: {chosen_food.regeneration}, Eating time: {chosen_food.et}")
    else:
        print("Not correct Food")

def selected_action():
    while True:
        print("1. Information about food")
        print("2. Eating food")
        print("3. exit")
        choose = input("choose your action: ")
        if choose == '1':
            choose_food()
        elif choose == '2':
            food_name = input("what your food? ")
            eating(food_name)
        elif choose == '3':
            break
        else:
            print("Not correct action")

selected_action()
