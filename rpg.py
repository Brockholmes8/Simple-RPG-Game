import random
import sys
import os

print("What is your name, adventurer")
player_name = input()
print(f"Welcome, {player_name}, to Simple RPG")

while True:
    adventureClass = input("Choose your class: (1) Barbarian, (2) Knight, (3) Rogue: ")
    if adventureClass == "1":
        healthMax = 75 
        damage = 20
        speed = 8
        healRate = 10
        break
    elif adventureClass == "2":
        healthMax = 60
        damage = 15
        speed = 5
        healRate = 15
        break
    elif adventureClass == "3":
        healthMax = 50
        damage = 10
        speed = 3
        healRate = 20
        break
    else:
        print("Invalid input, please choose 1, 2, or 3.")

fightCnt = 0
runFlg = 0
fearFlg = 0
attackRoll = 0
guardRoll = 0
runRoll = 0
enemySpecRoll = 0
health = healthMax

while fightCnt < 5:
    enemyChoice = random.choice(["Sewer Rat", "Skeleton", "Zombie"])
    if enemyChoice == "Sewer Rat":
        enemyHealth = 25
        enemyDamage = 5
        enemySpeed = 3
        enemySpecial = "poison"
        enemyWeakness = "Rogue"
    elif enemyChoice == "Skeleton":
        enemyHealth = 35
        enemyDamage = 10
        enemySpeed = 5
        enemySpecial = "fear"
        enemyWeakness = "Cleric"
    elif enemyChoice == "Zombie":
        enemyHealth = 40
        enemyDamage = 12
        enemySpeed = 8
        enemySpecial = "heal"
        enemyWeakness = "Barbarian"

    os.system('clear' if sys.platform == 'darwin' else 'cls')
    print("You have encountered a " + enemyChoice + "!")
    print("Enemy Health: " + str(enemyHealth))
    escapedFlg = 0

    while enemyHealth > 0 and health > 0 and escapedFlg == 0:
        #Player Turn
        print("Your Turn: ")
        print("Player Health: " + str(health))
        while True and fearFlg == 0:
            playerChoice = input("(1) Attack, (2) Guard, (3) Run Away: ")
            os.system('clear' if sys.platform == 'darwin' else 'cls')
            if playerChoice == "1":
                attackRoll = random.randint(1, 20)
                if attackRoll < speed:
                    attackRoll = 0
                    print("You missed!")
                else: 
                    attackRoll = random.randint(1, damage)
                    print(f"You hit the {enemyChoice} for {attackRoll} damage!")
                break
            elif playerChoice == "2":
                guardRoll = random.randint(1, healRate)
                health += guardRoll
                if health > healthMax:
                    health = healthMax
                print(f"You healed yourself for {guardRoll} health!")
                break
            elif playerChoice == "3":
                runRoll = random.randint(1,20)
                if runRoll >= 12:
                    print("You have successfully ran away")
                    if health < healthMax:
                        health += (healthMax // 2)
                        if health > healthMax:
                            health = healthMax
                    print("Your health has been restored to " + str(health))
                    escapedFlg = 1
                else:
                    print("You have failed to run away")
                break
            else:
                print("Invalid input, please enter a valid number")
        
        if escapedFlg == 0:
            if adventureClass == "1" and enemyChoice == "Zombie":
                enemyHealth -= 2
                print("You dealt 2 points of bonus damage!")
            if adventureClass == "2" and enemyChoice == "Skeleton":
                enemyHealth -= 2
                print("You dealt 2 points of bonus damage!")
            if adventureClass == "3" and enemyChoice == "Sewer Rat":
                enemyHealth -= 2
                print("You dealt 2 points of bonus damage!")
        
        if enemyHealth <= 0:
            print("You have killed the " + enemyChoice)
            break
                        
        #Enemy Turn
        os.system('clear' if sys.platform == 'darwin' else 'cls')
        fearFlg = 0
        print(enemyChoice + "'s Turn: ")
        print("Enemy Health: " + str(enemyHealth))
        attackRoll = random.randint(1, 20)
        if attackRoll < enemySpeed:
            attackRoll = 0
            print(f"The {enemyChoice} missed!")
        else:
            attackRoll = random.randint(1, enemyDamage)
            health -= attackRoll
            if health < 0:
                health = 0
        print("The enemy dealt " + str(attackRoll) + " points of damage")
        specialRoll = random.randint(1,20)
        if specialRoll >= 15:
            if enemyChoice == "Sewer Rat":
                print("The enemy has poisoned you! 2 points of damage!")
                health -= 2
            if enemyChoice == "Skeleton":
                print("The enemy has frightened you! Lose your next turn!")
                fearFlg = 1
            if enemyChoice == "Zombie":
                print("The enemy has found its missing limb! It has healed to 5 points!")
                enemyHealth += 5
                if enemyHealth > 40:
                    enemyHealth = 40
    
        if health <= 0:
            print("You Died! Game Over!")
            sys.exit()
    
    fightCnt += 1

print("You have cleared the dungeon! You win!")
