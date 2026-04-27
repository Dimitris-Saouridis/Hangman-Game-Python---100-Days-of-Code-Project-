import random
from hangman_words import word_list
from hangman_art import stages, logo
chosen_word=random.choice(word_list)
#print(chosen_word)
lives=6
game_over=False
correct_letters=[]
wrong_letters=[]
display=["_"]*len(chosen_word)
print(logo)
while not game_over:
    print(f"**************** {lives} LIVES *****************")
    print("Word to guess:\n"+"".join(display))
    guess=input("Give me a guess: ").lower()
    if guess in correct_letters or guess in wrong_letters:
        print("You have already guessed this letter which is " + guess)
        continue
    if guess in chosen_word:
        correct_letters.append(guess)
        for i in range(0,len(chosen_word)):
            if guess==chosen_word[i]:
                display[i]=guess
    else:
        wrong_letters.append(guess)
        lives-=1
        print(f"Wrong guess! '{guess}' is not in the word. You lose a life.")
    if lives==0:
        game_over=True
        print("\n**************************** YOU LOSE ****************************")
        print("The word was "+chosen_word)
    if "_" not in display:
            game_over=True
            print("\n**************************** YOU WIN ****************************")
            print("The word was " + chosen_word)
    print(stages[lives])        













