# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    s_word = list(secret_word)

    try:
      if(len(letters_guessed) > 0):
        for i in range(len(s_word)):
            for j in range(len(letters_guessed)):
              if(s_word[i] == letters_guessed[j]):
                check = True
                break
              else:
                check = False
        return check
      else:
        return False
    
    except:
       print("Error!")


def get_guessed_word(secret_word, letters_guessed):
    s_word = list(secret_word)
    guessed_word = []

    for i in range(len(s_word)):
      guessed_word.append("_ ")

    for i in range(len(s_word)):
      for j in range(len(letters_guessed)):
        if(s_word[i] == letters_guessed[j]):
          guessed_word[i] = letters_guessed[j]

    return guessed_word
    

def get_available_letters(letters_guessed):
    letters_avalible = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in letters_avalible:
        for j in range(len(letters_guessed)):
            if(i == letters_guessed[j]):
                letters_avalible.remove(i)
    return letters_avalible 
'''    
def count_warnings(warning, attempt, vowel, guess):
  if(warning > 0):
    warning -= 1
    print(f"Warning left: {warning}\n")
  else:
    warning = 3
    tmp = attempt

    for i in range(len(vowel)):
      if(vowel[i] == guess):
        attempt -= 2
        break
      
      if(tmp == attempt):
        attempt -= 1

    print("\nYou have lost all warnings\n")
    print(f"Attempts left: {attempt}\n")
    print(f"Warning left: {warning}\n")
    '''

