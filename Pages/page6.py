# import BOOKSEARCH

def page6():
    print("=== PAGE 6 ===")
    print("Press D to go back to Page 5.")
    print("Press A to restart at page 1")
    #print("Press P to play [BOOKSEARCH - N/A])

    choice = input("Choose: ").lower()

    if choice == "d":
        return "page5"
    elif choice == "a":
        return "page1"
    #elif choice == "p":
        #BOOKSEARCH.run()
        #return "page6"
    else:
        print("Invalid choice.")
        return "page6"
