import PressToContinue
import random
import EnemyEncounter


money = 25
def StartingScene():
    print("You hear your alarm go off.")
    PressToContinue.PressToContinue()
    print("its 7:10 AM\nThe big day is finally here.\nDr. Oc is preparing the Pythonmons this second!")
    PressToContinue.PressToContinue()
    print("You dont want to miss out! Especially for this one time event!")
    PressToContinue.PressToContinue()

    print("You get ready and rush out the door while your mom gets your breakfest ready")
    PressToContinue.PressToContinue()

    print("You head to the pythonmon observatory lab")
    PressToContinue.PressToContinue()
    print("Along the way you notice the whole road filled with people cheering and walking to the same observatory")
    PressToContinue.PressToContinue()
    print("You finally reach the observatory, the crowd buzzing with excitement")
    PressToContinue.PressToContinue()

    print("You show the entrance man your ticket and he nods, letting you through")
    PressToContinue.PressToContinue()
    print("You step inside the observatory, the grandeur of the place taking your breath away")
    PressToContinue.PressToContinue()
    print("You notice a group of children playing with their Pythonmons, the sound of their laughter echoing through the hall")
    PressToContinue.PressToContinue()
    print("You feel a mix of excitement and anticipation as you approach the main stage, where you expect Dr. Oc to be preparing the Pythonmons")
    PressToContinue.PressToContinue()

    print("However when you get there you realize-")
    PressToContinue.PressToContinue()
    print("No one but Dr. Oc is present on the stage, wrapping up on the preparations")
    PressToContinue.PressToContinue()

    print("You feel a mix of confusion and disappointment as you try to process the situation")
    PressToContinue.PressToContinue()

    print("Dr. Oc: \"Ah, you're finally here. I was wondering when you'd arrive.\"")
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"But I must say, you're a bit late.\"")
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"All of our Pythonmons have been already claimed.\"")
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"However we do have this prototype one left, he is extremely hostile to anyone.\"")
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"Are you sure you want to claim, it...?\"")
    PressToContinue.PressToContinue()
    print("You hesitate for a moment, weighing the risks and the flex of claiming the risky Pythonmon")
    PressToContinue.PressToContinue()


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
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"I trust you will take good care of it.\"")
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"Good luck on your journey!\"")
    PressToContinue.PressToContinue()
    print("Dr. Oc: \"And Remember to use your School PearBook wisely!\"")
    print("You leave the observatory with your new Pythonmon, feeling a mix of pride and responsibility!")
    PressToContinue.PressToContinue()
    print("As you step outside, you start to embark on your brand new journey with your new Pythonmon by your side.")
    PressToContinue.PressToContinue()

StartingScene()


print("Pearbook: You are now walking inside the vast forest of herestia...")
PressToContinue.PressToContinue()

print("Pearbook: Remember player, our main goal right now is to find the city bus stop and head for the city.\n then we can get started on fighting other Pythonmon Trainers!")
PressToContinue.PressToContinue()

money = EnemyEncounter.EnemyEncounter(money)

print("You continue walking down the forest, looking for any pathways")

money = EnemyEncounter.EnemyEncounter(money)

print("You finally start seeing some sort of cobblestone in the near distance")
PressToContinue.PressToContinue()
print("Pearbook: You are getting closer to the city bus stop!")
PressToContinue.PressToContinue()

money = EnemyEncounter.EnemyEncounter(money)

print("You finally reach the city bus stop!")
PressToContinue.PressToContinue()
print("Pearbook: Oh no! to your right there is an enemy in that bush I hear!")

money = EnemyEncounter.EnemyEncounter(money)

print("Pearbook: Finally we have made it perfectly on time to the city bus stop!")
PressToContinue.PressToContinue()

print("Bus Driver: \"Welcome to the city bus! Please pay your fare and enjoy the ride.\"")
PressToContinue.PressToContinue()
print("The Fare for the city bus is $10.")
if money >= 10:
    print("You pay the fare and board the city bus.")
    print("Pearbook: Now  that we are on the city bus, we can finally start our journey as a Pythonmon Trainer!\n We are gonna rule em all!!")

else:
    print("Pearbook: You do not have enough money to pay the fare. You cannot board the city bus.")
    PressToContinue.PressToContinue()
    print("Game over, you cannot continue your pythonmon journey... :(")
    exit()

print("Thank you for playing Pythonmon!")
print("This game is really simple but it was a lot of fun using my brain creatively!")