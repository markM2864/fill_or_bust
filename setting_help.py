# Filename: setting_help.py
# Author: Mark Maurer
# Date: 6/13/2022
# Version: 1
# Description: Contains the loops for settings and help menus.
from classes_functions import *
# function for running the settings menu screen
def setting_menu(screen, new_font, clock, myGame):
    font = pygame.font.Font('freesansbold.ttf', 20) # smaller font for some text to screen function calls
    score_text = 'SET TARGET SCORE:'
    bot_text = 'SET NUMBER OF BOTS:'
    bot_speed = 'SET BOT SPEED:'
    textToScreen(score_text, screen, font, 150, 100, green, black)
    textToScreen(bot_text, screen, font, 150, 200, green, black)
    textToScreen(bot_speed, screen, font, 150, 300, green, black)
    textToScreen('CURRENT SETTINGS', screen, font, 350, 550, red, black)

    reset_btn = button('RESET TO DEFAULT SETTINGS', 350, 500, font, 1) # button to reset to default settings
    menu_btn = button("MAIN MENU", 70, 20, new_font, 0.5) # button to return to main menu

    score_10k = button('10000', 310, 100, font, 1) # set target to 10k
    score_5k = button('5000', 410, 100, font, 1) # 5k
    score_2_5k = button('2500', 510, 100, font, 1) # 2.5k

    one_bot = button('1', 290, 200, font, 1) # buttons for the number of bots
    two_bot = button('2', 340, 200, font, 1)
    three_bot = button('3', 390, 200, font, 1)
    four_bot = button('4', 440, 200, font, 1)
    five_bot = button('5', 490, 200, font, 1)

    one_hundred = button('100', 290, 300, font, 1) # buttons to set the selection speed of bot in milliseconds
    two_hundred = button('200', 350, 300, font, 1)
    three_hundred = button('300', 410, 300, font, 1)
    four_hundred = button('400', 470, 300, font, 1)
    five_hundred = button('500', 530, 300, font, 1)

    # main loop
    while True:
        # required for loop to make the game check for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # refers to user hitting x in top right
                sys.exit()
        main_menu = menu_btn.draw(screen) # draw on screen and check for button presses for all buttons
        ten_score = score_10k.draw(screen)
        five_score = score_5k.draw(screen)
        two_score = score_2_5k.draw(screen)
        bot_one = one_bot.draw(screen)
        bot_two = two_bot.draw(screen)
        bot_three = three_bot.draw(screen)
        bot_four = four_bot.draw(screen)
        bot_five = five_bot.draw(screen)
        speed1 = one_hundred.draw(screen)
        speed2 = two_hundred.draw(screen)
        speed3 = three_hundred.draw(screen)
        speed4 = four_hundred.draw(screen)
        speed5 = five_hundred.draw(screen)
        reset = reset_btn.draw(screen)

        # display current settings
        settings = 'SCORE: {}  NUMBER OF BOTS: {}  BOT SPEED: {}'.format(myGame.getTargetScore(),
                                                                         myGame.getNumBots(), myGame.getBotSpeed())
        rect = pygame.draw.rect(screen, black, pygame.Rect(50, 580, 600, 35)) # erase previous version
        textNoUpdate(settings, screen, font, 350, 600, red, black) # draw new version
        if main_menu: # return to main menu
            return True

        # perform appropriate button actions
        if ten_score:
            myGame.setTargetScore(10000)
        elif five_score:
            myGame.setTargetScore(5000)
        elif two_score:
            myGame.setTargetScore(2500)
        if bot_one:
            myGame.setNumBots(1)
        elif bot_two:
            myGame.setNumBots(2)
        elif bot_three:
            myGame.setNumBots(3)
        elif bot_four:
            myGame.setNumBots(4)
        elif bot_five:
            myGame.setNumBots(5)
        if speed1:
            myGame.setBotSpeed(100)
        elif speed2:
            myGame.setBotSpeed(200)
        elif speed3:
            myGame.setBotSpeed(300)
        elif speed4:
            myGame.setBotSpeed(400)
        elif speed5:
            myGame.setBotSpeed(500)
        if reset:
            myGame.setTargetScore(10000)
            myGame.setNumBots(1)
            myGame.setBotSpeed(500)
        pygame.display.update()
        clock.tick(30)

