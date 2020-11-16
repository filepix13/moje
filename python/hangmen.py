import random
import getpass

class user: 
    def __init__(self, login, password):      
        self.login = login
        self.password = password 



print("Hello, you are playing the Hangmen game\n\n" + "Do you want to: " + "\n1 - Log in" + "\n2 - Sign up" + "\n3 - Play as guest\n")
logging = input("I want to: ")
print("\n")

from_file = []
with open('users.txt', 'r') as file:        #reading the list of users
    for lines in file:
        from_file.append(lines.split()[0])
        from_file.append(lines.split()[1])

if logging == "1":
    while 1:
        login = input("Login: ")
        password = getpass.getpass()        #hiding password
        if from_file.count(login) > 0:      #checking if this login exists
            if from_file[from_file.index(login)+1] == password:
                break
            else:
                print("Your login or password is wrong. Try again")
        else:
            print("Your login or password is wrong. Try again")
            
    
elif logging == "2":
    while 1:
        login = input("Your new login: ")       #checking if this login exists, if not it is valid new login
        if from_file.count(login) == 0:
            break
        else:
            print("This login has been already taken\n")
    while 1:
        password = getpass.getpass(prompt="Your new password: ",stream=None)
        password_check = getpass.getpass(prompt="Repeat your password: ",stream=None)
        if password == password_check:
            break
        else:
            print("\nYou need to type twice this same password")
    with open('users.txt', 'a') as file:
        file.write(login + " " + password + "\n")

elif logging == "3":
    pass
else:
    print("Please choose 1,2 or 3")
print(chr(27) + "[2J")

menu_choice = None
number_of_lines = -1

print("Hi " + login + "!\n")

while menu_choice != 0:
    print('''
1 - Singleplayer
2 - Multiplayer
3 - Add question to the base
4 - Instruction
5 - Credits
0 - Exit
    ''')

    menu_choice = input("What do you want to do? ")
    print("\n")


    if menu_choice == "1":
        
        with open('zdania.txt', 'r') as file:       #How many sentences the base file has
            if number_of_lines == -1:
                number_of_lines = 0
                for lines in file:
                    number_of_lines += 1
                list_of_sentences = []

        end_of = 0
        
        while 1:        #randomizing sentence that is picked
            line_to_read = random.randint(0,number_of_lines-1)
            if list_of_sentences.count(line_to_read) == 0:
                list_of_sentences.append(line_to_read)
                break
            elif len(list_of_sentences) == number_of_lines:
                end_of = 1
                print("You finished the game!! Congratulations")
                break
            else:
                continue

        if end_of == 1:
            continue

        with open('zdania.txt', 'r') as file:       #reading a sentence from the file
            for position, line in enumerate(file):
                if position == line_to_read:
                    sentence = line

        sentence = sentence.lower()     #editing the sentence(easier to work with)
        sentence = sentence.strip()
        guess = sentence        #guess will be transormed into sentence during the game(and vice versa)
        anwser = sentence       #for informative purposes

        for l in guess:         #creating blank sentence
            if l == " ":
                continue
            else:
                guess = guess.replace(l, "-")
        print("Start guessing!")

        #hangmen game rules:
        #-you lose when you enter 11 wrong numbers
        #-you win if you guess every letter(checking it after and)
        count = 0
        while count < 2 and (sentence.count("-") + sentence.count(" ")) != len(sentence):

            print(guess)
            print("\n")
            search = input("Enter letter: ")
            if search == "":        #Checking for unwanted enter
                continue

            if sentence.find(search) == -1:
                print("This letter cannot be found in this sentence!\n")
                count += 1
            else: 
                print("This letter can be found in this sentence!\n")
                while sentence.find(search) != -1:      #changing the sentences
                    guess = guess[:sentence.find(search)] + sentence[sentence.find(search)] + guess[sentence.find(search) + 1:]
                    sentence = sentence[:sentence.find(search)] + "-" + sentence[sentence.find(search) + 1:]  

        print("Correct anwser:" + str(anwser) + "\n")

        if count == 2:
            print("You lose")
        else:
            print("Congratulations!!! You win!!!")


    elif menu_choice == "2":

        player1_score = player2_score = 0

        for x in range(0,8):        #number of rounds

            print("Scores:\nPlayer 1: " + str(player1_score) + "\nPlayer 2: " + str(player2_score))
            print("\nRound " + str(x+1))
            print("\nPlayer " + str((x%2)+1) + " creates the sentence")

            correct = 1     #Checking the sentence
            while correct != 0:
                sentence = input("Enter the sentence which will be guessed: ")
                if not 0 < len(sentence) <= 50 and sentence.isalpha():
                    print("Correct sentence must have at least one character and have less or equal to 50 chars\n")
                elif not all(x.isalpha() or x.isspace() for x in sentence):
                    print("You should enter only letters!\n")
                else:
                    correct = 0

            print(chr(27) + "[2J")      #hiding the sentence from oponent

            sentence = sentence.lower()     #editing the sentence(easier to work with)
            sentence = sentence.strip()
            guess = sentence        #guess will be transormed into sentence during the game(and vice versa)
            anwser = sentence

            for l in guess:         #creating blank sentence
                if l == " ":
                    continue
                else:
                    guess = guess.replace(l, "-")
            print("Start guessing!")

            #hangmen game rules:
            #-you lose when you enter 11 wrong numbers
            #-you win if you guess every letter(checking it after and)
            count = 0
            while count < 2 and (sentence.count("-") + sentence.count(" ")) != len(sentence):
                print(guess)
                print("\n")
                search = input("Enter letter: ")

                if sentence.find(search) == -1:
                    print("This letter cannot be found in this sentence!\n")
                    count += 1
                else: 
                    print("This letter can be found in this sentence!\n")
                    while sentence.find(search) != -1:      #changing the sentences
                        guess = guess[:sentence.find(search)] + sentence[sentence.find(search)] + guess[sentence.find(search) + 1:]
                        sentence = sentence[:sentence.find(search)] + "-" + sentence[sentence.find(search) + 1:]  

            print("Correct anwser:" + str(anwser) + "\n")

            if count == 2:
                print("You don't get a point")
            else:
                print("You get a point")
                if x%2 == 1:
                    player1_score += 1
                else:
                    player2_score += 1
            print("End of this round\n")

        if player1_score > player2_score:       #who wins
            print("Player 1 wins!")
        elif player1_score < player2_score:
            print("Player 2 wins!")
        else:
            print("Tie!")

    elif menu_choice == "3":
        correct = 1     #Checking the sentence
        while correct != 0:
            new_sentence = input("Enter new sentence: ")
            if not 0 < len(new_sentence) <= 50 and new_sentence.isalpha():
                print("Correct sentence must have at least one character and have less or equal to 50 chars\n")
            elif not all(x.isalpha() or x.isspace() for x in new_sentence):
                print("You should enter only letters!\n")
            else:
                correct = 0
        
        with open('zdania.txt', 'a') as file:       #writing the new sentence to the base file
            file.write(new_sentence)
            file.write("\n")
        print("Your sentence has been added")

    elif menu_choice == "4":
        print("You need to guess letters from the sentence, you have 11 tries")

    elif menu_choice == "5":
        print("Author: Filip Hellwig")
        
    elif menu_choice == "0":
        print("Closing application...")
        exit()  

    else:
        print("Unrecognised character, try once again")
