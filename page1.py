def page1():
    print("\n=== PAGE 1 ===")
    print("FIRST PAGE.")
    print("Press D to go to the next page.")
    print("Press A to go back (does nothing because this is the first page).")
    #print("Press P to play [Meal Prep - N/A])

    choice = input("Choose: ").lower()

    if choice == "d":
        return "page2"
    elif choice == "a":
        return "page1"   # can't go back further
    else:
        print("Invalid choice.")
        return "page1"
