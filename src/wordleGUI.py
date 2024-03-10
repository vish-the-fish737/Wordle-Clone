import pygame
import sys
from src import *

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wordle')
FONT = pygame.font.Font(None, 56)

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (106, 170, 100)
YELLOW = (201, 180, 88)
GRAY = (120, 124, 126)
DARK_MODE_BLACK = (18, 18, 18)
USED_LETTER_COLOR= (50,50,50)  

correct_word = "FAVOR"
guesses = []
current_guess = ""
max_guesses = 6

def draw_letter_boxes():
    box_size = 60  
    box_margin = 20  
    start_x = (SCREEN_WIDTH - (len(correct_word) * (box_size + box_margin) - box_margin)) // 2
    start_y = 60

    for i in range(max_guesses):
        for j in range(len(correct_word)):
            box_x = start_x + j * (box_size + box_margin)
            box_y = start_y + i * (box_size + box_margin)
            pygame.draw.rect(SCREEN, GRAY, (box_x, box_y, box_size, box_size), 3)

def draw_guesses():
    box_size = 60  
    box_margin = 20  
    start_x = (SCREEN_WIDTH - (len(correct_word) * (box_size + box_margin) - box_margin)) // 2  
    start_y = 60  
    
    for i, guess in enumerate(guesses):
        result = tally(correct_word, guess)
        
        for j, letter in enumerate(guess):
            letter_color = BLACK  

            if result[j] == Matches.EXACT_MATCH:
                box_color = GREEN
                letter_color = WHITE  
            elif result[j] == Matches.PARTIAL_MATCH:
                box_color = YELLOW
                letter_color = WHITE
            else:
                box_color = GRAY
                letter_color = WHITE  

            letter_x = start_x + j * (box_size + box_margin)
            letter_y = start_y + i * (box_size + box_margin)
            
            pygame.draw.rect(SCREEN, box_color, (letter_x, letter_y, box_size, box_size))
            
            text = FONT.render(letter, True, letter_color)
            text_rect = text.get_rect(center=(letter_x + box_size / 2, letter_y + box_size / 2))
            SCREEN.blit(text, text_rect)

# def draw_keyboard(guessed_letters):
#     key_width = 50  
#     key_height = 60  
#     key_margin = 5  
#     start_keyboard_x = 20  
#     start_keyboard_y = SCREEN_HEIGHT - 230  

#     keyboard_rows = [
#         " QWERTYUIOP",
#         "  ASDFGHJKL ",
#         "      ZXCVBNM  "
#     ]

#     for row_idx, row in enumerate(keyboard_rows):
#         for key_idx, key in enumerate(row.strip()):
#             key_x = start_keyboard_x + key_idx * (key_width + key_margin) + (len(row) - len(row.strip())) * key_width / 4
#             key_y = start_keyboard_y + row_idx * (key_height + key_margin)
            
#             key_color = GRAY  

#             if key in guessed_letters['correct']:
#                 key_color = GREEN
#             elif key in guessed_letters['present']:
#                 key_color = YELLOW
#             elif key in guessed_letters['absent']:
#                 key_color = USED_LETTER_COLOR  

#             pygame.draw.rect(SCREEN, key_color, (key_x, key_y, key_width, key_height))

#             letter_text = FONT.render(key, True, WHITE)
#             SCREEN.blit(letter_text, (key_x + (key_width - letter_text.get_width()) / 2,
#                                       key_y + (key_height - letter_text.get_height()) / 2))


def draw_current_guess():
    box_size = 60
    box_margin = 20
    start_x = (SCREEN_WIDTH - (len(correct_word) * (box_size + box_margin) - box_margin)) // 2
    current_guess_y = 60 + len(guesses) * (box_size + box_margin) 
    
    for j, letter in enumerate(current_guess):
        letter_x = start_x + j * (box_size + box_margin)
        
        text = FONT.render(letter, True, WHITE)
        text_rect = text.get_rect(center=(letter_x + box_size / 2, current_guess_y + box_size / 2))
        SCREEN.blit(text, text_rect)

def message(num_guesses):
        if num_guesses == 1:
            message = "Amazing!"
        elif num_guesses == 2:
            message = "Splendid!"
        elif num_guesses == 3:
            message = "Awesome!"
        elif num_guesses <= max_guesses:
            message = "Yay!"
        return message
    
def checkGameEnd():
    if guesses[-1] == correct_word:
        message = ""
        num_guesses = len(guesses)

        message = message(num_guesses)

        displayEndMessage(message)
        
        print(message)
        
    elif len(guesses) == max_guesses:
        displayEndMessage("It was {}, better luck next time!".format(correct_word))
        print("Game Over! The word was: {}".format(correct_word))  

def displayEndMessage(message):
    SCREEN.fill(BLACK) 

    font_size = 56
    text = pygame.font.Font(None, font_size).render(message, True, WHITE)
    while text.get_width() > SCREEN_WIDTH - 40:  # Adjusting for margins
        font_size -= 1
        text = pygame.font.Font(None, font_size).render(message, True, WHITE)

    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    SCREEN.blit(text, text_rect)

    restart_text = FONT.render("Restart", True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    SCREEN.blit(restart_text, restart_rect)

    pygame.display.update()

    pygame.time.delay(5000)
    
    return restart_rect

# def updateCurrentGuess(event, current_guess, max_length, game_ended):
#     if not game_ended and event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_BACKSPACE and len(current_guess) > 0:
#             current_guess = current_guess[:-1]
#         elif event.unicode.isalpha() and len(current_guess) < max_length:
#             current_guess += event.unicode.upper()
    
#     return current_guess

# def color():
#     for i, letter in enumerate(current_guess.upper()):
#         if letter == correct_word[i]:  
#             guessed_letters['correct'].add(letter)
#         elif letter in correct_word:
#             guessed_letters['present'].add(letter)
#         else:
#             guessed_letters['absent'].add(letter)

def resetBoard():
    global guesses, current_guess, guessed_letters, game_ended
    guesses.clear()
    current_guess = ""
    guessed_letters = {'correct': set(), 'present': set(), 'absent': set()}
    game_ended = False

def draw_components():
    draw_letter_boxes()
    draw_guesses()
    draw_current_guess()

def restartGame():
    resetBoard()
    main()
    
# def update():
#                 if not game_ended:
#                     if event.key == pygame.K_RETURN and len(current_guess) == len(correct_word):
#                         guesses.append(current_guess.upper())
#                         color()
                        
#                         current_guess = ""
#                         checkGameEnd()  
#                         if len(guesses) > max_guesses or current_guess == correct_word:
#                             print("Game Over")
#                             run = False
#                             game_ended = True
#                     else:
#                         current_guess = updateCurrentGuess(event, current_guess, len(correct_word), game_ended)

def main():
    global current_guess
    guessed_letters = {'correct': set(), 'present': set(), 'absent': set()} 
    run = True
    game_ended = False
    while run:
        SCREEN.fill(DARK_MODE_BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                update()
                
        draw_components()  
        draw_keyboard(guessed_letters) 
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
