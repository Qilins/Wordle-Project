#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============

from re import A
from tkinter import Y
from player import Player
from unicodedata import name

# TODO - make WordlePlayer
class WordlePlayer(Player):
    def __init__(self, name, maxTry):
        super().__init__(name)
        self.maxTry = maxTry
        self.wins = 0
        self.games = 0
        self.winstreak = 0
        self.maxstreak = 0
    

    def updateStats(self, won, tries):
        while tries < self.maxTry:
            tries += 1

        if won == True:
            self.wins = self.wins+1
            self.winstreak += 1
        if won == False:
            if self.winstreak > self.maxstreak:
                self.maxstreak = self.winstreak
            else:
                self.winstreak = 0
        self.games +=1

        

    def winPercentage(self):
        x = self.wins/self.games
        return str(x)

    def gamesPlayed(self):
        return str(self.games)

    def currentStreak(self):
        return str(self.winstreak)

    def maxStreak(self):
        return str(self.maxstreak)

    def displayStatus():
        print("Games Played: " + str(self.games))
        print("Win %: " + self.winPercentage() + "%")
        print("Current Streak: " + str(self.winstreak))
        print("Max Streak: " + str(self.maxstreak))
        self.guessDist()



