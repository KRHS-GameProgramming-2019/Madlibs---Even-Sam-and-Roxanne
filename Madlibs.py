from Screens import *
from Getters import *
from Story1 import *
from Story2 import *
from Story3 import *
from Story4 import *
from Group_Story import *
from SamEasterEgg import *



def Madlibs (debug = False):
    if debug: print ("welcome to debug")
    
    print(TitleScreen(debug))
    input ("press enter to continue")

    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
       
        if choice == "q":
            exit();
            
        elif choice == "1":
            print(Story1())
            print("\n") 
            input("press enter to continue")
            
        elif choice == "2":
            print(Story2())
            print("\n") 
            input("press enter to continue")
            
        elif choice == "3":
            print(Story3())
            print("\n")
            input("press enter to continue")
            
        elif choice == "4":
            print(Story4())
            print("\n")
            input("press enter to continue")
            
        elif choice == "5":
            print(Story5())
            print("\n")
            input("press enter to continue")
 
        elif choice == "kyle":
            print("Kyle is a snakey snake")
            import snake 
            
        elif choice == "unicorn":
            print("\n Unicorn")
            print("You have found my magical land")
            import Unicorn
            input("press enter to continue")
            
        elif choice == "ee":
            print(SamEasterEgg())
            print("\n")
            input("01110000 01110010 01100101 01110011 01110011 00100000 01100101 01101110 01110100 01100101 01110010 00100000 01110100 01101111 00100000 01100011 01101111 01101110 01110100 01101001 01101110 01110101 01100101")
            
            
            
Madlibs()






Madlibs (True)