def hangman(secret_word):

    #secret_word = "parzival"
    secret_word = choose_word(wordlist)
    s_word = list(secret_word)

    check = False
    check_att = False
    check_lett = False

    letters_guessed = []
    available_letters = get_available_letters(letters_guessed)

    attempt = 6
    warning = 3

    vowel = ['a', 'e', 'i', 'o']

    print("-----------------------------------------------------------------")
    print(f"I am thinking of a word that is {len(secret_word)} letters long")
    print(f"You have {attempt} guesses left")
    print(f"And {warning} warnings left")
    print()
    print("Letters avalible:")
    print(*available_letters)
    print()
    
    while(check == False and attempt > 0):
      print("----------------------------------------------------------------")
      while(True):
        guess = input("Enter your letter: ")
        guess = guess.lower()
        print()

        if(len(guess) == 1 and guess.isdigit() == False):
          break
        else:
          if(warning > 0):
            warning -= 1
            print(f"Warning left: {warning}\n")
          else:
            warning = 3
            tmp = attempt

            for i in range(len(vowel)):
              if(vowel[i] == guess):
                attempt -= 2
                break
              
              if(tmp == attempt):
                attempt -= 1

            print("\nYou have lost all warnings\n")
            print(f"Attempts left: {attempt}\n")
            print(f"Warning left: {warning}\n")
          print("Enter correct value!\n")
          continue

      for i in range(len(s_word)):
        if(s_word[i] == guess):
          if(len(letters_guessed) > 0):
            for j in range(len(letters_guessed)):

              if(letters_guessed[j] != guess):
                check_lett = True

              else:
                check_lett = False

            if(check_lett == True):
              letters_guessed.append(guess)
            else:
              if(warning > 0):
                warning -= 1
                print(f"Warning left: {warning}\n")
              else:
                warning = 3
                tmp = attempt

                for i in range(len(vowel)):
                  if(vowel[i] == guess):
                    attempt -= 2
                    break

                if(tmp == attempt):
                  attempt -= 1

                print("\nYou have lost all warnings\n")
                print(f"Attempts left: {attempt}\n")
                print(f"Warning left: {warning}\n")      

            print("You already had wrote this letter!\n")

          else:
            letters_guessed.append(guess)
          
          check_att = True
          break
        else:
          check_att = False
      
      if(check_att == False):
        tmp = attempt

        for i in range(len(vowel)):
          if(vowel[i] == guess):
            attempt -= 2
            break

        if(tmp == attempt):
          attempt -= 1
        
        print("Incorrect letter!")
        print(f"You have {attempt} attempts left\n")
      
      available_letters = get_available_letters(letters_guessed)
      print("Letters available:")
      print(*available_letters)
      print("\n")

      show_word = get_guessed_word(secret_word, letters_guessed)
      print(*show_word)
      print("\n")

      check = is_word_guessed(secret_word, letters_guessed)    
    
    if(attempt <= 0):
      print("You lose!\n")
      print(f"The word was: {secret_word}")

    else:
      print("You win!")
      letters = ''.join(letters_guessed)
      count = len(set(letters))
      print(f"Your score is: {attempt * count}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
  word = list(other_word)
  check = False

  if(len(my_word) == len(word)):
    for i in range(len(my_word)):
      if(my_word[i] == "_ "):
        continue
      else:
        if(my_word[i] == word[i]):
          check = True
        else:
          check = False
          break

  print(check)

def show_possible_matches(my_word):
  check = False
  WordsToShow = []

  for j in range(len(wordlist)):
    word = list(wordlist[j])
    if(len(my_word) == len(word)):
      for a in range(len(word)):
        if(my_word[a] == "_ "):
          continue
        else:
          if(my_word[a] == word[a]):
            check = True
          else:
            check = False
            break
      if(check == True):
        WordsToShow.append(wordlist[j])
    
  if(len(WordsToShow) != 0):
    print(*WordsToShow)
  else:
    print("No possible mathes found!")



def hangman_with_hints(secret_word):
  #secret_word = "parzival"
  secret_word = choose_word(wordlist)
  s_word = list(secret_word)

  check = False
  check_att = False
  check_lett = False

  letters_guessed = []
  available_letters = get_available_letters(letters_guessed)

  attempt = 6
  warning = 3

  vowel = ['a', 'e', 'i', 'o']

  print("-----------------------------------------------------------------")
  print(f"I am thinking of a word that is {len(secret_word)} letters long")
  print(f"You have {attempt} guesses left")
  print(f"And {warning} warnings left")
  print()
  print("Letters avalible:")
  print(*available_letters)
  print()
    
  while(check == False and attempt > 0):
    print("----------------------------------------------------------------")
    while(True):
      guess = input("Enter your letter: ")
      guess = guess.lower()
      print()

      if(len(guess) == 1 and guess.isdigit() == False):
        if(guess == "*"):
          show_word = get_guessed_word(secret_word, letters_guessed)
          match_with_gaps(show_word, secret_word)  

          print() 
          show_possible_matches(show_word)
          print()
        break
      else:
        if(warning > 0):
          warning -= 1
          print(f"Warning left: {warning}\n")
        else:
          warning = 3
          tmp = attempt

          for i in range(len(vowel)):
            if(vowel[i] == guess):
              attempt -= 2
              break

            if(tmp == attempt):
              attempt -= 1

          print("\nYou have lost all warnings\n")
          print(f"Attempts left: {attempt}\n")
          print(f"Warning left: {warning}\n")
        print("Enter correct value!\n")
        continue
    
    if(guess == "*"):
      continue

    for i in range(len(s_word)):
      if(s_word[i] == guess):
        if(len(letters_guessed) > 0):
          for j in range(len(letters_guessed)):

            if(letters_guessed[j] != guess):
              check_lett = True

            else:
              check_lett = False

          if(check_lett == True):
            letters_guessed.append(guess)
          else:
            if(warning > 0):
              warning -= 1
              print(f"Warning left: {warning}\n")
            else:
              warning = 3
              tmp = attempt

              for i in range(len(vowel)):
                if(vowel[i] == guess):
                  attempt -= 2
                  break

              if(tmp == attempt):
                attempt -= 1

              print("\nYou have lost all warnings\n")
              print(f"Attempts left: {attempt}\n")
              print(f"Warning left: {warning}\n")      

          print("You already had wrote this letter!\n")

        else:
          letters_guessed.append(guess)
          
        check_att = True
        break
      else:
        check_att = False
      
    if(check_att == False):
      tmp = attempt

      for i in range(len(vowel)):
        if(vowel[i] == guess):
          attempt -= 2
          break

      if(tmp == attempt):
        attempt -= 1
        
      print("Incorrect letter!")
      print(f"You have {attempt} attempts left\n")
      
    available_letters = get_available_letters(letters_guessed)
    print("Letters available:")
    print(*available_letters)
    print("\n")

    show_word = get_guessed_word(secret_word, letters_guessed)
    print(*show_word)
    print("\n")

    check = is_word_guessed(secret_word, letters_guessed)    
    
  if(attempt <= 0):
    print("You lose!\n")
    print(f"The word was: {secret_word}")

  else:
    print("You win!")
    letters = ''.join(letters_guessed)
    count = len(set(letters))
    print(f"Your score is: {attempt * count}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