# first page of help menu
def help1(screen, clock):
    pygame.time.delay(200)  # delay to make buttons more consistent
    font = pygame.font.Font('freesansbold.ttf', 16)
    big_font = pygame.font.Font('freesansbold.ttf', 32)
    menu_btn = button("MAIN MENU", 70, 20, big_font, 0.5) # main menu button
    next_page = button('NEXT PAGE ->', 600, 600, big_font, 0.5) # button to go to next page of rules
    page = -1
    while True:
        # rules of the game
        textNoUpdate('->RULES OF THE GAME<-', screen, font, 350, 100, red, black)
        textNoUpdate('1) SIX PLAYERS MAXIMUM', screen, font, 350, 130, green, black)
        textNoUpdate('2) BE THE FIRST PLAYER TO REACH THE TARGET SCORE', screen, font, 350, 160, green, black)
        textNoUpdate('3) ONCE THE TARGET SCORE IS REACHED EACH PLAYER GETS ONE MORE TURN', screen, font, 350, 190, green, black)
        textNoUpdate('4) PLAYER WITH THE HIGHEST SCORE WINS', screen, font, 350, 220, green, black)
        textNoUpdate('5) EACH TURN STARTS BY DRAWING A CARD FROM THE DECK', screen, font, 350, 250, green, black)
        textNoUpdate('6) THEN THE DICE ARE ROLLED AND THE PLAYER WILL TRY', screen, font, 350, 280, green, black)
        textNoUpdate('7) TO COMPLETE THE OBJECTIVE OF THE CARD MY CHOOSING CERTAIN DICE', screen, font, 350, 310, green, black)
        textNoUpdate('8) IF YOU ROLL THE DICE AND NO POINTS ARE POSSIBLE, YOU BUST', screen, font, 350, 340, green, black)
        textNoUpdate('9) IF YOU BUST YOU LOSE ALL POINTS FOR THAT TURN', screen, font, 350, 370, green, black)
        textNoUpdate('10) IF YOU ARE ABLE TO COMBINE ALL SIX DICE, THATS A FILL', screen, font, 350, 400, green, black)
        textNoUpdate('11) IF YOU FILL YOU HAVE THE OPTION OF DRAWING ANOTHER CARD', screen, font, 350, 430, green, black)
        textNoUpdate('THERE ARE SIX DIFFERENT KINDS OF CARDS', screen, font, 350, 460, green, black)
        textNoUpdate('BONUS, FILL 1000, VENGEANCE, NO DICE, MUST BUST, AND DOUBLE TROUBLE', screen, font, 350, 490, green, black)
        textNoUpdate('EACH ONE HAS A CERTAIN OBJECTIVE TO COMPLETE', screen, font, 350, 520, green, black)
        for event in pygame.event.get(): # required loop to check for events
            if event.type == pygame.QUIT:  # refers to user hitting x in top right
                sys.exit()
        menu = menu_btn.draw(screen) # draw the button and check for presses
        next = next_page.draw(screen)
        if menu: # go back to main menu
            return True
        if next: # go to the next page
            screen.fill(black) # erase the screen
            next_page.reset() # reset the button
            page = help2(screen, clock) # call for second help page
        if page == 0: # refers to returning to main menu from page 2
            return True
        else:
            pass
        pygame.display.update()
        clock.tick(30)

