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
        
        elif (option == "3" or
            option == "story 3" or
            option == "story3" or 
            option == "three" or
            option == "story three"):
                option = "3"
                goodInput = True
                
        elif (option == "4" or
            option == "story 4" or
            option == "story4" or
            option == "four" or
            option == "story four"):
                option = "4"
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
    
def getTeacher(prompt, debug = False):
    if debug: print("getTeacher Function")
    
    goodInput = False
    
    teachers = ["mrs. hill",
                "mr. spooner",
                "mrs. Ellis",
                "mrs. hall",
                "mrs. valerio",
                "mr. anderson",
                "mrs. skov",
                "mr. selby",
                "mrs. dwyer",
                "mr. girard",
                "",
                "",
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
        elif word.lower() not in teachers:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that teacher at Kearsarge.")
        
    return word  
    
def getGrade(prompt, debug = False):
    if debug: print("getTeacher Function")
    
    goodInput = False
    
    grades = ["a",
              "a-",
              "a+"
              "b",
              "b-",
              "b+",
              "c",
              "c-",
              "c+",
              "d",
              "d-",
              "d+",
              "f"
    ]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in grades:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that Grade.")
        
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
             "pig",
             "kyle",
             "turtle",
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
        elif word.lower() not in Animal:
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



swearList =["poop",
            "pee",
            "dipshit",
            "bullshit",
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
            "hoe",
            "asshat",
            "dick",
            "dickhead",
            "fortnite",
            "puurrpdrank",
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
            "hairy balls"]


def getRockInstrument(prompt, debug = False):
    if debug: print("getRockInstrument Function")
    
    goodInput = False
    
    RockInstrument = ["stratocaster",
                      "telecaster",
                      "precision bass",
                      "p bass",
                      "p-bass",
                      "jazz bass",
                      "j bass",
                      "j-bass",
                      "les paul",
                      "guitar",
                      "bass",
                      "bass guitar",
                      "keyboard",
                      "piano",
                      "grand piano",
                      "synthesizer",
                      "rock organ",
                      "drum kit",
                      "drum set"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in RockInstrument:
            goodInput= False
            print("\n")
            print ("Instrument not recognized. Please input another instrument.")
        
    return word  

