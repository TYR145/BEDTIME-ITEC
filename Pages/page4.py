# import BathBunPop

def page4():
    print("=== PAGE 4 ===")
    print("Press D to go to Page 5.")
    print("Press A to go back to Page 3.")
    #print("Press P to play [BATHTIME BUBBLE POP - N/A])

    choice = input("Choose: ").lower()
   
    if choice == "d":
        return "page5"
    elif choice == "a":
        return "page3"
    #elif choice == "p":
        #BATHBUBPOP.run()
        #return "page4"
    else:
        print("Invalid choice.")
        return "page4"
