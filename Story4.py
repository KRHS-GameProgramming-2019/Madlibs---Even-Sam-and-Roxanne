#Sam Lloyd
from Getters import *

def Story4(debug = False):
    if debug: print("Story4 Function")
    
    print("\n")
    personName = getWord ("Enter the name of a person (or 'I' if referring to yourself): ", debug)
    videoGame1 = getWord ("Enter the name of a really hard video game: ", debug)
    videoGame2 = getWord ("Enter the name of another really hard video game: ", debug)
    videoGame3 = getWord ("Enter the name of an easy video game: ", debug)
    deviceName1 = getDeviceName ("Enter the name of the device this person would play these games on (or just choose one if device support varies): ", debug)
    nonGamingItem1 = getWord ("Enter the name of a non-gaming item: ", debug)
    nonGamingItem2 = getWord ("Enter the name of another non-gaming item: ", debug)
    gamingDevice1 = getWord ("What is used to control these games? If more than one answer, choose your personal preference: ", debug)
    instrument1 = getRockInstrument ("Enter the name of a rock instrument: ", debug)
    
    out = "\n" 
    out += "\n"
    out += "One day, " + personName
    out += " tried to beat " + videoGame2
    out += " using a " + nonGamingItem1 + "on the " + deviceName1 
    out += ". " + ("\n") + personName + " was unsucsessful and decided that it would be worth a try to play " + videoGame2 + " using a " + instrument1
    out += "." + ("\n") + " However, " + personName
    out += " ended up destryoing the " + instrument1 
    out += " after losing the final boss level, effectively ruining the play. " + ("\n") + personName
    out += " decided to take a step back and play " + videoGame3 + " using a " + nonGamingItem1 + ". " + ("\n")
    out += + personName + " failed on the very first level, gave up out of anger and decided to play the games how they were meant to be played: using a " + gamingDevice1
    out += ".\n"
    
    
    return out
   
