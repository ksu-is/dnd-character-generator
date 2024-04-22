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
dex_mod = 2
con_mod = 2
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


#Creating The Fighter Character Class as its own Python Class

class Fighter:
    title = "Fighter"
    hd = 10
    profBonus = 2
    ac = 16
    hp = hd + con_mod
    def __init__(self, name):
        self.charName = name

    def toString(self):
        print("Name: {} \nClass: {} \nHit Dice: d{} \nProficiency Bonus: +{} \nArmor Class: {}\n".format(self.charName, Fighter.title, Fighter.hd, Fighter.profBonus, Fighter.ac))
        
char = Fighter("Njal")
char.toString() 

class Wizard:
    title = "Wizard"
    hd = 6
    profBonus = 2
    ac = 10 + dex_mod
    hp = hd + con_mod
    def __init__(self, name):
        self.charName = name
        
    def toString(self):
        print("Name: {} \nClass: {} \nHit Dice: d{} \nProficiency Bonus: +{} \nArmor Class: {}\n".format(self.charName, Wizard.title, Wizard.hd, Wizard.profBonus, Wizard.ac))
    
char2 = Wizard("Volkmir")  
char2.toString()  

#Creating Character Races as Python Classes

class Elf:
    title = "Wood Elf"
    size = "Medium"
    Dex = Dex + 2
    Wis = Wis + 1
    darkvision = True
    Languages = ["Common", "Elven"]
    feature = "Fleet of Foot"
    
    def toString(self):
        print("You are a Wood Elf. Your size class is medium. You gain a +2 to your Dexterity and +1 to your Wisdom scores. You have darkvision with a range of 60ft. You speak the common language and Elven. You gain the feature Fleet of Foot.\n")
    
    
race = Elf()
race.toString()

class Human:
    title = "Human"
    size = "Medium"
    Str = Str + 1
    Dex = Dex + 1
    Con = Con + 1
    Int = Int + 1
    Wis = Wis + 1
    Cha = Cha + 1
    darkvision = False
    Languages = ["Common"]
        
    def toString(self):
        print("You are a Human. Your size class is medium. You gain a +1 to all ability scores. You speak the common language.\n")

race2 = Human()
race2.toString()

