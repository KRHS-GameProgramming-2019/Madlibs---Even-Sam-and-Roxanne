#Annie
from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    sport1 = getSport("Enter a sport ", debug)
    Place1= getPlace("enter a place (proper noun) ")
    animal1 = getAnimal("enter an animal ")
    Teacher1 = getTeacher("enter a teachers name ")
    grade1 = getGrade ("enter a grade A-F: ")
    
    out = "\n"
    out += "\n"
    out+= "One day me and my friend " + friendName1
    out+= " Were out playing " + sport1 
    out+= ". "
    out+= "\n"
    
    out += "Me and my homie, " + friendName1
    out+= " went to " + Place1 
    out += " to play " + sport1
    out += ". "
    out += "\n"
    
    out += "while we were playing " + sport1
    out += " we saw a " +animal1
    out += " walking near " + Place1
    out += ". "
    out += "\n"
    
    out += "Then, " + Teacher1
    out += " walked up to you and told you you got a " + grade1
    out += " in the class and you cried because it was such a bad grade"
    out += ". "
    out +="\n"
    
    out += "Finnaly, you left " + Place1
    out += " and went home."
    
    
    
    
    return out 



 
