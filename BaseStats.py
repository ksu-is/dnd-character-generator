"""
DnD Character Generator
Author: Mason Nix
Main Progran Functionality

!!!!To understand the distinction between "Character Class" and "Python Class" please see the README. It is important to avoid confusion!!!!!

"""
#initializing core stats
Str = 0
Dex = 0
Con = 0
Int = 0
Wis = 0
Cha = 0
race  = ""
characterClass = ""

#init derived stats
str_mod = 0
dex_mod = 0
int_mod = 0
wis_mod = 0
cha_mod = 0
ac = 0

#classList = ["Figher", "Bard", "Rogue", "Wizard"]


#decisions = input ("Please input a Character Name:")

#Defining the python class to create character classes from DnD
class CharacterClass:
    def __init__(self, title, hd):
        self.className = title
        self.hd = hd

fighter = CharacterClass("Fighter", 10)
wizard = CharacterClass("Wizard", 6)

print("Class: {} \nHit Dice: d{}".format(fighter.className, fighter.hd))
print("Class: {} \nHit Dice: d{}".format(wizard.className, wizard.hd))

    
    




