def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or
            option == "exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "story 1" or 
            option == "story1" or 
            option == "one" or
            option == "story one"):
                option = "1"
                goodInput = True
                
        elif (option == "2" or
             option == "story 2" or 
             option == "story2" or 
             option == "two" or
             option == "story two"):
                option = "2"
                goodInput = True
                
                
        elif (option == "u"):
                option = "unicorn"
                goodInput = True
            
        else:
            print ("please make a valid choice: ")
            
    return option   

def getWord(prompt, debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print ("don't use language like that")
        
    return word  
    
def getPlace(prompt, debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print ("don't use language like that")
        
    return word  
    
def getSport(prompt, debug = False):
    if debug: print("getSport Function")
    
    goodInput = False
    
    sports = ["soccer",
              "football",
              "hockey",
              "wrestling",
              "field hockey",
              "skiing",
              "nordic"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in sports:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that sport.")
        
    return word  
    
def getAnimal(prompt, debug = False):
    if debug: print("getAnimal Function")
    
    goodInput = False
    
    Animal = ["dog",
             "cat",
             "cow",
             "frog",
             "toad",
             "bear",
             "peacock",
             "fish",
             "penguin",
             "owl",
             "fox",
             "goose",
             "lion",
             "llama",
             "",
             "",
             "",
             "",
             "",
             
             
             
             
             
        
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in Animal-:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that Animal.")
        
    return word  

def isSwear (word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList :
        return True
    else:
        return False



swearList =[ "poop",
            "pee",
            "shit",
            "fuck",
            "lolfap",
            "bitch",
            "faggot",
            "fag",
            "fucktard",
            "bitch ass hoe",
            "puurrpdrank",
            "kyle goodwin",
            "anus",
            "foreskin",
            "nigger",
            "penis",
            "vagina",
            "poopybutt",
            "cuck",
            "cock",
            "dick",
            "shlong",
            "nutsack",
            "wank",
            "wanker",
            "fagtard",
            "retard", 
            "ass",
            "niggerfaggot",
            "eat my ass",
            "fuck you",
            "fuck me",
            "cum",
            "boner",
            "pussy",
            "porn",
            "cunt",
            "dildo",
            "hairy balls"                                                                                                                       
           
            
]


















