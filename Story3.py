#Sam Lloyd
from Getters import *

def Story3(debug = False):
    if debug: print("Story3 Function")
    
    print("\n")
    friendName1 = getWord ("Enter a friend's name: ", debug)
    friendName2 = getWord ("Enter a second friend's name: ", debug)
    instrument1 = getRockInstrument("Enter a rock instrument: ", debug)
    instrument2 = getRockInstrument("Enter a second rock instrument: ", debug)
    musicStore1 = getWord ("Enter the name of a music store: ", debug)
    grade1 = getGrade ("enter in a letter grade: ", debug)
    teacher1 = getTeacher ("enter a teacher: ", debug)
    bandName1 = getWord ("enter a band name: ", debug)

    out = "\n"
    out += "\n"
    out += "One day, I, along with two of my friends, " + friendName1 
    out += "and " + friendName2 
    out += ", and went to " + musicStore1
    out += ". \n" 
    out += "I got a " + instrument1
    out += ", " + friendName1
    out += " got a " + instrument2
    out += ", and " + friendName2
    out += " got nothing. \n"
    out += "But, you couldn't get " + instrument1 + " because you had a " + grade1 + " in band. \n"
    out += "The music store knew your grade, because " + teacher1 + " told " + musicStore1 ". \n"
    out += "Because you couldnt get " + instrument1 + " your friends, " + friendName2 + " and " + friendName1 + " left you alone. \n"
    out += "Your friends, then left you and started a band named" + bandName1 + " and became famous. \n"
    
    
    return out
