import pygame
import os
import random


#---------------------
# Book Objects
#---------------------
class BooksObjects:
    class Book:
        def __init__(self, book_ans, book_cover):
            self.answer = book_ans #--> answer for the book (to be used in quiz)
            self.image = pygame.image.load(os.path.join("ProjectImages", "BookImages", book_cover)).convert_alpha() #--> helps transparent background load
            self.image = pygame.transform.smoothscale(self.image, (180, 180))
            self.rect = self.image.get_rect()

# Create book LIST to initalize & store book objects
books = [
    BooksObjects.Book("Book1", "book1.png"), #--Choosing a book from BooksObject class, and defining its answer & image
    BooksObjects.Book("Book2", "book2.png"),
    BooksObjects.Book("Book3", "book3.png"),
    BooksObjects.Book("Book4", "book4.png"),
    BooksObjects.Book("Book5", "book5.png"),
]


#>>---------------------------------
# INIT
#>>---------------------------------
class BubbleGame():
    def __init__(self):
        pygame.init()
        
# Method for randomized book answer
chosen_book = random.choice(books) #--> Randomly selects a book from the list of books
book_answer = chosen_book.answer #--> STORES THE CHOSEN ANSWER

# Function for guessing the book answer
def guess_book(chosen_book):
    correct = chosen_book.answer

    print("Guess the book!")
    print("Options: Book1, Book2, Book3, Book4, Book5")

    for attempt in range(3):
        guess = input("Your guess: ")

        if guess.lower() == correct.lower():
            print("Correct! The book was:", correct)
            return True

        print("Wrong!")

        # Guess attempt 1 ==> clue 1:
        if attempt == 0:
            print("Clue: There's a plant")
        # Guess attempt 1 ==> clue 1:
        elif attempt == 1:
            print("Clue: It has an animal")
        elif attempt == 2:
            print("Clue: The cover is pink")
    
    print("You lost! The correct answer was:", correct)
    return False

#>>---------------------------------
# DRAW: all images
#>>---------------------------------



"""
# Initializing Pygame
def run():
    pygame.init()
    WIDTH, HEIGHT = 650, 450
    FPS = 60 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Book Mechanics - BETA")

#drawing the background + objects 
    background = pygame.image.load(os.path.join("ProjectImages", "background.jpg"))
    background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))

if __name__ == "__main__":
        run()
"""