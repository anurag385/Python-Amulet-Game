#copy this code to your IDE and then execute the code to play.
import time
import random

print("Welcome to Python Amulet Adventure Game")
print("Your choices must be only written in lower case... thank you for your time")
time.sleep(3)
print("Once upon a time in the mystical land of Pythoria, there existed a legendary artifact known as the Python Amulet.")
time.sleep(4)
print("This powerful relic was said to possess the ability to unlock untold knowledge and magic. Many had sought after it, but none had succeeded in locating its elusive whereabouts.")
time.sleep(3)
print("A young and aspiring Python programmer named Alex, stumbled upon an ancient map hidden within the depths of an old library. The map revealed cryptic clues leading to the Python Amulet's hidden sanctuary deep within the Enchanted Forest.")
time.sleep(3)
print("Diving into Alex Character. . . .")
time.sleep(3)

print("Let's Begin the Journey to the Python Amulet.")
time.sleep(1)
print(" in a dimly lit library, shelves stacked with dusty tomes. Alex, a young and enthusiastic programmer, browses through a stack of ancient scrolls. Suddenly, a glint catches their eye as they unearth an old map tucked within the pages of an ancient manuscript")
print("Alex: What is this a map?")
print("Map: Yes...I am")
time.sleep(2)
print("Alex: Wait a map replied?? This looks like...")
time.sleep(2)
print("Its a map to Python Amulet...")
print("Map: Yes now You enter...")

print("SHALL WE BEGIN? YES OR YES")
time.sleep(2)
choice = input().lower()
if choice == "yes":
    print("There is no going back, Lets start the adventure")
    
    # Introduction
    print("\n You find yourself standing in front of a mysterious Cave...")
    time.sleep(1)
    print("Legend has it that a treasure lies deep within the cave, guarded by mythical creatures.")
    time.sleep(1)
    
    # Choice
    print("\n Do You Want to Enter the Game?: Yes or No")
    enter = input().lower()
    if enter == 'yes':
        print("You chose the bravest path of finding the Amulet in the cave, cautiously checking for it you are going deep into the cave ")
        time.sleep(2)
        print("As you move you encountered a fork path to move left or right, there is a caution written on the wall")
        time.sleep(2)
        print("The both of the ways lead to the same path, but the choices you make choose yourself a path of difficulties...")
        fork_choice = input().lower()
        if fork_choice == 'left':
            print("You chose the left path...")
            time.sleep(2)
            print("\n As you walk you notice something on your right side...")
            time.sleep(2)
            print("Its a huge mystical creature looks like a dragon...")
            print("You should fight with that dragon to move forward...")
            # Dragon fight 1
            print("\n Prepare for battle...")
            time.sleep(1)
            player_health = 100
            dragon_health = 150
            for round in range(1, 4):  # 3 rounds
                print("\n --- Round", round, "---")
                player_attacks = random.randint(10, 20)
                dragon_attacks = random.randint(15, 25)
                # Player attacks
                print("You attack Dragon with all your might")
                dragon_health -= player_attacks
                print("You Dealt ", player_attacks, "damage to the dragon. Dragon's Health", dragon_health)
                
                # Dragon Attacks
                print("Dragon attacks you with fiery breath!")
                player_health -= dragon_attacks
                # Check if defeated by the dragon
                if player_health <= 0:
                    print("You have been defeated by the dragon")
                    break
                elif dragon_health <= 0:
                    print("You have won the battle")
            
            time.sleep(2)
            print("As you won the deadliest battle, keep moving for the Amulet")
        elif fork_choice == 'right':
            print("You chose the right path...")
            print("The ground started to shake below your legs...")
            time.sleep(2)
            print("You stated to fall... now you are entering a loop state press the number 1 for 5 times to reach the correct destination else you will die...")
            time.sleep(1)
            count = 0  # initializing count var to keep track of numbers
            for _ in range(5):
                number = int(input())
                if number == 1:
                    count += 1
                else:
                    print("incorrect number plz enter 1")
            if count == 5:
                print("As you entered 1 successfully for 5 times it activated a magic spell which is now taking you to the Amulet's real path...")
            else:
                print("You died")    
            print("\n As you walk you notice something on your left side...")
            time.sleep(2)
            print("Its a huge magical creature looks like a dragon...")
            print("You should fight with that dragon to move forward...")
            # Dragon fight 2
            print("\n Prepare for battle...")
            time.sleep(1)
            player_health = 100
            dragon_health = 150
            for round in range(1, 4):  # 3 rounds
                print("\n --- Round", round, "---")
                player_attacks = random.randint(10, 20)
                dragon_attacks = random.randint(15, 25)
                # Player attacks
                print("You attack Dragon with all your might")
                dragon_health -= player_attacks
                print("You Dealt ", player_attacks, "damage to the dragon. Dragon's Health", dragon_health)
                
                # Dragon Attacks
                print("Dragon attacks you with fiery breath!")
                player_health -= dragon_attacks
                # Check if defeated by the dragon
                if player_health <= 0:
                    print("You have been defeated by the dragon")
                    break
                elif dragon_health <= 0:
                    print("You have won the battle")
            
            time.sleep(2)
            print("As you won the deadliest battle, keep moving for the Amulet")
        time.sleep(3)
        print("You are now finally entering the Amulets Location....")
        time.sleep(2)
        print("You can see many people bodies and some of them still alive but cannot move, they told there is a small puzzle to solve if not you will remain the same, they also mentioned its a python question")
        time.sleep(2)
        print("The question is...")
        time.sleep(2)
        # Given code for generating the question
        x = random.randint(1, 9)  # Generate a random integer between 1 and 9
        n = random.randint(1, 5)  # Generate a random integer between 1 and 5
        term_num = str(x)
        total = 0
        for i in range(1, n + 1):
            term = term_num * i
            total += int(term)
        correct_answer = total

        print("What is the total sum after repeating the number", x, "for", n, "times?")

        # Player's answer
        player_answer = int(input("Your answer: "))

        # Comparing with the correct answer
        if player_answer == correct_answer:
            print("Congratulations! You have solved the puzzle.")
            time.sleep(2)
            print("You have found the Amulet, with unlimited knowledge, You made it, you have won the game")
            print("Thanks for playing...")
            print("Will be back with more adventures")
        else:
            print("Sorry, that's incorrect. You remain trapped like the others.")
            print("Game Over...")
            print("Restart and choose wisely this time...")
elif choice.lower() == "no":
    print("\nYou hesitate at the entrance of the cave, unsure if you're ready to face the unknown.")
    print("After a moment of contemplation, you decide to turn back and explore elsewhere.")
    print("Perhaps another adventure awaits you beyond the cave's confines.")
else:
    print("\nInvalid choice. You stand frozen at the entrance, uncertain of what to do next.")
    print("The wind whispers through the cave's mouth as you weigh your options.")
