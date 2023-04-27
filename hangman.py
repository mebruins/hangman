import random
import word_list
import hangman_art

print(hangman_art.logo)
# word_list = ['trumpet', 'flute', 'oboe', 'clarinet', 'saxophone', 'piano',
#              'trombone', 'drums', 'tuba', 'xylophone', 'timpani', 'piccolo',
#              'violin', 'viola', 'cello', 'bassoon', 'baritone', 'harp']
chosen_word = random.choice(word_list.word_list)
word_length = len(chosen_word)
lives = 6

display = []
# incorrect_guess = []

print('======="Welcome to Hangman======\n')
print("Can you guess the word?")

for _ in range(word_length):
    display += "_"
print(display)

while "_" in display:
    guess = input("Guess a letter:\n").lower()
    if guess in display:
        print("You have already guessed that letter.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
        # incorrect_guess += incorrect_guess
        print("Incorrect guess")
        print(f"You have {lives} guesses left.")
        if lives == 0:
            print("You lose!")
            break
    print(hangman_art.stages[lives])
    print(display)

print(f'The word was: {chosen_word}')

# can you add code for guessing incorrect letter second time
# tell user they have already guessed that letter, even though incorrect