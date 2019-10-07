
#Evan

from Getters import *
def Story1(debug = False):
    if debug: print("Story1 Function") 

    print("\n")
    friendName1 = getWord("Enter a name: ", debug)
    sport1 = getSport("Enter a sport: ", debug)
    Place1= getPlace("enter a place (proper noun): ", debug)
    animal1 = getAnimal("enter an animal: ", debug)
    Teacher1 = getTeacher("enter a teachers name: ", debug)
    grade1 = getGrade ("enter a grade A-F: ", debug)
    food1 = getWord("Enter you favorite food ", debug)
    noun1= getWord("enter where you would hate to sleep", debug)
    
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
    
    out += "Finally, you left " + Place1
    out += " and went home."
    
    out += "once you get home, you eat " + food1 
    out += "after that you sleep on a " + noun1
    
    
    
    
    return out 



 
