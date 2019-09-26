from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    sport1 = getSport("Enter a sport ", debug)
    Place1= getPlace("enter a place (proper noun) ")
    
    out = "\n"
    out += "\n"
    out+= "One day me and my friend " + friendName1
    out+= " Were out playing " + sport1 
    out+= ". "
    out += "Me and my homie cuh, " + friendName1
    out+= " went to " + Place1 
    
    
    
    return out 



 
