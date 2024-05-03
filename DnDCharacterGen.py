"""
DnD Character Generator
Author: Mason Nix

!!!! Please see the README at https://github.com/ksu-is/dnd-character-generator. It is important to install easygui !!!!!



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


#init features list
features = []

#Creating Character Classes as its own Python Class

class Fighter:
    title = "Fighter"
    hd = 10
    profBonus = 2
    ac = 16 # chain mail
    primary = "str"
    weapon = "greatsword"
    
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
        return "Class: Level 1 {} \nHit Points: {}\nHit Dice: 1d{} \nProficiency Bonus: +{} \n\nArmor Class: {}\n".format(Fighter.title, Fighter.getHp(self), Fighter.hd, Fighter.profBonus, Fighter.ac)
    def getHp(self):
        return self.hd + con_mod
    def getSaves(self):
        return["con","str"]
        
class Wizard:
    title = "Wizard"
    hd = 6
    profBonus = 2
    ac = 13 #mage armor
    primary = "int"
    weapon = "none"
    spellbook_0 = ["Minor Illusion,", "Mage Hand,", "Firebolt"]
    spellbook_1 = ["Mage Armor,", "Shield,", "Magic Missile,", "Find Familiar,", "Detect Magic,", "Chromatic Orb"]
    
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
        return "Class: Level 1 {} \nHit Points: {}\nHit Dice: 1d{} \nProficiency Bonus: +{} \n\nArmor Class: {}\n".format(Wizard.title, Wizard.getHp(self), Wizard.hd, Wizard.profBonus, Wizard.getAc(self))
    def getHp(self):
        return self.hd + con_mod
    def getSaves(self):
        return["wis","int"]
    def getAc(self):
        return self.ac + dex_mod
        
class Rogue:
    title = "Rogue"
    hd = 8
    profBonus = 2
    ac = 11 #leather armor
    primary = "dex"
    weapon = "dagger"

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
        return "Class: Level 1 {} \nHit Points: {}\nHit Dice: 1d{} \nProficiency Bonus: +{} \n\nArmor Class: {}\n".format(Rogue.title, Rogue.getHp(self), Rogue.hd, Rogue.profBonus, Rogue.getAc(self))
    def getHp(self):
        return self.hd + con_mod
    def getSaves(self):
        return["dex","int"]
    def getAc(self):
        return self.ac + dex_mod


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
  
#method to add racial bonuses to ability scores
def addracialBonus(species, job):
    
    job.Str += species.str_race
    job.Dex += species.dex_race
    job.Con += species.con_race
    job.Int += species.int_race
    job.Wis += species.wis_race
    job.Cha += species.cha_race

#method to determine ability modifiers which derive from their ability score
def getMods(stat):
    if stat == 10 or stat == 11:
        return 0
    if stat == 12 or stat == 13:
        return 1
    if stat == 14  or stat == 15:
        return 2
    if stat == 16 or stat == 17:
        return 3
    if stat == 18 or stat == 19:
        return 4
    if stat == 20:
        return 5

def calcSaves(prof,job):
    save1 = prof[0]
    save2 = prof[1]
    str_save = str_mod
    dex_save = dex_mod
    con_save = con_mod
    int_save = int_mod
    wis_save = wis_mod
    cha_save = cha_mod
    
    if save1.lower() == "str"  or save2.lower() == "str":
        str_save += job.profBonus
    if save1.lower() == "dex"  or save2.lower() == "dex":
        dex_save += job.profBonus
    if save1.lower() == "con"  or save2.lower() == "con":
        con_save += job.profBonus
    if save1.lower() == "int"  or save2.lower() == "int":
        int_save += job.profBonus
    if save1.lower() == "wis"  or save2.lower() == "wis":
        wis_save += job.profBonus
    if save1.lower() == "cha"  or save2.lower() == "cha":
        cha_save += job.profBonus
        
    return [str_save, dex_save ,con_save ,int_save ,wis_save ,cha_save]
    
def calcAttack(martial):
    if martial.title.lower() == "wizard":
        return
    if martial.primary == "str":
        return str_mod + martial.profBonus
    if martial.primary == "dex":
        return dex_mod + martial.profBonus
    
def calcSpellDC(caster):
    if caster.title.lower() != "wizard":
        return
    dc = 8 + caster.profBonus + int_mod
    return dc
        
        
    
    

#Gathering user input and creating GUI using easygui
easygui.msgbox("Hello! Welcome to DnD Character Gen!\n")

#User selects their race from elf, human, or dwarf
raceChoice = easygui.buttonbox("Please choose a character race:", "Race Selection", ("Elf", "Human", "Dwarf"))

if raceChoice == None:
    print("Exiting...")
    sys.exit()
if raceChoice.lower() == "elf":
    race = Elf()
if raceChoice.lower() == "human":
    race = Human()
if raceChoice.lower() == "dwarf":
    race = Dwarf()

        
    
easygui.msgbox(race.getString())

##User selects their character class from wizard, fighter, or rogue    
core =  easygui.buttonbox("Please choose a character class\n\nFighters stike down their foes with raw martial prowess\n\nWizards cast powerful magic to control the battlefield\n\nRogues use stealth to strike from the shadows","Class Selction",("Fighter","Wizard","Rogue"))

if core == None:
    print("Exiting...")
    sys.exit()
if core.lower() == "wizard":
    vocation = Wizard()
    easygui.msgbox(vocation.getString())
if core.lower() == "fighter":
    vocation = Fighter()
    easygui.msgbox(vocation.getString())
if core.lower() == "rogue":
    vocation = Rogue()
    easygui.msgbox(vocation.getString())
    
#adding racial bonuses and calculating ability score modifiers 
addracialBonus(race,vocation)
str_mod = getMods(vocation.Str)
dex_mod = getMods(vocation.Dex)  
con_mod = getMods(vocation.Con)  
int_mod = getMods(vocation.Int)
wis_mod = getMods(vocation.Wis)
cha_mod = getMods(vocation.Cha)
savesList = calcSaves(vocation.getSaves(),vocation)
spellDc = calcSpellDC(vocation)
atkBonus = calcAttack(vocation)
 
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


#creating the sheet and writing all character information to the file
sheet = open("Character_Sheet_{}.txt".format(name), "w")

sheet.write("Name: {}\n".format(name))
sheet.write("Race: {}\n".format(race.title))
sheet.write(vocation.toString())
sheet.write("Initiative: +{}\n".format(dex_mod))
sheet.write("Speed: {} ft\n\n".format(race.speed))
sheet.write("Strength: {}(+{}) | Dexterity: {}(+{}) | Constitution: {}(+{}) | Intelligence: {}(+{}) | Wisdom: {}(+{}) | Charisma: {}(+{}) \n".format(vocation.Str, str_mod, vocation.Dex, dex_mod, vocation.Con, con_mod, vocation.Int, int_mod, vocation.Wis, wis_mod, vocation.Cha, cha_mod))
sheet.write("Saving Throws: Str +{}, Dex +{}, Con +{}, Int +{}, Wis +{}, Cha +{}".format(savesList[0], savesList[1], savesList[2], savesList[3], savesList[4], savesList[5]))

if vocation.title.lower() == "wizard":
    sheet.write("\n\nSpell Save DC: {}".format(spellDc))
    sheet.write("\nCantrips: ")
    for x in vocation.spellbook_0:
        sheet.write(x + " ")
    sheet.write("\n1st Level Spells: ")
    for x in vocation.spellbook_1:
        sheet.write(x + " ")
    sheet.write("(2 spell slots)")
    sheet.write("\n\n\n")
if vocation.weapon == "greatsword":
    sheet.write("\n\nWeapon Attacks\nGreatsword: +{} to hit, 2d6 + {} slashing damage".format(atkBonus,str_mod))
if vocation.weapon == "dagger":
    sheet.write("\n\nWeapon Attacks\nDagger: +{} to hit, 1d4 + {} slashing damage + 1d6 (Sneak Attack)".format(atkBonus,dex_mod))

print("Character Sheet Generated Succesfully! \nPlease look for a file named Character_Sheet_{}.txt in the directory you ran this program.".format(name))
sheet.close()
   

    
