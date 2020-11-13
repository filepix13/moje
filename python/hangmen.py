print('Hello, you are playing the Hangmen game\n')
sentence = input("Enter the sentence which will be guessed: ")
print(chr(27) + "[2J")

sentence = sentence.lower()
guess = sentence

for l in guess:
    if l == " ":
        continue
    else:
        guess = guess.replace(l, "_")
        
#s_letters = [letter for letter in sentence]
#print(s_letters)
#new = [d for letter in sentence]
#print(sentence.replace)

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
        while sentence.find(search) != -1:
            guess = guess[:sentence.find(search)] + sentence[sentence.find(search)] + guess[sentence.find(search) + 1:]
            sentence = sentence[:sentence.find(search)] + "_" + sentence[sentence.find(search) + 1:]  
        # = sentence.replace(search, "_")

if count == 2:
    print("You lose")
else:
    print("Congratulations!!! You win!!!")    

