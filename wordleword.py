#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from fancyword import FancyWord
 
# TODO - make WordleWord
class WordleWord(FancyWord):
  
   def setCorrect(self, pos):
       self.setColorAt(pos, "green")
 
   def setMisplaced(self, pos):
       self.setColorAt(pos, "yellow")
 
   def setUnused(self, pos):
       self.setColorAt(pos, "gray")
 
   def isCorrect(self, pos):
       self.colorAt(pos) == "green"
 
   def isMisplaced(self, pos):
       self.colorAt(pos) == "yellow"
  
   def isNotUsed(self,pos):
       self.colorAt(pos) == "gray"
