# Filename: main.py
# Author: Mark Maurer
# Date: 6/13/2022
# Version: 1
# Description: Main game loop, uses pygame module functions and functions from other files.
from setting_help import *
from classes_functions import *
# starting up
pygame.init()
clock = pygame.time.Clock()


pygame.font.init()
size = X, Y = 700, 700
pygame.display.set_caption('Fill or Bust')
screen = pygame.display.set_mode(size)
screen.fill(black)
font = pygame.font.Font('freesansbold.ttf', 32)
textToScreen('Main Menu', screen, font, (X/2), (Y/6), green, black)
fob_img = pygame.image.load('images/fill_or_bust.jpg')
width = fob_img.get_width()
height = fob_img.get_height()
fob_img = pygame.transform.scale(fob_img, (700, 700))
fob_rect = fob_img.get_rect()
screen.blit(fob_img, (0, 0))

stop = False  # boolean for stopping the thread

# buttons for the main menu
ng_btn = button('NEW GAME', X/2, Y/3, font, 1)
stg_btn = button('SETTINGS', X/2, Y/3 + 50, font, 1)
hlp_btn = button('HELP', X/2, Y/3 + 100, font, 1)
exit_btn = button('EXIT', X/2, Y/3 + 150, font, 1)
# button actions
ext_act = False
ng_act = False
hlp_act = False
stg_act = False

done = False
gamedone = False
showplayers = False
game_over = False

myGame = Game(screen, font, X, Y)
while True:
    ext_act = exit_btn.draw(screen)
    ng_act = ng_btn.draw(screen)
    hlp_act = hlp_btn.draw(screen)
    stg_act = stg_btn.draw(screen)
    # this is lower cpu usage, without it usage goes to 30 percent, effectively a debounce effect, may be unnecessary
    if not (ext_act and ng_act and hlp_act and stg_act):
        pygame.event.wait(10)  # wait 100 ms if no button hit

    if ext_act:
        stop = True
        sys.exit()

    if stg_act:
        screen.fill(black)
        yes = setting_menu(screen, font, clock, myGame)
        screen.blit(fob_img, (0, 0))
        stg_btn.reset()

    if hlp_act:
        screen.fill(black)
        help_done = help1(screen, clock)
        screen.blit(fob_img, (0, 0))
        hlp_btn.reset()


    if ng_act:
        screen.fill(black)
        game_over = playGame(screen, clock, myGame)
        screen.fill(black)
        screen.blit(fob_img, (0, 0))
        ng_btn.reset()

    if game_over:
        game_over = False
        over = winScreen(screen, font, clock, myGame)
        screen.blit(fob_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # refers to user hitting x in top right
            stop = True
            sys.exit()
    pygame.display.update()
    clock.tick(30)  # 30 fps to try to minimize flickering
