import random
import PressToContinue

def EnemyEncounter(money):
    print("You hear the rustling of leaves and the distant calls of unknown creatures.")
    PressToContinue.PressToContinue()

    print("Pearbook: ALERT! You encounter an enemy in the forest!")
    PressToContinue.PressToContinue()

    choice = input("Pearbook: What will you do? \n1) Fight\n2) Run away!")

    if choice == "1":
        print("Pearbook: You chose to fight the enemy!")
        WinChance = random.choice([1, 2])
        if WinChance == 1:
            print("Pearbook: You win the battle!")
            money += random.randint(1, 8)
            print(f"Pearbook: You now have ${money}.")
        else:
            print("Pearbook: You lose the battle!")
            money -= random.randint(1, 5)
            print(f"Pearbook: You now have ${money}.")
    else:
        print("Pearbook: You chose to run away from the enemy!")
        PressToContinue.PressToContinue()
        print("Pearbook: You successfully escaped from the battle! but you tripped and fell and lost some money.")
        money -= random.randint(1, 10)
        print(f"Pearbook: You now have ${money}.")
        PressToContinue.PressToContinue()

    return money