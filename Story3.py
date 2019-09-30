from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")
    
    print("\n")
    friendName1 = getWord ("Enter a friend's name: ", debug)
    friendName2 = getWord ("Enter a second friend's name: ", debug)
    friendName3 = getWord ("Enter a third friend's name: ", debug)
    instrument1 = getRockInstrument("Enter a rock instrument: ", debug)
    instrument2 = getRockInstrument("Enter a second rock instrument: ", debug)
    instrument3 = getRockInstrument("Enter a third rock instrument: ", debug)
    instrument4 = getRockInstrument("Enter a fourth rock instrument: ", debug)
    musicStore1 = getWord ("Enter the name of a music store: ", debug)


    out = "\n"
    out += "\n"
    out += "One day, I, along with three of my friends, " + friendName1 
    out += ", " + friendName2 
    out += ", and " + friendName3
    out += ", went to " + musicStore1
    out += ". " 
    out += "I got a " + instrument1
    out += ", " + friendName1
    out += " got a " + instrument2
    out += ", " + friendName2
    out += " got a " + instrument3
    out += ", and " + friendName3
    out += " got a " + instrument4
    out += "."
    
    
    
    return out
