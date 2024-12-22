import os
from Player import player
from Enemy import enemy

#BUGGED
from Utilities import display_health as display_Hp


Hero = player(Hp= 100, MHp= 100, atk= 25)
enemies = []

for i in range(5):
    enemies.append(enemy(name= i, Hp= 50, MHp= 75, atk= 2))

run = True

while run:

    ## Drawing

    for enemy in enemies:
        if enemy.Hp <= 0:
            #enemies.remove(enemy)
            enemy.alive = False

    for enemy in enemies:
        if enemy.alive == True:
            print(f"{enemy.name +1}. ", enemy.Hp)
        else:
            print(f"{enemy.name +1}. ", "Dead")

    print("")

    print(f"Your Health : {Hero.Hp}/{Hero.MHp}")


    while True:
        print("What do you want to do? \n1. Attack\n2. Heal")
        choice = input("> ")
        if choice == "1":
            while True:
                target = int(input(f"Which enemy would you like to attack from {len(enemies)} : "))
                if target <= len(enemies) and target > 0:
                    break
                else:
                    print("Invalid Input")
                    os.system("pause")
            Hero.attack(enemies[target -1])

            break
        elif choice == "2":
            Hero.heal()
            break
        else:
            print("Invalid choice")
            os.system("pause")

    for enemy in enemies:
        if enemy.alive:
            enemy.attack(Hero)