#Annie
from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function") 
    
    print("\n")
    Teacher1 = getTeacher("enter a teachers name ", debug)
    grade1 = getGrade ("what is your dreeam grade? ", debug)
    grade2 = getGrade ("what is your worst grade? ", debug)
    DreamHome = getWord("Where do you wish to live? ", debug)
    dreamFood = getWord("What is your favorite food? ", debug)
    realtown = getWord("where do you live? ", debug)
    
    
    
    out = "\n"
    out += "\n"
    
    out+= "Once upon a time, you didn't go to Kearsarge, and you never had" + Teacher1 + " as a teacher." + ("\n")
    out+= "In this world every grade you get was a" + grade1 + "and you lived a happy life." + ("\n")
    out+= "You live in " + DreamHome + " and you can eat as much " + dreamFood + " as you want." + ("\n")
    out+= "But, then you woke up, and your average grade was " + grade2 + " and you live in" + realtown + ("\n")
    out+= "Yet, at the end of the day you are still eating" + dreamFood + ", YAY." + "\n"
    
    
    
    
    
    
    return out 



 
