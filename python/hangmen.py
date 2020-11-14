import random

print("Hello, you are playing the Hangmen game")

still_plaing = None
number_of_lines = -1

while still_plaing != 0:
    print('''
1 - Singleplayer
2 - Multiplayer
3 - Add question to the base
4 - Instruction
5 - Credits
0 - Exit
    ''')

    still_plaing = input("What do you want to do? \n")


    if still_plaing == "1":
        
        with open('zdania.txt', 'r') as file:
            if number_of_lines == -1:
                number_of_lines = 0
                for lines in file:
                    number_of_lines += 1
    
        line_to_read = random.randint(0,number_of_lines-1)

        with open('zdania.txt', 'r') as file:
            for position, line in enumerate(file):
                if position == line_to_read:
                    sentence = line

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
            if search == "":
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


    elif still_plaing == "2":

        player1_score = player2_score = 0

        for x in range(0,4):

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

        if player1_score > player2_score:
            print("Player 1 wins!")
        elif player1_score < player2_score:
            print("Player 2 wins!")
        else:
            print("Tie!")

    elif still_plaing == "3":
        correct = 1     #Checking the sentence
        while correct != 0:
            new_sentence = input("Enter new sentence: ")
            if not 0 < len(new_sentence) <= 50 and new_sentence.isalpha():
                print("Correct sentence must have at least one character and have less or equal to 50 chars\n")
            elif not all(x.isalpha() or x.isspace() for x in new_sentence):
                print("You should enter only letters!\n")
            else:
                correct = 0
        
        with open('zdania.txt', 'a') as file:
            file.write(new_sentence)
            file.write("\n")
        print("Your sentence has been added")

    elif still_plaing == "4":
        print("You need to guess letters from the sentence, you have 11 tries")

    elif still_plaing == "5":
        print("Author: Filip Hellwig")
        
    elif still_plaing == "0":
        print("Closing application...")
        exit()  

    else:
        print("Unrecognised character, try once again")
