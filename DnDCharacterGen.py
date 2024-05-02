"""
DnD Character Generator
Author: Mason Nix
Main Progran Functionality

!!!!To understand the distinction between "Character Class" and "Python Class" please see the README. It is important to avoid confusion!!!!!



"""
import easygui
import os
import sys

#init derived stats global variables
str_mod = 0
dex_mod = 0
con_mod = 0
int_mod = 0
wis_mod = 0
cha_mod = 0



features = []


#Creating Character Classes as its own Python Class

class Fighter:
    title = "Fighter"
    hd = 10
    profBonus = 2
    ac = 16
    hp = hd + con_mod
    
    Str = 15
    Dex = 13
    Con = 14
    Int = 10
    Wis = 10
    Cha = 10
    
    
    description = "You are a Fighter. You wield your weapon with unmatched skill."
    
    def getString(self):
      return self.description

    def toString(self):
        return "Class: Level 1 {} \nHit Points: {}\nHit Dice: 1d{} \nProficiency Bonus: +{} \n\nArmor Class: {}\n".format(Fighter.title, Fighter.hp, Fighter.hd, Fighter.profBonus, Fighter.ac)
        
class Wizard:
    title = "Wizard"
    hd = 6
    profBonus = 2
    ac = 13 + dex_mod
    hp = hd + con_mod
    
    Str = 10
    Dex = 14
    Con = 12
    Int = 15
    Wis = 11
    Cha = 10
    
    
    description = "You are a Wizard! You hold the power to bend reality to your will."
    
    def getString(self):
      return self.description
        
    def toString(self):
        return "Class: Level 1 {} \nHit Points: {}\nHit Dice: 1d{} \nProficiency Bonus: +{} \n\nArmor Class: {}\n".format(Wizard.title, Wizard.hp, Wizard.hd, Wizard.profBonus, Wizard.ac)
        
class Rogue:
    title = "Rogue"
    hd = 8
    profBonus = 2
    ac = 11 + dex_mod
    hp = hd + con_mod

    Str = 10
    Dex = 15
    Con = 12
    Int = 11
    Wis = 10
    Cha = 14
    
    description = "You are a Rogue. You inflict deadly wounds from the shadows."
    
    def getString(self):
      return self.description
        
    def toString(self):
        return "Class: Level 1 {} \nHit Points: {}\nHit Dice: 1d{} \nProficiency Bonus: +{} \n\nArmor Class: {}\n".format(Rogue.title, Rogue.hp, Rogue.hd, Rogue.profBonus, Rogue.ac)


#Creating Character Races as Python Classes

class Elf:
    title = "Wood Elf"
    size = "Medium"
    speed = 35
    
    str_race = 0
    dex_race = 2
    con_race = 0
    int_race = 0
    wis_race = 1
    cha_race = 0 
    
    darkvision = True
    Languages = ["Common", "Elven"]
    features.append("Fleet of Foot: speed increased by 5 ft")
    
    description = "You are a Wood Elf. Your size class is medium. You gain a +2 to your Dexterity and +1 to your Wisdom scores. You have darkvision with a range of 60ft. You speak the common language and Elven. You gain the feature Fleet of Foot.\n"
    
    def getString(self):
      return self.description
    

class Human:
    title = "Human"
    size = "Medium"
    speed = 30
    
    str_race = 1
    dex_race = 1
    con_race = 1
    int_race = 1
    wis_race = 1
    cha_race = 1 

    darkvision = False
    Languages = ["Common"]
        
    description = "You are a Human. Your size class is medium. You gain a +1 to all ability scores. You speak the common language.\n"
    
    def getString(self):
      return self.description
    

class Dwarf:
    title = "Dwarf"
    size = "Medium"
    speed = 25
    
    str_race = 2
    dex_race = 0
    con_race = 2
    int_race = 0
    wis_race = 0
    cha_race = 0 
    
    darkvision = True
    Languages = ["Common, Dwarven"]
        
    description = "You are a Mountain Dwarf. Your size class is medium. You gain a +2 to Strength and Constitution. You are resistant to poison and have addtional weapon and armor proficiencies. You speak the common language and Dwarven.\n"
    
    def getString(self):
      return self.description
  

def addracialBonus(species, job):
    
    job.Str += species.str_race
    job.Dex += species.dex_race
    job.Con += species.con_race
    job.Int += species.int_race
    job.Wis += species.wis_race
    job.Cha += species.cha_race
    
    

#Gathering user input and creating GUI using easygui
easygui.msgbox("Hello! Welcome to DnD Character Gen!\n")

#User selects their race from elf, human, or dwarf
raceChoice = easygui.buttonbox("Please choose a character race:", "Race Selection", ("Elf", "Human", "Dwarf"))
if raceChoice.lower() == "elf":
    race = Elf()
if raceChoice.lower() == "human":
    race = Human()
if raceChoice.lower() == "dwarf":
    race = Dwarf()
    
        
    
easygui.msgbox(race.getString())

##User selects their character class from wizard, fighter, or rogue    
core =  easygui.buttonbox("Please choose a character class\n\nFighters stike down their foes with raw martial prowess\n\nWizards cast powerful magic to control the battlefield\n\nRogues use stealth to strike from the shadows","Class Selction",("Fighter","Wizard","Rogue"))
if core.lower() == "wizard":
    vocation = Wizard()
    easygui.msgbox(vocation.getString())
if core.lower() == "fighter":
    vocation = Fighter()
    easygui.msgbox(vocation.getString())
if core.lower() == "rogue":
    vocation = Rogue()
    easygui.msgbox(vocation.getString())
    
#adding racial bonuses
addracialBonus(race,vocation)
 
#gathering user input for a character name
while(True):
    name = easygui.enterbox("Name your character:")  
    
    if name == None:
        print("Exiting...")
        sys.exit()
    if name.isalpha() and len(name) <= 20:
        break
    else:
        easygui.msgbox("Please input only A-Z and use 20 or less characters")

    

sheet = open("Character_Sheet_{}.txt".format(name), "w")

sheet.write("Name: {}\n".format(name))
sheet.write("Race: {}\n".format(race.title))
sheet.write(vocation.toString())
sheet.write("Initiative: +{}\n".format(dex_mod))
sheet.write("Speed: {} ft\n\n".format(race.speed))
sheet.write("Str: {}(+{}) | Dex: {}(+{}) | Con: {}(+{}) | Int: {}(+{}) | Wis: {}(+{}) | Cha: {}(+{}) \n".format(vocation.Str, str_mod, vocation.Dex, dex_mod, vocation.Con, con_mod, vocation.Int, int_mod, vocation.Wis, wis_mod, vocation.Cha, cha_mod))


print("Character Sheet Generated Succesfully! \nPlease look for a file named Character_Sheet_{}.txt in the directory you ran this program.".format(name))
sheet.close()
   

    
