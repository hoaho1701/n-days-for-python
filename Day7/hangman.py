stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
lives = 6
import random
# import hangman_words
# chosen_word = random.choice(hangman_words.words_list)
from hangman_words import words_list
chosen_word = random.choice(words_list)
print(f'Pssst, the solution is {chosen_word}')

from hangman_art import logo
print(logo)

display = []
for _ in range(len(chosen_word)):
  display += "_"
end_game = False

while not end_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You've already guessed {guess}")
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if guess == letter:
      display[position] = letter
      
  if guess not in chosen_word:
    print(f"You guess {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_game = True
      print("You lose.")
  print(f"{' '.join(display)}")

  if "_" not in display:
    end_game = True
    print("You win.")
    from hangman_art import stages
  print(stages[lives])
                                          