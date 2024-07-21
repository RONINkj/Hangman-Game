import random
from  hangman_word import word_list
 
chosen_word=random.choice(word_list)
end_of_game=False
lives=6 

from hangman_stages import logo
print(logo)

blank_list=[]
for letter in chosen_word:
    blank_list+="_"


while not end_of_game:
    guess=input("Guess a letter:").lower()

    for posi in range(len(chosen_word)):
        letter=chosen_word[posi]
        if letter==guess:
            blank_list[posi]=letter

    if guess  not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You Lose.")
    print(blank_list) 


    if "_" not in blank_list:
        end_of_game=True
        print("You win.")

    from hangman_stages import stages
    print(stages[lives])