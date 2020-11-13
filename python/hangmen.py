print("Hello, you are playing the Hangmen game")

still_plaing = None
while still_plaing != 0:
    print('''
1 - play the game
2 - instruction
3 - credits
0 - exit
    ''')

    still_plaing = input("What do you want to do? ")
    print("\n")

    if still_plaing == "1":
        correct = 1     #Checking the sentence
        while correct != 0:
            sentence = input("Enter the sentence which will be guessed: ")
            if 0 < len(sentence) <= 50 and sentence.isalpha():
                correct = 0
            elif not sentence.isalpha():
                print("You should enter only letters!\n")
            else:
                print("Correct sentence must have at least one character and have less or equal to 50 chars\n")


        print(chr(27) + "[2J")      #hiding the sentence from oponent

        sentence = sentence.lower()     #editing the sentence(easier to work with)
        sentence = sentence.strip()
        guess = sentence        #guess will be transormed into sentence during the game(and vice versa)
        anwser = sentence

        for l in guess:         #creating blank sentence
            if l == " ":
                continue
            else:
                guess = guess.replace(l, "_")
        print("Start guessing!")

        #hangmen game rules:
        #-you lose when you enter 11 wrong numbers
        #-you win if you guess every letter(checking it after and)
        count = 0
        while count < 2 and (sentence.count("_") + sentence.count(" ")) != len(sentence):
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
                    sentence = sentence[:sentence.find(search)] + "_" + sentence[sentence.find(search) + 1:]  


        print("Correct anwser:")
        print(anwser)
        print("\n")

        if count == 2:
            print("You lose")
        else:
            print("Congratulations!!! You win!!!")

    elif still_plaing == "2":
        print("You need to guess letters from the sentence, you have 11 tries")
    elif still_plaing == "3":
        print("Author: Filip Hellwig")
    elif still_plaing == "0":
        print("Closing application...")
        exit()  
    else:
        print("Unrecognised character, try once again")
