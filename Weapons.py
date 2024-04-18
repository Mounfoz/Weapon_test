import time
import sys

class Weapons(): #Данные о оружиях
    def __init__(self, name = None, created = None, ammo = None, rof = None, ammunation = None, recharge = None, range = None, damage = None): #rof - rate of fire 
        self.name = name
        self.created = created
        self.range = range
        self.ammo = ammo
        self.rof = rof
        self.ammunation = ammunation
        self.recharge = recharge
        self.damage = damage


    def fire(self, distance_meter): 
        if self.range >= distance_meter: #Если range больше дистанции
            shots_fired = 0
            while self.ammo > 0: #Пока количество патронов больше нуля
                shots_fired += 1 #Добавляет +1 выстрел при каждой итерпретации 
                print (f"shoot doing ({shots_fired})") #Выводит сообщение о удачном выстреле и количеству выстрелов
                self.ammo -= 1  #Уменьшает патрон на 1
                time.sleep (self.rof) #Время между следующим выстрелом
            if self.ammo == 0: #Если количество патронов = 0, заканчивает стрельбу
                print("Ammo is out")
        else:
            print("Target is out of range")


weapons = {
    "carcano": Weapons(name = "carcano", created = 1891, ammo = 6, rof = 2, ammunation = 18, recharge = 2.0, range = 2000, damage = 75),
    "springfield": Weapons(name = "springfield", created = 1903, ammo = 5, rof = 2, ammunation = 15, recharge = 1.75, range = 2700, damage = 80),
    "browning m2": Weapons(name = "browning m2", created = 1921, ammo = 100, rof = 0.15, ammunation = 250, recharge = 3.5, range = 2000, damage = 50),
    "type38": Weapons(name = "type38", created = 1905, ammo = 5, rof = 3, ammunation = 15, recharge = 2.25, range = 1920, damage = 80),
    "Lee Enfield": Weapons(name = "Lee Enfield", created = 1902, ammo = 5, rof = 1.75, ammunation = 15, recharge = 1.75, range = 1829, damage = 70),
    "Thompson": Weapons(name = "Thompson", created = 1918, ammo = 30, rof = 0.10, ammunation = 90, recharge = 4, range = 100, damage = 75)
}

def select_weapon(weapon_name): #Функция для оружия
    if weapon_name in weapons: #Если оружие есть в weapons выбираем его
        return weapons[weapon_name] #Возвращает weapons
    else: #Если такого оружия нет - вводим нужное сообщение
        print ("This weapon not find")

weapon_name = input("What you weapon? ")
selected_weapon = select_weapon(weapon_name)

if selected_weapon: #если оружие выбрано
    distance_meter = int(input("Enter target distance: "))
    fire_choice = input("Shoot? (yes or not?) ") #Выстрелить или отказаться
    if fire_choice.lower() == "yes": #Согласие
        selected_weapon.fire(distance_meter) #выполнение функции выбранным оружием
else:
    print("Your don't shoot")



