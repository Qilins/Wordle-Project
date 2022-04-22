import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
from fancyword import FancyWord
 
 
#======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    word2 = str(word)
    for i in range(5):
        if word2[i] == guess[i]:
            x = guess[i]
            WordleWord.setCorrect(x in alphabet)
        elif word2[i] == guess[0] or word2[i] == guess[1] or word2[i] == guess[2] or word2[i] == guess [3] or word2[i] == guess[4]:
            x = word2[i]
            WordleWord.setMisplaced(x in alphabet)
        elif word2[i] != guess[0] or word2[i] != guess[1] or word2[i] != guess[2] or word2[i] != guess [3] or word2[i] != guess[4]:
            x = word2[i]
            WordleWord.isNotUsed(x in alphabet)
#======
# playRound(players, words, all_words, settings)
# Plays one round of Wordle.
# Returns nothing, but modifies the player statistics at end of round
#
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#======
def playRound(players, words, all_words, settings):
    wordleAnswer = words.getRandom()
    #random word inserted
    goodGuess = 0
    player_guess = input(str("Enter a 5 letter guess: "))
    for i in range(6):
            if len(player_guess) == 5:
                if player_guess in words:
                    goodGuess = goodGuess+1
                else:
                    return(input("Your guess is incorrect"))
            else:
                return(input("Your guess is not in the paramters"))
#  defines the guesses the player has, and if it is correct or incorrect
 
 
def playWordle():
    name = input(str("Enter your name: "))
    print("Hello", name + ", let's play the game of Wordle!")
#  starts the game with input of name
 
   # initialize WordBanks
    all_words = WordBank("words_alpha.txt")
    common_words = WordBank("common5letter.txt")
 
   # intialize settings to the baseline settings
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')
 
   # make the player
    players = WordlePlayer(name, 6)
 
   # start playing rounds of Wordle

    playRound(players, all_words, common_words, settings)
 
   # end game by displaying player stats
 
def main():
    playWordle()
 
if __name__ == "__main__":
    main()
