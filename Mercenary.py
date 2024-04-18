import time

class Mercenary:
    def __init__ (self, name, years, health):
        self.name = name
        self.years = years
        self.health = health

print("К Вашему дому подъехали наёмники, выберите кого-либо чтобы убить его.")

killing = []

mercenary = {
    "Henry": Mercenary(name = "Henry", years = 24, health = 100),
    "Jacob": Mercenary(name = "Jacob", years = 31, health = 105),
    "Michael": Mercenary(name = "Michael", years = 29, health = 100)
        
}

def mercenary_killing():
    while len(mercenary) > 0:
        mercenary_kill = input("Choose mercenary to kill him: ")
        if mercenary_kill in mercenary:
            print("You killing " + mercenary_kill)
            killing.append(mercenary_kill)
            del mercenary[mercenary_kill]
            if len(mercenary) == 0:
                print("All mercenary have been killed")
        else:
            print("No such mercenary")
            
def choose_mercenary():
    mercenary_name = input("Enter mercenary name: ")
    if mercenary_name in mercenary:
        chosen_mercenary = mercenary[mercenary_name]
        print(f"Name: {chosen_mercenary.name}, Years: {chosen_mercenary.years}, Health: {chosen_mercenary.health}")
    else:
        print("No mercenary")


def kill_list():
    print(", ".join(killing) + " ✓")
    print(len(killing))

def information():
    while True:
        print("1. Information about mercenary")
        print("2. Killing mercenary")
        print("3. Your kill list")
        print("4. Exit")
        choice = input("Choise you action: ")
        if choice == '1':
            choose_mercenary()
        elif choice == '2':
            mercenary_killing()
        elif choice == '3':
            kill_list()      
        elif choice == '4':
            break
        else:
            print("Not correct choice")

information()

