# import PYJAMAMEMORY
def page5():
    print("=== PAGE 5 ===")
    print("Press D to got to Page 6.")
    print("Press A to go back to Page 4.")
    #print("Press P to play [PYJAMA MEMORIZING MATCHING - N/A])

    choice = input("Choose: ").lower()

    if choice == "d":
        return "page6"
    elif choice == "a":
        return "page4"
    #elif choice == "p":
        #PYJAMAMEMORY.run()
        #return "page4"
    else:
        print("Invalid choice.")
        return "page5"