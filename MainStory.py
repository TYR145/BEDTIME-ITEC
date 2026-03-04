"""
import Maze
import Race

def main():
    Maze.run() # maze mini-game page 
    Race.run() # race mini-game page
main()
"""
import Maze
import Race
import page1
import page2
import page3
import page4
import page5
import page6

def main():
    current_page = "page1"

    while current_page != "quit":
        if current_page == "page1":
            current_page = page1.page1()
        elif current_page == "page2":
            current_page = page2.page2()
        elif current_page == "page3":
            current_page = page3.page3()
        elif current_page == "page4":
            current_page = page4.page4()
        elif current_page == "page5":
            current_page = page5.page5()
        elif current_page == "page6":
            current_page = page6.page6()


    # Linking the Mini games to respective pages
        elif current_page == "maze":
            Maze.run()
            current_page = "page2"  # page shown after mini-game is completed

        elif current_page == "race":
            Race.run()
            current_page = "page4"

        else:
            print("Exiting page.")
            current_page = "quit"
    print("That's all for now!")
main()