# second page of help menu
def help2(screen, clock):
    pygame.time.delay(200)
    font = pygame.font.Font('freesansbold.ttf', 14)
    big_font = pygame.font.Font('freesansbold.ttf', 32)
    menu_btn = button("MAIN MENU", 70, 20, big_font, 0.5)
    next_page = button('NEXT PAGE ->', 600, 600, big_font, 0.5)
    next_page.reset() # call to reset since the button is literally the same as page 1
    prev_page = button('<- PREV PAGE', 450, 600, big_font, 0.5) # button to go to previous page
    prev_page.reset() # reset since button is used in next page
    page = -1
    while True:
        # displayes the card types and objectives
        textNoUpdate('->CARD TYPES<-', screen, font, 350, 100, red, black)
        textNoUpdate('BONUS: FILL TO GET THE BONUS ON CARD OR CLICK DONE TO KEEP POINTS (300, 400, 500)', screen, font, 350, 130, green, black)
        textNoUpdate('FILL 1000: FILL TO GET 1000 BONUS POINTS (MUST FILL', screen, font, 350, 160, green, black)
        textNoUpdate('VENGEANCE: FILL TO DEDUCT 2500 POINTS FROM PLAYER WITH MOST POINTS', screen, font, 350, 190, green, black)
        textNoUpdate('VENGEANCE: CAN BE SKIPPED, HIGH SCORE MUST BE MORE THAN 2500 TO USE', screen, font, 350, 220, green, black)
        textNoUpdate('NO DICE: WHO EVER DRAWS THIS CARD HAS THEIR TURN SKIPPED', screen, font, 350, 250, green, black)
        textNoUpdate('NO DICE: WHO EVER DRAW THIS CARD GETS NO POINTS FOR THAT TURN', screen, font, 350, 280, green, black)
        textNoUpdate('MUST BUST: PLAYER CONTINUES ROLLING AND COLLECTING POINTS UNTIL BUSTED', screen, font, 350, 310, green, black)
        textNoUpdate('MUST BUST: PLAYER CAN NOT DRAW ANOTHER CARD AFTER BUSTING', screen, font, 350, 340, green, black)
        textNoUpdate('DOUBLE TROUBLE: PLAYER MUST FILL TWICE TO COMPLETE THIS CARD', screen, font, 350, 370, green, black)
        textNoUpdate('DOUBLE TROUBLE: ONCE FILLED TWICE, POINTS WILL BE DOUBLED', screen, font, 350, 400, green, black)
        textNoUpdate('FOR ANY CARD OTHER THAN MUST BUST, NEW CARDS CAN BE DRAWN ON FILL', screen, font, 350, 430, green, black)
        for event in pygame.event.get(): # required
            if event.type == pygame.QUIT:  # refers to user hitting x in top right
                sys.exit()
        menu = menu_btn.draw(screen)
        next = next_page.draw(screen)
        prev = prev_page.draw(screen)
        if menu or page == 0: # return to main menu
            return 0
        if next: # go to next page
            screen.fill(black)
            next_page.reset()
            prev_page.reset()
            page = help3(screen, clock)
            prev = False
        if prev: # go to prev page
            screen.fill(black)
            prev_page.reset()
            next_page.reset()
            return 2
        pygame.display.update()
        clock.tick(30)

# third help menu page
def help3(screen, clock):
    pygame.time.delay(200)
    font = pygame.font.Font('freesansbold.ttf', 14)
    big_font = pygame.font.Font('freesansbold.ttf', 32)
    menu_btn = button("MAIN MENU", 70, 20, big_font, 0.5)
    prev_page = button('<- PREV PAGE', 450, 600, big_font, 0.5)
    prev_page.reset()
    while True:
        # displays dice combination information
        textNoUpdate('->DICE COMBINATIONS<-', screen, font, 350, 100, red, black)
        textNoUpdate('ALL DICE CAN BE COMBINED INTO A GROUP OF THREE OR SIX', screen, font, 350, 130, green, black)
        textNoUpdate('THREE ONES = 1000, TWOS = 200, THREES = 300, FOURS = 400, FIVES = 500, SIXES = 600', screen, font, 350, 160, green, black)
        textNoUpdate('A GROUP OF SIX IS WORTH DOUBLE THOSE POINTS', screen, font, 350, 190, green, black)
        textNoUpdate('SINGULAR ONES AND FOURS CAN BE COMBINED FOR 50 POINTS', screen, font, 350, 220, green, black)
        textNoUpdate('THIS IS THE SAME FOR TWOS AND THREES', screen, font, 350, 250, green, black)
        textNoUpdate('IF YOU ROLL THE DICE AND GET ONE OF EVERY NUMBER THAT IS A STRAIGHT', screen, font, 350, 280, green, black)
        textNoUpdate('STRAIGHTS ARE WORTH 1500 POINTS', screen, font, 350, 310, green, black)
        for event in pygame.event.get(): # required
            if event.type == pygame.QUIT:  # refers to user hitting x in top right
                sys.exit()
        menu = menu_btn.draw(screen)
        prev = prev_page.draw(screen)
        if menu: # return to main menu
            return 0
        if prev: # prev page
            screen.fill(black)
            prev_page.reset()
            return 1
        pygame.display.update()
        clock.tick(30)
