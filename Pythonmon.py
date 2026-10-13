import random

def PressToContinue():
    return input("Press Enter to continue...")

def EnemyEncounter(money):
    print("You hear the rustling of leaves and the distant calls of unknown creatures.")
    PressToContinue()

    print("Pearbook: ALERT! You encounter an enemy in the forest!")
    PressToContinue()

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
        PressToContinue()
        print("Pearbook: You successfully escaped from the battle! but you tripped and fell and lost some money.")
        money -= random.randint(1, 10)
        print(f"Pearbook: You now have ${money}.")
        PressToContinue()

    return money


money = 25
def StartingScene():
    print("You hear your alarm go off.")
    PressToContinue()
    print("its 7:10 AM\nThe big day is finally here.\nDr. Oc is preparing the Pythonmons this second!")
    PressToContinue()
    print("You dont want to miss out! Especially for this one time event!")
    PressToContinue()

    print("You get ready and rush out the door while your mom gets your breakfest ready")
    PressToContinue()

    print("You head to the pythonmon observatory lab")
    PressToContinue()
    print("Along the way you notice the whole road filled with people cheering and walking to the same observatory")
    PressToContinue()
    print("You finally reach the observatory, the crowd buzzing with excitement")
    PressToContinue()

    print("You show the entrance man your ticket and he nods, letting you through")
    PressToContinue()
    print("You step inside the observatory, the grandeur of the place taking your breath away")
    PressToContinue()
    print("You notice a group of children playing with their Pythonmons, the sound of their laughter echoing through the hall")
    PressToContinue()
    print("You feel a mix of excitement and anticipation as you approach the main stage, where you expect Dr. Oc to be preparing the Pythonmons")
    PressToContinue()

    print("However when you get there you realize-")
    PressToContinue()
    print("No one but Dr. Oc is present on the stage, wrapping up on the preparations")
    PressToContinue()

    print("You feel a mix of confusion and disappointment as you try to process the situation")
    PressToContinue()

    print("Dr. Oc: \"Ah, you're finally here. I was wondering when you'd arrive.\"")
    PressToContinue()
    print("Dr. Oc: \"But I must say, you're a bit late.\"")
    PressToContinue()
    print("Dr. Oc: \"All of our Pythonmons have been already claimed.\"")
    PressToContinue()
    print("Dr. Oc: \"However we do have this prototype one left, he is extremely hostile to anyone.\"")
    PressToContinue()
    print("Dr. Oc: \"Are you sure you want to claim, it...?\"")
    PressToContinue()
    print("You hesitate for a moment, weighing the risks and the flex of claiming the risky Pythonmon")
    PressToContinue()


    Choice1 = input("Do you really want to claim the Pythonmon? (yes/no): ").lower()

    if Choice1 == "yes":
        print("Dr. Oc: \nVery well ketchup, lets proceed.")

    elif Choice1 == "no":
        print("Dr. Oc: \"I see... well, maybe next time. 'cough' Next Year.\"")
        print("Game over, you just had to give up your chance...")
        exit()

    else:
        print("Dr. Oc: \"Ash lets not waste time, your getting it anyway..\"")


    print("+1 Pythonmon gained, species R A T\nbehaviors, hostile, curious, abnormal.\nCombat Skills: B+ - A\nCodeName: Pythachu")

    print("Dr. Oc: \"Congratulations on your first Pythonmon!\"")
    PressToContinue()
    print("Dr. Oc: \"I trust you will take good care of it.\"")
    PressToContinue()
    print("Dr. Oc: \"Good luck on your journey!\"")
    PressToContinue()
    print("Dr. Oc: \"And Remember to use your School PearBook wisely!\"")
    print("You leave the observatory with your new Pythonmon, feeling a mix of pride and responsibility!")
    PressToContinue()
    print("As you step outside, you start to embark on your brand new journey with your new Pythonmon by your side.")
    PressToContinue()

StartingScene()


print("Pearbook: You are now walking inside the vast forest of herestia...")
PressToContinue()

print("Pearbook: Remember player, our main goal right now is to find the city bus stop and head for the city.\n then we can get started on fighting other Pythonmon Trainers!")
PressToContinue()

money = EnemyEncounter(money)

print("You continue walking down the forest, looking for any pathways")

money = EnemyEncounter(money)

print("You finally start seeing some sort of cobblestone in the near distance")
PressToContinue()
print("Pearbook: You are getting closer to the city bus stop!")
PressToContinue()

money = EnemyEncounter(money)

print("You finally reach the city bus stop!")
PressToContinue()
print("Pearbook: Oh no! to your right there is an enemy in that bush I hear!")

money = EnemyEncounter(money)

print("Pearbook: Finally we have made it perfectly on time to the city bus stop!")
PressToContinue()

print("Bus Driver: \"Welcome to the city bus! Please pay your fare and enjoy the ride.\"")
PressToContinue()
print("The Fare for the city bus is $10.")
if money >= 10:
    print("You pay the fare and board the city bus.")
    print("Pearbook: Now  that we are on the city bus, we can finally start our journey as a Pythonmon Trainer!\n We are gonna rule em all!!")

else:
    print("Pearbook: You do not have enough money to pay the fare. You cannot board the city bus.")
    PressToContinue()
    print("Game over, you cannot continue your pythonmon journey... :(")
    exit()

print("Thank you for playing Pythonmon!")
print("This game is really simple but it was a lot of fun using my brain creatively!")