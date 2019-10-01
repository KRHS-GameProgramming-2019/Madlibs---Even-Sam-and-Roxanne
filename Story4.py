from Getters import *

def Story4(debug = False):
    if debug: print("Story4 Function")
    
    print("\n")
    personName = getWord ("Enter the name of a person (or 'I' if referring to yourself): ", debug)
    videoGame1 = getWord ("Enter the name of a really hard video game: ", debug)
    videoGame2 = getWord ("Enter the name of another really hard video game: ", debug)
    nonGamingDevice = getWord ("Enter the name of a non-gaming device: ", debug)
    instrument1 = getRockInstrument ("Enter the name of a rock instrument: ", debug)
    amountTime1 = getWord ("Enter an amount of time: ", debug)
    amountTime1 = getWord ("Enter a shorter amount of time: ", debug)
    
    out = "\n" 
    out += "\n"
    out += "One day, " + personName
    out += " played and beat " + videoGame2
    out += " in " + amountTime1
    out += ". However, " +personName
    out += " thought that this wasn't an impressive enough feat, and later played and beat " + videoGame2
    out += " in " + amountTime2
    out += ". Only then could " + personName
    out += " rest easy knowing that the (quite literally) impossible task of beating " + videoGame2
    out += " with a " + instrument1
    out += " was completed."
    
    return out
   
