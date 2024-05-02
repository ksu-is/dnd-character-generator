"""
DnD Character Generator
Author: Mason Nix
Main Progran Functionality

!!!!To understand the distinction between "Character Class" and "Python Class" please see the README. It is important to avoid confusion!!!!!



"""
import easygui

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
        
class Wizard:
    title = "Wizard"
    hd = 6
    profBonus = 2
    ac = 13 + dex_mod
    hp = hd + con_mod
    def __init__(self, name):
        self.charName = name
        
    def toString(self):
        print("Name: {} \nClass: {} \nHit Dice: d{} \nProficiency Bonus: +{} \nArmor Class: {}\n".format(self.charName, Wizard.title, Wizard.hd, Wizard.profBonus, Wizard.ac))
    
#print("Str: 14(+2) | Dex: 10(+0) | Con: 16(+3) | Int: 17(+3) | Wis: 12(+1) | Cha: 10(+0) \n")

#Creating Character Races as Python Classes

class Elf:
    title = "Wood Elf"
    size = "Medium"
    Dex = Dex + 2
    Wis = Wis + 1
    darkvision = True
    Languages = ["Common", "Elven"]
    feature = "Fleet of Foot"
    
    description = "You are a Wood Elf. Your size class is medium. You gain a +2 to your Dexterity and +1 to your Wisdom scores. You have darkvision with a range of 60ft. You speak the common language and Elven. You gain the feature Fleet of Foot.\n"
    
    def getString(self):
      return self.description
    
    def toString(self):
        print("You are a Wood Elf. Your size class is medium. You gain a +2 to your Dexterity and +1 to your Wisdom scores. You have darkvision with a range of 60ft. You speak the common language and Elven. You gain the feature Fleet of Foot.\n")
    

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
        
    description = "You are a Human. Your size class is medium. You gain a +1 to all ability scores. You speak the common language.\n"
    
    def getString(self):
      return self.description
    
    def toString(self):
        print("You are a Human. Your size class is medium. You gain a +1 to all ability scores. You speak the common language.\n")


easygui.msgbox("Hello! Welcome to DnD Character Gen!\n")

while True:
    raceChoice = easygui.buttonbox("Please choose a character race:", "Race Selection", ("Elf", "Human", "Dwarf"))
    if raceChoice.lower() == "elf":
        race = Elf()
        break
    elif raceChoice.lower() == "human":
        race = Human()
        break
    else:
        easygui.msgbox("Please select either Elf or Human")
    
easygui.msgbox(race.getString())
    
#core = input ("Please choose a character class (Fighter or Wizard): ")

