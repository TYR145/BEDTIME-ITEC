from tkinter import font

import pygame
import os
import random


#---------------------
# Book Objects
#---------------------
class BookObjects:
   
    class Book: # defining books properties
        def __init__(self, book_ans, book_cover):
            # defining & loading image (x,y) dimensions
            self.image = pygame.image.load(os.path.join("ProjectImages", "BooksImages", book_cover)).convert_alpha() #--> .convert_alpha for a transparent PNG (yes)
            self.image = pygame.transform.smoothscale(self.image, (180,250)) #--> helps with image clarity

            # Set & store the book to COMPARE to the answer later
            self.answer = book_ans

            # create a Rect for clickability
            self.rect = self.image.get_rect()



#>>---------------------------------
# INIT
#>>---------------------------------
class BookGame:
    def __init__(self):
        pygame.init()

      # Creating Game window
        WIDTH, HEIGHT = 1000, 680
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.FPS = 60
        pygame.display.set_caption("Game 4: Books Guessing")
        self.clock = pygame.time.Clock()
   
        # dEFINE Background image
        self.background = pygame.image.load(os.path.join("ProjectImages", "kidTOYS_img.jpeg"))
        self.background = pygame.transform.smoothscale(self.background, (WIDTH, HEIGHT)) #--> BACKGROUND image dimensions (x,y)
       
        # Create book LIST to initalize & store book objects
        all_books = [
            BookObjects.Book("Book1", "book1.png"),
            BookObjects.Book("Book2", "book2.png"),
            BookObjects.Book("Book3", "book3.png"),
            BookObjects.Book("Book4", "book4.png"),
            BookObjects.Book("Book5", "book5.png"),
        ]

        # Loading Books & Positioning them
        self.books = all_books  #--> accessing images LIST "Books"
        self.book_positions() #--> call the positioning function

        #----------------------------------------------------------
        # Game Loic VARIABLES
        #----------------------------------------------------------
        # randomized answer
        self.correct_answer = "Book4" #ANSWER FOR BOOKS
        self.guesses_left = 3

        # making message's appear
        self.message = "Click to find which book the kid wants!"

        # Clue responses --> {} is a dictionary, applying a key-value pair (key = Book#, value = Clue)
        self.clues = {
            "Book1": "Plants are boring. Try again!",
            "Book2": "This dog looks weird. Try again!",
            "Book3": "A bunny in a desert? Try again",
            "Book4": "The kid likes sheep!",
            "Book5": "The kid is scared of mice.Try again!",
        }


    # Ending screen:
    def show_message(self, text_string, duration=2000):
        font = pygame.font.SysFont('Arial', 50)
        # Render the text
        text_surface = font.render(text_string, True, (255, 255, 255)) #--> green text

        # Center the text on the screen
        text_rect = text_surface.get_rect(center=(1000 // 2, 680 // 2))

        # Draw the final frame (background + books)
        self.screen.blit(self.background, (0, 0))
        for book in self.books:
            self.screen.blit(book.image, book.rect)

        # Draw the message centered
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()
        pygame.time.delay(duration)


    # positioning the books PLACEMENT MANUALLY
    def book_positions(self):
        #--> targets the specific book by index & places it (x,y)
        self.books[0].rect.topleft = (150, 110)
        self.books[1].rect.topleft = (400, 110)
        self.books[2].rect.topleft = (650, 110)

        # Bottom row (shifted inward to fill the gaps)
        self.books[3].rect.topleft = (275, 410)
        self.books[4].rect.topleft = (525, 410)

#>>--------UPDATE (N/A: No game movement)-----------

    #---------------------------------
    #  MAIN GAME LOOP
    #---------------------------------
    def run(self):
        game_over = False
        show_final_message = True


        while not game_over:
            for event in pygame.event.get():

                # Quit event
                if event.type == pygame.QUIT:
                    show_final_message = False
                    game_over = True
    
                #--> close window with escape
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: 
                        show_final_message = False
                        game_over = True
                   
                # Mouse click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    for book in self.books:
                        if book.rect.collidepoint(mouse_pos):

                            # Correct book
                            if book.answer == self.correct_answer:
                                if self.guesses_left == 3:
                                    self.message = f"WOW! {self.correct_answer}, with the sheep was correct!"
                                else:
                                    self.message = f"{self.correct_answer} is the right book!"
                                game_over = True

                            # Wrong book
                            else:
                                self.guesses_left -= 1
                                self.message = self.clues[book.answer]
                                if self.guesses_left > 0:
                                    self.message += f" ({self.guesses_left} guesses left)"
                                else:
                                    self.message = (
                                        "The kid wanted " + self.correct_answer + ", with the sheep."
                                    )
                                    game_over = True


            # DRAW
            self.screen.blit(self.background, (0, 0))
            for book in self.books:
                self.screen.blit(book.image, book.rect)

            # Draw message during gameplay
            font_small = pygame.font.SysFont("Arial", 30)
            text_surface = font_small.render(self.message, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(500, 40))
            self.screen.blit(text_surface, text_rect)

            # Ending Final message
            if game_over and show_final_message:
                self.show_message(self.message)


            pygame.display.update()
            self.clock.tick(self.FPS)
        return

def run():
    game = BookGame()
    game.run()
    return

if __name__ == "__main__":
    run()