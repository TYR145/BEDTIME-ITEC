# import MealPrep

def page1():
    print("=== PAGE 1 ===")
    print("Press D to go to page 2.")
    #print("Press P to play [Meal Prep - N/A])

    choice = input("Choose: ").lower()

    if choice == "d":
        return "page2"
    #elif choice == "p":
        #MealPrep.run()
        #return "page1"
    else:
        print("Invalid choice.")
        return "page1"
