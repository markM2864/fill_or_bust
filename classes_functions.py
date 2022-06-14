# Filename: classes_functions.py
# Author: Mark Maurer
# Date: 6/13/2022
# Version: 1
# Description: File that contains all classes and most functions used in main loop.
import time
import random
from base_ADT import *
# didn't want to create a new file so just copied colors over
black = 0, 0, 0
white = 255, 255, 255
green = 0, 255, 0
blue = 0, 0, 255
red = 255, 0, 0
brown = 164, 116, 73
lightBrown = 181, 101, 29
sand = 250, 242, 195
# print text to screen
def textToScreen(text, screen, font, x, y, textcolor, backcolor):
    text = font.render(text, True, textcolor, backcolor)
    textBox = text.get_rect()
    textBox.center = (x, y)
    screen.blit(text, textBox)
    pygame.display.update()

# same as above function without update for optimization
def textNoUpdate(text, screen, font, x, y, textcolor, backcolor):
    text = font.render(text, True, textcolor, backcolor)
    textBox = text.get_rect()
    textBox.center = (x, y)
    screen.blit(text, textBox)

# draw rectangle with rounded corners
def roundedRect(screen, color, trc, tlc, rad, width, height):
    pygame.draw.rect(screen, color, pygame.Rect(trc, tlc, width, height))
    pygame.draw.rect(screen, color, pygame.Rect(trc - rad, tlc + rad, width + rad*2, height - rad*2))
    pygame.draw.circle(screen, color, [trc, tlc + rad], rad)
    pygame.draw.circle(screen, color, [trc + width, tlc + rad], rad)
    pygame.draw.circle(screen, color, [trc, tlc + height - rad], rad)
    pygame.draw.circle(screen, color, [trc + width, tlc + height - rad], rad)

# draw a deck, just for shows
def drawDeck(screen, trc, tlc, width, height):
    roundedRect(screen, white,trc + 10, tlc + 10, 2, width, height)
    roundedRect(screen, black, trc + 8, tlc + 8, 2, width, height)
    roundedRect(screen, white, trc + 6, tlc + 6, 2, width, height)
    roundedRect(screen, black, trc + 4, tlc + 4, 2, width, height)
    roundedRect(screen, white, trc + 2, tlc + 2, 2, width, height)
    roundedRect(screen, red, trc, tlc, 2, width, height)

# get player names from the user(s)
def getPlayers(screen, game):
    font = pygame.font.SysFont('arial', 20)
    players = [] # place to hold player names
    ng_txt = "NEW GAME STARTED!!!"
    textToScreen(ng_txt, screen, font, 350 - len(ng_txt)/2, 50, white, black)
    textToScreen("Enter Name: ", screen, font, 300, 180, white, black)
    dn_btn = button('Done?', 600, 100, font, 1) # button to exit loop early if done
    user_text = "" # empty string
    text = font.render(user_text, True, white)
    rect = text.get_rect()
    rect.topleft = (350, 170)
    cursor = pygame.Rect(rect.topright, (3, rect.height)) # creating a cursor
    clock = pygame.time.Clock()
    running = True
    while running:
        done = dn_btn.draw(screen) # draw the button and check for clicks
        if done:
            game.setNumHP(len(players)) # get number of human players
            num = 1 # used for creating bot names
            while len(players) < 1 + game.getNumBots(): # fill the rest of the players with correct number of bots
                players.append("BOT" + str(num))
                num += 1
            game.setPlayers(players) # set the players
            return True
        if len(players) == 6: # six players is max
            game.setPlayers(players)
            return True
        for event in pygame.event.get(): # required
            if event.type == pygame.QUIT: # exiting the window
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # check for key presses
                if event.key == pygame.K_RETURN: # check for enter key
                    players.append(user_text) # add the current text as player name
                    user_text = "" # reset text
                    if len(players) > 0: # display players if len greater than 0
                        y = 450
                        index = 0
                        number = 1
                        for player in players:
                            text = "Player " + str(number) + ": " + player
                            textToScreen(text, screen, font, 350 + len(text), y, white, black)
                            index += 1
                            y += 20
                            number += 1
                if event.key == pygame.K_BACKSPACE: # check for backspaces
                    if len(user_text) > 0:
                        user_text = user_text[:-1]
                elif event.key != pygame.K_RETURN: # check to typing
                    if len(user_text) < 11: # max length of 11 characters
                        user_text += event.unicode
                text = font.render(user_text, True, white)
                rect.size = text.get_size()
                cursor.topleft = rect.topright # set position of cursor
        pygame.draw.rect(screen, black, (350, 170, 200, 25))
        screen.blit(text, rect)
        if time.time() % 1 > 0.5: # makes the cursor blink
            pygame.draw.rect(screen, white, cursor)
        else:
            pygame.draw.rect(screen, black, cursor)
        clock.tick(30)
        pygame.display.flip()

# display player names on screen
def dispPlayers(screen, game):
    font = pygame.font.SysFont('arial', 20)
    players = game.getPlayers()
    turn = game.getTurn()
    rect = pygame.draw.rect(screen, black, pygame.Rect(230, 80, 290, 35))
    textNoUpdate("Player {}'s turn!".format(players[turn]), screen, font, 350, 100, red, black)
    if len(players) >= 1: # check to only display valid names
        textNoUpdate(players[0], screen, font, 300, 140, red, black)
    if len(players) >= 2:
        textNoUpdate(players[1], screen, font, 400, 140, red, black)
    if len(players) >= 3:
        textNoUpdate(players[2], screen, font, 600, 290, red, black)
    if len(players) >= 4:
        textNoUpdate(players[3], screen, font, 400, 445, red, black)
    if len(players) >= 5:
        textNoUpdate(players[4], screen, font, 300, 445, red, black)
    if len(players) >= 6:
        textNoUpdate(players[5], screen, font, 125, 290, red, black)
    return True

# erase previous scores from screen
def eraseScores(screen):
    rect0 = pygame.draw.rect(screen, black, pygame.Rect(200, 155, 300, 30))
    rect2 = pygame.draw.rect(screen, black, pygame.Rect(540, 305, 150, 30))
    rect3 = pygame.draw.rect(screen, black, pygame.Rect(200, 460, 300, 30))
    rect5 = pygame.draw.rect(screen, black, pygame.Rect(25, 305, 160, 30))

# display scores of all players
def dispScores(screen, game):
    font = pygame.font.SysFont('arial', 20)
    players = game.getPlayers()
    scores = game.getScores()
    if len(players) >= 1: # displaying valid player scores
        textNoUpdate("Score: " + str(scores[0]), screen, font, 300, 165, red, black)
    if len(players) >= 2:
        textNoUpdate("Score: " + str(scores[1]), screen, font, 400, 165, red, black)
    if len(players) >= 3:
        textNoUpdate("Score: " + str(scores[2]), screen, font, 600, 315, red, black)
    if len(players) >= 4:
        textNoUpdate("Score: " + str(scores[3]), screen, font, 400, 470, red, black)
    if len(players) >= 5:
        textNoUpdate("Score: " + str(scores[4]), screen, font, 300, 470, red, black)
    if len(players) >= 6:
        textNoUpdate("Score: " + str(scores[5]), screen, font, 125, 315, red, black)


def fill_or_bust(prev_sels, dice):
    score = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for x in range(0, 6, 1): #counting the number of possible choices
        if not prev_sels[x]: #indicates a choice that has not been made, in this case a possible choice
            if dice.getDiceAtIndex(x) == 1:
                ones += 1
            elif dice.getDiceAtIndex(x) == 2:
                twos += 1
            elif dice.getDiceAtIndex(x) == 3:
                threes += 1
            elif dice.getDiceAtIndex(x) == 4:
                fours += 1
            elif dice.getDiceAtIndex(x) == 5:
                fives += 1
            elif dice.getDiceAtIndex(x) == 6:
                sixes += 1
    if ones == twos == threes == fours == fives == sixes == 1:
        return True
    if ones == 6:
        score += 2000
    elif ones == 5 and fours == 1:
        score += 1150
    elif ones == 5:
        score += 1200
    elif ones == 4 and fours == 2:
        score += 300
    elif ones == 4 and fours == 1:
        score += 1050
    elif ones == 4:
        score += 1100
    elif ones == 3 and fours == 2:
        score += 200
    elif ones == 3 and fours == 1:
        score += 250
    elif ones == 3:
        score += 1000
    elif ones == 2 and fours == 2:
        score += 100
    elif ones == 2 and (fours == 1 or fours == 4):
        score += 150
    elif ones == 2:
        score += 200
    elif ones == 1 and (fours == 1 or fours == 4):
        score += 50
    elif ones == 1:
        score += 100

    if fives == 6:
        score += 1000
    elif fives == 5:
        score += 600
    elif fives == 4:
        score += 550
    elif fives == 3:
        score += 500
    elif fives == 2:
        score += 100
    elif fives == 1:
        score += 50

    if sixes == 6:
        score += 1200
    elif sixes >= 3:
        score += 600

    if fours == 6:
        score += 800
    elif fours == 5 and ones == 0:
        score += 400
    elif fours == 4 and ones == 0:
        score += 400
    elif fours == 3:
        score += 400

    if threes == 6:
        score += 600
    elif threes == 4 and ones == 1:
        score += 350
    elif threes == 3:
        score += 300

    if twos == 6:
        score += 400
    elif twos == 4 and threes == 1:
        score += 250
    elif twos == 3:
        score += 200
    elif twos == threes == 2:
        score += 100
    elif twos == 2 and threes == 1:
        score += 50
    elif twos == threes == 1:
        score += 50

    if score == 0:
        return False
    else:
        return True

# check if all dice are selected and f_o_B is true
def filled(selections, f_o_b):
    if selections[0] == selections[1] == selections[2] == selections[3] == selections[4] == selections[5] == f_o_b == True:
        return True
    else:
        return False

# starting procedure for first time through the game loop
def startup(screen, deck, dice, font):
    roundedRect(screen, brown, 200, 200, 10, 320, 225)
    drawDeck(screen, 475, 350, 30, 50)
    card = deck.drawCard(screen, font)
    dice.rollAgain(screen)
    dice.draw(screen)
    first = False
    return [card, first]

def validFill(prev_sels, dice):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    for x in range(0, 6, 1):  # counting the number of possible choices
        if prev_sels[x]:  # indicates a choice that has not been made, in this case a possible choice
            if dice.getDiceAtIndex(x) == 1:
                ones += 1
            elif dice.getDiceAtIndex(x) == 2:
                twos += 1
            elif dice.getDiceAtIndex(x) == 3:
                threes += 1
            elif dice.getDiceAtIndex(x) == 4:
                fours += 1
            elif dice.getDiceAtIndex(x) == 5:
                fives += 1
            elif dice.getDiceAtIndex(x) == 6:
                sixes += 1
    if ones == twos == threes == fours == fives == sixes == 1:
        print('flush')
        return True

    if ones == 6:
        return True
    elif ones == 5 and fours == 1:
        return True
    elif ones == 5:
        ones -= 5
    elif ones == 4 and fours == 1:
        ones -= 4
        fours -= 1
    elif ones == 4 and fours == 2:
        return True
    elif ones == 4:
        ones -= 4
    elif ones == fours == 3:
        return True
    elif ones == 3 and fours == 2:
        ones -= 3
        fours -= 2
    elif ones == 3 and fours == 1:
        ones -= 3
        fours -= 1
    elif ones == 3:
        ones -= 3
    elif ones == fours == 2:
        ones -= 2
        fours -= 2
    elif ones == 2 and (fours == 1 or fours == 4):
        ones -= 2
        fours -= 1
    elif ones == 2:
        ones -= 2
    elif ones == 1 and (fours == 1 or fours == 4):
        ones -= 1
        fours -= 1
    elif ones == 1:
        ones -= 1

    if fives == 6:
        return True
    elif fives == 5:
        fives -= 5
    elif fives == 4:
        fives -= 4
    elif fives == 3:
        fives -= 3
    elif fives == 2:
        fives -= 2
    elif fives == 1:
        fives -= 1

    if sixes == 6:
        return True
    elif sixes == 3:
        sixes -= 3
    elif sixes > 0:
        return False

    if fours == 6:
        return True
    elif fours == 3:
        fours -= 3
    elif fours > 0:
        return False

    if twos == 6:
        return True
    elif twos == 5:
        return False
    elif twos == 4 and threes == 0:
        return False
    elif twos == 4 and threes == 1:
        twos -= 4
        threes -= 1
    elif twos == threes == 3:
        return True
    elif twos == 3:
        twos -= 3
    elif twos == threes == 2:
        twos -= 2
        threes -= 2
    elif twos == 2 and threes == 1:
        twos -= 1
        threes -= 1
    elif twos == threes == 1:
        twos -= 1
        threes -= 1

    if threes == 6:
        return True
    elif threes == 5:
        return False
    elif threes == 4 and twos == 1:
        threes -= 4
        twos -= 1
    elif threes == 4 and twos == 0:
        return False
    elif threes == 3:
        threes -= 3

    total = ones + twos + threes + fours + fives + sixes
    #print(total)
    if total != 0:
        return False
    else:
        return True

# checks if any dice have been selected
def anySelection(sels):
    for selection in sels:
        if selection:
            return True
        else:
            return False

# helper function to determine possible combos of 1's/4's and 2's/3's
def combos(one_two, three_four, x, y, dice, selections, prev_selections):
    multiplier0 = 1 # for 1's and 2's
    multiplier1 = 1 # for 3's and 4's
    if x == 2:
        multiplier0 = 2
    elif x == 1:
        multiplier0 = 10 # is 10 because 3 1's = 1000
    if y == 3:
        multiplier1 = 3
    elif y == 4:
        multiplier1 = 4
    if one_two + three_four > 6: # checks if total is greater than 6, means invalid results
        return 0, selections, one_two, three_four
    if one_two == 6: # checks for simple cases
        return multiplier0 * 2 * 100, [True, True, True, True, True, True], one_two, three_four
    if three_four == 6:
        return multiplier1 * 2 * 100, [True, True, True, True, True, True], one_two, three_four
    score = 0 # score to be added
    count = 0 # count to ensure only 3 dice are used for score
    index = 0 # index for selections
    if one_two >= 3: # for 1's and 2's
        score += (multiplier0 * 100)
        one_two -= 3 # subtract the used dice
        while count < 3 and index < 6:
            if dice.getDiceAtIndex(index) == x and not selections[index] and not prev_selections[index]:
                selections[index] = True # set those locations to true
                count += 1 # count ensures no extra dice are selected, also exits early if possible
            index += 1
    count = 0 # reset
    index = 0
    if three_four >= 3: # check for 3's and 4's, same process as before
        score += (multiplier1 * 100)
        three_four -= 3
        while count < 3 and index < 6:
            if dice.getDiceAtIndex(index) == y and not selections[index] and not prev_selections[index]:
                selections[index] = True
                count += 1
            index += 1
        index = 0
    exit = False # for exiting loop below
    while ((one_two and three_four) > 0) and index < 6: # continue until either one is less than 0
        while index < 6 and not exit: # look for a x value dice to select, these will be combined with y dice
            if dice.getDiceAtIndex(index) == x and not selections[index] and not prev_selections[index]:
                selections[index] = True
                exit = True
            index += 1
        index = 0
        exit = False # reset for next loop
        while index < 6 and not exit:
            if dice.getDiceAtIndex(index) == y and not selections[index] and not prev_selections[index]:
                selections[index] = True
                exit = True
            index += 1
        index = 0
        exit = False
        score += 50
        one_two -= 1 # decrement counters
        three_four -= 1
    if multiplier0 == 10: # specific check for 1's since they are worth 100 each
        index = 0
        exit = False
        while one_two > 0:
            while index < 6 and not exit:
                if dice.getDiceAtIndex(index) == x and not selections[index] and not prev_selections[index]:
                    selections[index] = True
                    exit = True
                index += 1
            index = 0
            exit = False
            score += 100
            one_two -= 1
    return score, selections, one_two, three_four # return the score, selections made, and the counts that remain

# animation that plays when the game is over
def winScreen(screen, font, clock, game):
    menu_btn = button("MAIN MENU", 70, 20, font, 0.5)
    players = game.getPlayers()
    scores = game.getScores()
    max_score = max(scores) # person with highest score wins
    score_index = scores.index(max_score)
    images = [] # to store images
    text_start = 'images/frame_' # every file starts with this text
    text_end = '_delay-0.03s.gif' # and ends with this text
    for x in range(0, 5, 1):
        for y in range(0, 10, 1):
            text_mid = str(x) + str(y) # frame number
            text = text_start + text_mid + text_end
            if x == 4 and y > 5:
                break
            else:
                images.append(pygame.image.load(text)) # combine all parts and load image
    index = 0 # index to display image from collection
    color = 0
    active_color = red
    menu = False
    screen.fill(black) # erase screen
    while True:
        if len(players) != 0:
            textNoUpdate(players[score_index], screen, font, 350, 630, active_color, black)
        textNoUpdate('WINNER!!!', screen, font, 350, 670, active_color, black)
        for event in pygame.event.get(): # required
            if event.type == pygame.QUIT:  # refers to user hitting x in top right
                sys.exit()
        menu = menu_btn.draw(screen)
        image = images[index]
        image = pygame.transform.scale(image, (500, 500))
        rect = image.get_rect()
        rect.topleft = [100, 80]
        screen.blit(image, rect)
        index += 1
        color += 1
        if index > 45 and not menu: # reset index to start animation over
            index = 0
        if menu:
            return True
        if color <= 10: # flash the text different colors
            active_color = green
        elif color <= 20:
            active_color = blue
        elif color <= 30:
            active_color = red
            if color == 30:
                color = 0
        pygame.display.update()
        pygame.time.delay(15)
        clock.tick(30)

# evaluate dice selections to generate score, new selections, and fill or bust bools
def eval(dice, selections, prev_selections, new=False):
    # count for all the dices numbers
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    score = 0
    busted = False
    for x in range(0, 6, 1):  # counting the number of possible choices
        if new == False:
            if not selections[x]:  # only add if the choice had not been taken
                if dice.getDiceAtIndex(x) == 1:
                    ones += 1
                elif dice.getDiceAtIndex(x) == 2:
                    twos += 1
                elif dice.getDiceAtIndex(x) == 3:
                    threes += 1
                elif dice.getDiceAtIndex(x) == 4:
                    fours += 1
                elif dice.getDiceAtIndex(x) == 5:
                    fives += 1
                elif dice.getDiceAtIndex(x) == 6:
                    sixes += 1
        elif new == True:
            if not selections[x] and not prev_selections[x]:  # only add if the choice had not been taken
                if dice.getDiceAtIndex(x) == 1:
                    ones += 1
                elif dice.getDiceAtIndex(x) == 2:
                    twos += 1
                elif dice.getDiceAtIndex(x) == 3:
                    threes += 1
                elif dice.getDiceAtIndex(x) == 4:
                    fours += 1
                elif dice.getDiceAtIndex(x) == 5:
                    fives += 1
                elif dice.getDiceAtIndex(x) == 6:
                    sixes += 1
    # straight means function can be exited early
    if ones == twos == threes == fours == fives == sixes == 1:
        score += 1500
        for x in range(len(selections)):
            selections[x] = True
        return score, selections, True, True

    # temp vars for function call
    temp_score = 0
    new_1 = 0
    new_4 = 0
    temp_score, selections, new_1, new_4 = combos(ones, fours, 1, 4, dice, selections, prev_selections)  # process all ones and fours
    score += temp_score  # add the score from the function call to current score

    # fives are not combined but are always worth points, so they are evaluated for each number 1 - 6
    if fives == 6:
        score += 1000
        for x in range(len(selections)):  # click any dice that was five
            if dice.getDiceAtIndex(x) == 5:
                selections[x] = True
        return score, selections, True, True
    elif fives == 5:
        score += 600
        fives -= 5
    elif fives == 4:
        score += 550
        fives -= 4
    elif fives == 3:
        score += 500
        fives -= 3
    elif fives == 2:
        score += 100
        fives -= 2
    elif fives == 1:
        score += 50
        fives -= 1
    for x in range(len(selections)):  # click any dice that was five
        if dice.getDiceAtIndex(x) == 5:
            selections[x] = True

    # if sixes are 6, function can return early
    if sixes == 6:
        score += 1200
        for x in range(len(selections)):
            selections[x] = True
        return score, selections, True, True
    elif sixes == 3: # only 3 or 6 sixes can give points
        score += 600
        sixes -= 3
        for x in range(len(selections)):
            if dice.getDiceAtIndex(x) == 6:
                selections[x] = True
    temp_score = 0
    new_2 = 0
    new_3 = 0
    temp_score, selections, new_2, new_3 = combos(twos, threes, 2, 3, dice, selections, prev_selections)
    score += temp_score
    total = new_1 + new_2 + new_3 + new_4 + fives + sixes
    if score != 0:
        busted = True
    if total == 0:
        return score, selections, True, busted
    else:
        return score, selections, False, busted

# main loop for playing game
def playGame(screen, clock, myGame):
    font = pygame.font.Font('freesansbold.ttf', 32)
    arial_small = pygame.font.SysFont('arial', 18)
    myDeck = deck() # deck instance
    myDice = dice() # dice instance
    first = True # checking if first time through to get players before starting
    exit_btn = button("EXIT", 650, 25, font, 1)
    menu_btn = button("MAIN MENU", 70, 20, font, 0.5)
    done_btn = button("DONE", 620, 675, font, 0.8)
    dce_sel = button("KEEP+ROLL", 615, 550, font, 0.7)
    drw_agn = button("DRAW", 615, 520, font, 0.7)
    done = False # for done button
    exit = False # for exit button
    selected = False # for select and roll button
    f_o_b = False # determines if filled or busted
    fill = False # determines if filled
    filled_1_k = False # for fill 1000 card
    bonus = False # for bonus cards
    valid = False # checks for valid fill, cant just select all dice
    chosen = False # checks if a player has reached the target score
    veng_taken = False # for vengeance cards
    fill_count = 0 # for double trouble card
    score = 0 # players score
    high_score = max(myGame.getScores())
    currentscore = 0 # current dice score before select and roll or busting
    dummy = [False, False, False, False, False, False]
    prev_sels = myDice.getSelections() # previous selections before select and roll
    getPlayers(screen, myGame) # call to getPlayers function
    screen.fill(black) # erase screen
    card = None # declared card as none initially
    fnl_plyr = 0 # a count for ending the game
    while fnl_plyr < len(myGame.getPlayers()) - 1:
        for event in pygame.event.get(): # required
            if event.type == pygame.QUIT:  # refers to user hitting x in top right
                sys.exit()
        dispPlayers(screen, myGame)
        dispScores(screen, myGame)
        exit = exit_btn.draw(screen) # exit and menu buttons should always be visible
        menu = menu_btn.draw(screen)
        if menu: # return to main menu
            return False
        if exit: # exits the game
            sys.exit()
        if first:
            card, first = startup(screen, myDeck, myDice, font) # perform startup
            temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False) # only f_o_b needed
        else:
            done = done_btn.draw(screen) # done button, may be erased later
            fill = filled(myDice.getSelections(), f_o_b) # test for a fill
            ready = validFill(myDice.getSelections(), myDice)
            if fill: # test for a valid fill
                valid = validFill(myDice.getSelections(), myDice)
            else:
                valid = False
            draw = drw_agn.draw(screen) # draw the draw card button, may be erased later
            # testing whether or not to erase the done button
            if ((myGame.getTurn() > myGame.getNumHP() - 1) or myGame.getNumHP() == 0):
                rect = pygame.draw.rect(screen, black, pygame.Rect(575, 660, 100, 30))
                done = False
            elif card.getType() == 'Must Bust':
                rect = pygame.draw.rect(screen, black, pygame.Rect(575, 660, 100, 30))
                done = False
            elif card.getType() == 'Double Trouble' and fill_count != 2:
                rect = pygame.draw.rect(screen, black, pygame.Rect(575, 660, 100, 30))
                done = False
            elif card.getType() == 'Fill' and not valid:
                rect = pygame.draw.rect(screen, black, pygame.Rect(575, 660, 100, 30))
                done = False
            elif card.getType() == 'Vengeance' and not valid:
                rect = pygame.draw.rect(screen, black, pygame.Rect(575, 660, 100, 30))
                done = False
            elif card.getType() == 'Bonus' and currentscore == 0 and score == 0:
                rect = pygame.draw.rect(screen, black, pygame.Rect(575, 660, 100, 30))
                done = False
            # testing whether or not to erase select and roll button
            if currentscore > 0 and ready and not fill:
                selected = dce_sel.draw(screen)
            else:
                selected = False
                rect = pygame.draw.rect(screen, black, pygame.Rect(545, 540, 150, 25))
            # testing whether or not to erase draw button
            if ((myGame.getTurn() > myGame.getNumHP() - 1) or myGame.getNumHP() == 0):
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            elif card.getType() == 'Vengeance' and score > 0 and not valid:
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            elif card.getType() == 'Double Trouble' and fill_count != 2:
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            elif card.getType() == 'Must Bust':
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            elif card.getType() == 'Fill' and not valid:
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            elif card.getType() == 'No Dice':
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            elif card.getType() == 'Bonus' and not valid and not fill:
                rect = pygame.draw.rect(screen, black, pygame.Rect(580, 505, 80, 30))
                draw = False
            # bot selection code
            if ((myGame.getTurn() > myGame.getNumHP() - 1) or myGame.getNumHP() == 0) and not card.getType() == 'No Dice':
                new_selections = [False, False, False, False, False, False]
                temp, new_selections, dummy[0], temp_fill = eval(myDice, new_selections, prev_sels, True) # evaluate dice selections
                text = 'BOT SELECTING DICE'
                textToScreen(text, screen, arial_small, 325, 510, white, black) # display text to indicate bot working
                if temp > 0: # skip process if no score possible
                    for x in range(len(new_selections)):
                        if new_selections[x]: # select dice
                            myDice.selectDice(x, screen)
                        if x % 2 == 0: # change color between blue and white
                            textToScreen(text, screen, arial_small, 325, 510, white, black)
                        else:
                            textToScreen(text, screen, arial_small, 325, 510, blue, black)
                        currentscore = evalSel(prev_sels, myDice.getSelections(), myDice) # get the current score
                        if card.getType() == 'Double Trouble' and fill_count == 2:
                            currentscore = 0
                        rect = pygame.draw.rect(screen, black, pygame.Rect(55, 525, 470, 50)) # erase displayed score
                        score_text = "Score To Be Added: {}".format(score + currentscore)
                        textNoUpdate(score_text, screen, font, 335 - len(text) / 2, 550, white, black) # display score
                        myDice.draw(screen) # draw dice to screen
                        pygame.display.update()
                        pygame.time.delay(myGame.getBotSpeed()) # determines bot speed from settings
                currentscore = evalSel(prev_sels, myDice.getSelections(), myDice)
                rect = pygame.draw.rect(screen, black, pygame.Rect(55, 525, 470, 50))
                score_text = "Score To Be Added: {}".format(score + currentscore)
                textNoUpdate(score_text, screen, font, 335 - len(text) / 2, 550, white, black)  # display score
                myDice.draw(screen)  # draw dice to screen
                pygame.display.update()
                if card.getType() == 'Double Trouble' and fill_count == 2: # check for double trouble card only
                    currentscore = 0
                rect = pygame.draw.rect(screen, black, pygame.Rect(55, 525, 470, 50))
                score_text = "Score To Be Added: {}".format(score + currentscore)
                textNoUpdate(score_text, screen, font, 335 - len(text) / 2, 550, white, black)
                prev_sels = myDice.getSelections() # get new selections
                textToScreen(text, screen, arial_small, 325, 510, black, black)
                fill = (prev_sels[0] and prev_sels[1] and prev_sels[2] and prev_sels[3] and prev_sels[4] and prev_sels[5])
                valid = fill
                # determine the correct button responses
                if fill:
                    done = True
                    selected = False
                    f_o_b = True
                elif currentscore > 0:
                    done = False
                    selected = True
                    f_o_b = True
                elif not fill and currentscore == 0:
                    done = False
                    selected = False
                    f_o_b = False
            # draw a new card
            if draw:
                score += currentscore
                card = myDeck.drawCard(screen, font) # draw a new card
                myDice.resetDice() # reset dice
                prev_sels = myDice.getSelections() # reset selections
                myDice.rollAgain(screen) # roll the dice
                temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False) # check for bust
                selected = False # reset vars for other card types
                filled_1_k = False
                fill = False
                fill_count = 0
                bonus = False
                veng_taken = False
            # for double trouble cards
            if card.getType() == 'Double Trouble' and fill and valid and fill_count < 2:
                fill_count += 1
                score += currentscore
                if fill_count == 1: # reset to start next fill
                    myDice.resetDice()
                    prev_sels = myDice.getSelections()
                    myDice.rollAgain(screen)
                    temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False) # check for bust
                    selected = False
                elif fill_count == 2:
                    score *= 2
                    selected = False
            # for must bust cards
            if card.getType() == 'Must Bust':
                if fill and valid and f_o_b: # reset to continue till busting
                    score += currentscore
                    myDice.resetDice()
                    myDice.rollAgain(screen)
                    temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                    prev_sels = myDice.getSelections()
                    selected = False
                if not f_o_b: # busting reset no draw for must bust cards
                    score += currentscore
                    myGame.setScore(myGame.getTurn(), score)
                    myGame.nextTurn()
                    myDice.resetDice()
                    myDice.rollAgain(screen)
                    temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                    prev_sels = myDice.getSelections()
                    text = "Score To Be Added: {}  ".format(score)
                    textNoUpdate(text, screen, font, 335 - len(str(score)) / 2, 550, black, black)
                    score = 0
                    currentscore = 0
                    selected = False
                    card = myDeck.drawCard(screen, font)
                    if chosen: # increment if last round
                        fnl_plyr += 1
            # for no dice cards, reset everything, no score added
            if card.getType() == 'No Dice':
                rect = pygame.draw.rect(screen, black, pygame.Rect(75, 525, 450, 50))
                score = 0
                currentscore = 0
                selected = False
                fill = False
                bonus = False
                veng_taken = False
                fill_count = 0
                myDice.resetDice()
                myGame.nextTurn()
                prev_sels = myDice.getSelections()
                count = 0
                text = 'NO DICE TURN SKIPPED!!!' # display to let player know what happened
                textToScreen(text, screen, font, 300, 550, white, black)
                while count < 5:
                    pygame.time.delay(450)
                    count += 1
                    if count % 2 != 0: # flash red and white
                        textToScreen(text, screen, font, 300, 550, red, black)
                    else:
                        textToScreen(text, screen, font, 300, 550, white, black)
                textToScreen(text, screen, font, 300, 550, black, black)
                card = myDeck.drawCard(screen, font)
                myDice.rollAgain(screen)
                temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                if chosen:
                    fnl_plyr += 1
            # for fill 1000 cards
            if card.getType() == 'Fill' and fill and valid and not filled_1_k:
                score += 1000
                filled_1_k = True
                selected = False
            # for vengeance cards
            if card.getType() == 'Vengeance' and not veng_taken:
                scores = myGame.getScores()
                max_score = max(scores)
                turn = myGame.getTurn()
                if max_score < 2500: # dont use card if no score high enough
                    card = myDeck.drawCard(screen, font)
                    myDice.rollAgain(screen)
                    temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                    selected = False
                elif scores[turn] == max_score: # dont use card if player who draws has max score
                    card = myDeck.drawCard(screen, font)
                    myDice.rollAgain(screen)
                    temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                    selected = False
                elif fill and valid and max_score > 2500 and (scores[turn] != max_score):
                    for x in range(len(scores)):
                        if scores[x] == max_score and x != turn: # if filled, reduce players with that score
                            temp = scores[x] - 2500
                            myGame.setScore(x, -2500)
                    eraseScores(screen) # needed when lowering scores
                    selected = False
                    veng_taken = True
            # busted, reset everything, no score added
            if not f_o_b and (card.getType() != 'Must Bust') and not fill:
                rect = pygame.draw.rect(screen, black, pygame.Rect(75, 525, 450, 50))
                score = 0
                currentscore = 0
                selected = False
                veng_taken = False
                myDice.resetDice()
                myGame.nextTurn() # switch to next player
                prev_sels = myDice.getSelections()
                count = 0
                text = 'BUSTED!!!'
                textToScreen(text, screen, font, 275, 550, white, black)
                while count < 5:
                    pygame.time.delay(300)
                    count += 1
                    if count % 2 != 0: # flashes like no dice
                        textToScreen(text, screen, font, 275, 550, red, black)
                    else:
                        textToScreen(text, screen, font, 275, 550, white, black)
                textToScreen(text, screen, font, 275, 550, black, black)
                card = myDeck.drawCard(screen, font)
                myDice.rollAgain(screen)
                temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                if chosen:
                    fnl_plyr += 1
            # bonus cards
            if card.getType() == 'Bonus' and fill and valid and not bonus:
                score += card.getBonus()
                bonus = True
                selected = False
            # for select and roll button
            if selected and not fill:
                selected = False
                score += currentscore
                prev_sels = myDice.getSelections() # get current selections
                myDice.rollAgain(screen) # roll dice again
                temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
            myDice.draw(screen) # draw the dice on the screen
            if not done: # update score displayed as long as player isnt done
                currentscore = evalSel(prev_sels, myDice.getSelections(), myDice)
                if card.getType() == 'Double Trouble' and fill_count == 2:
                    currentscore = 0
                rect = pygame.draw.rect(screen, black, pygame.Rect(75, 525, 450, 50))
                text = "Score To Be Added: {}".format(score + currentscore)
                textNoUpdate(text, screen, font, 335 - len(text)/2, 550, white, black)
            # for when players are done
            elif done and f_o_b and (card.getType() == 'Bonus' or card.getType() == 'Fill' or (card.getType() == 'Double Trouble' and fill_count == 2) or card.getType() == 'Vengeance'):
                final = score + currentscore
                myGame.setScore(myGame.getTurn(), final) # set the score for that player
                myGame.nextTurn() # go to next player
                myDice.resetDice()
                prev_sels = myDice.getSelections()
                myDice.rollAgain(screen)
                text = "Score To Be Added: {}  ".format(final)
                textNoUpdate(text, screen, font, 335 - len(str(score)) / 2, 550, black, black) # erase score
                score = 0
                currentscore = 0
                fill_count = 0
                selected = False
                filled_1_k = False
                bonus = False
                veng_taken = False
                card = myDeck.drawCard(screen, font)
                temp, dummy, dummy[0], f_o_b = eval(myDice, myDice.getSelections(), prev_sels, False)
                if chosen:
                    fnl_plyr += 1
        selected = False # always reset to avoid auto rolling
        high_score = max(myGame.getScores()) # get high score
        if high_score > myGame.getTargetScore():
            chosen = True
        elif high_score < myGame.getTargetScore():
            fnl_plyr = 0
            chosen = False
        pygame.display.update()
        clock.tick(30)
    return True

class deck:
    def __init__(self):
        self.vCard = pygame.image.load('images/vengence.PNG') # load all the images from folder
        self.ndCard = pygame.image.load('images/nodice.PNG')
        self.mbCard = pygame.image.load('images/mustbust.PNG')
        self.f1kCard = pygame.image.load('images/fill1000.PNG')
        self.dtCard = pygame.image.load('images/doubletrouble.PNG')
        self.b3Card = pygame.image.load('images/bonus300.PNG')
        self.b4Card = pygame.image.load('images/bonus400.PNG')
        self.b5Card = pygame.image.load('images/bonus500.PNG')
        self.vw = self.vCard.get_width() # this is the width and height that the other cards scale to
        self.vh = self.vCard.get_height()
        self.scaleCards()
        self.cards = []
        self.build()
        self.shuffle() # shuffling twice seemed to create a better distribution
        self.shuffle()

    # shuffles the cards in the deck
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # used from original class to print card types to console
    def printDeck(self):
        print("Size of deck is: {}".format(len(self.cards)))
        for card in self.cards:
            print(card.getType())

    # draws a card from the deck and displays to screen
    def drawCard(self, screen, font):
        count = 0
        text = 'Drawing Card'
        textToScreen("NEW CARD DRAWN", screen, font, 350, 50, black, black) # erase previous text
        while count < 5: # loop creates a changing text
            textToScreen(text, screen, font, 350, 50, white, black)
            text += '.'
            count += 1
            pygame.time.delay(200)
        textToScreen("NEW CARD DRAWN", screen, font, 350, 50, white, black) # display new text after loop is done
        roundedRect(screen, white, 310, 205, 10, int((self.vw - 10) * 0.8), int((self.vh + 10) * 0.8)) # the actual card
        card = self.cards.pop() # get a card from the deck
        type = card.getType() # display the right image depending on the card type
        if type == 'Bonus':
            bonus = card.getBonus()
            if bonus == 300:
                screen.blit(self.b3Card, (305, 210))
            elif bonus == 400:
                screen.blit(self.b4Card, (305, 210))
            elif bonus == 500:
                screen.blit(self.b5Card, (305, 210))
        elif type == 'No Dice':
            screen.blit(self.ndCard, (305, 210))
        elif type == 'Must Bust':
            screen.blit(self.mbCard, (305, 210))
        elif type == 'Fill':
            screen.blit(self.f1kCard, (305, 210))
        elif type == 'Vengeance':
            screen.blit(self.vCard, (305, 210))
        elif type == 'Double Trouble':
            screen.blit(self.dtCard, (305, 210))
        if len(self.cards) == 0: # rebuilds deck if no more cards remain after drawing new card
            self.rebuild()
            print("Deck rebuilt")
        return card

    # the images were not all the same size, this scales each one to the same size
    def scaleCards(self):
        self.b3Card = pygame.transform.scale(self.b3Card, (115, 199))
        self.b4Card = pygame.transform.scale(self.b4Card, (115, 199))
        self.b5Card = pygame.transform.scale(self.b5Card, (115, 199))
        self.ndCard = pygame.transform.scale(self.ndCard, (115, 199))
        self.mbCard = pygame.transform.scale(self.mbCard, (115, 199))
        self.f1kCard = pygame.transform.scale(self.f1kCard, (115, 199))
        self.vCard = pygame.transform.scale(self.vCard, (115, 199))
        self.dtCard = pygame.transform.scale(self.dtCard, (115, 199))

    # build the deck, 54 cards in total
    def build(self):
        for x in range(1, 55, 1):
            if x <= 12:
                self.cards.append(cardBonus(300))
            elif x <= 22:
                self.cards.append(cardBonus(400))
            elif x <= 30:
                self.cards.append(cardBonus(500))
            elif x <= 38:
                self.cards.append(cardNoDice())
            elif x <= 44:
                self.cards.append(cardFill())
            elif x <= 48:
                self.cards.append(cardMustBust())
            elif x <= 52:
                self.cards.append(cardVeng())
            elif x <= 54:
                self.cards.append(cardDT())

    # rebuild the deck if all cards have been drawn
    def rebuild(self):
        del self.cards
        self.cards = []
        self.build()

# different class for each card type, all conform to same interface but others have additional values
class cardBonus:
    def __init__(self, bonus):
        self.bonus = bonus
        self.drawn = False

    def getType(self):
        return 'Bonus'

    def getBonus(self):
        return self.bonus

    def draw(self):
        self.drawn = True

    def isDrawn(self):
        return self.drawn

    def reset(self):
        self.drawn = False

class cardNoDice:
    def __init__(self):
        self.drawn = False

    def getType(self):
        return 'No Dice'

    def draw(self):
        self.drawn = True

    def isDrawn(self):
        return self.drawn

    def reset(self):
        self.drawn = False

class cardFill:
    def __init__(self):
        self.drawn = False

    def getType(self):
        return 'Fill'

    def draw(self):
        self.drawn = True

    def isDrawn(self):
        return self.drawn

    def reset(self):
        self.drawn = False

class cardMustBust:
    def __init__(self):
        self.drawn = False

    def getType(self):
        return 'Must Bust'

    def draw(self):
        self.drawn = True

    def isDrawn(self):
        return self.drawn

    def reset(self):
        self.drawn = False

class cardVeng:
    def __init__(self):
        self.drawn = False

    def getType(self):
        return 'Vengeance'

    def draw(self):
        self.drawn = True

    def isDrawn(self):
        return self.drawn

    def reset(self):
        self.drawn = False

class cardDT:
    def __init__(self):
        self.drawn = False

    def getType(self):
        return 'Double Trouble'

    def draw(self):
        self.drawn = True

    def isDrawn(self):
        return self.drawn

    def reset(self):
        self.drawn = False

class dice:
    def __init__(self):
        self.lock_one = False # bools for locking the dice between rolls
        self.lock_two = False
        self.lock_three = False
        self.lock_four = False
        self.lock_five = False
        self.lock_six = False
        self.rolled = False
        self.pressed0 = False
        self.pressed1 = False
        self.pressed2 = False
        self.pressed3 = False
        self.pressed4 = False
        self.pressed5 = False
        self.dice = []
        for x in range(1, 7, 1):
            self.dice.append(int(6))
        self.roll()
        self.dice0 = diceButton(60, 600) # create dice buttons at those locations
        self.dice1 = diceButton(140, 600)
        self.dice2 = diceButton(220, 600)
        self.dice3 = diceButton(300, 600)
        self.dice4 = diceButton(380, 600)
        self.dice5 = diceButton(460, 600)
        self.dice_buttons = [self.dice0, self.dice1, self.dice2, self.dice3, self.dice4, self.dice5] # create array

    # roll the dice, uses random
    def roll(self):
        selections = [self.pressed0, self.pressed1, self.pressed2, self.pressed3, self.pressed4, self.pressed5]
        for x in range(0, 6, 1):
           if selections[x]: # only roll dice that haven't been selected
               self.dice[x] = self.dice[x]
           else:
               self.dice[x] = random.randint(1, 6) # random int between 1 and 6

    # get all dice numbers
    def getDice(self):
        return self.dice

    # draw the dice on the screen
    def draw(self, screen):
        if self.lock_one: # only draw if not locked
            pass
        else:
            self.pressed0 = self.dice0.draw(screen, self.dice[0])
        if self.lock_two:
            pass
        else:
            self.pressed1 = self.dice1.draw(screen, self.dice[1])
        if self.lock_three:
            pass
        else:
            self.pressed2 = self.dice2.draw(screen, self.dice[2])
        if self.lock_four:
            pass
        else:
            self.pressed3 = self.dice3.draw(screen, self.dice[3])
        if self.lock_five:
            pass
        else:
            self.pressed4 = self.dice4.draw(screen, self.dice[4])
        if self.lock_six:
            pass
        else:
            self.pressed5 = self.dice5.draw(screen, self.dice[5])

    # lock the dice if selected
    def diceLock(self):
        if self.pressed0 and self.rolled:
            self.lock_one = True
        if self.pressed1 and self.rolled:
            self.lock_two = True
        if self.pressed2 and self.rolled:
            self.lock_three = True
        if self.pressed3 and self.rolled:
            self.lock_four = True
        if self.pressed4 and self.rolled:
            self.lock_five = True
        if self.pressed5 and self.rolled:
            self.lock_six = True

    # rolls the dice and displays a message on the screen, short animation
    def rollAgain(self, screen):
        font = pygame.font.Font('freesansbold.ttf', 20)
        self.rolled = True # used in diceLock
        self.diceLock()
        count = 0
        text = "ROLLING"
        textToScreen(text, screen, font, 625, 600, white, black)
        while count < 5:
            self.roll()
            text += '.'
            textToScreen(text, screen, font, 625, 600, white, black)
            self.draw(screen)
            pygame.display.update()
            pygame.time.delay(100)
            count += 1
        textToScreen(text, screen, font, 625, 600, black, black)
        self.rolled = False

    # only resets rolled value
    def reset(self):
        self.rolled = False

    # reset all the dice boolean values
    def resetDice(self):
        self.lock_one = False
        self.lock_two = False
        self.lock_three = False
        self.lock_four = False
        self.lock_five = False
        self.lock_six = False
        self.rolled = False
        self.pressed0 = False
        self.pressed1 = False
        self.pressed2 = False
        self.pressed3 = False
        self.pressed4 = False
        self.pressed5 = False
        self.dice0.reset()
        self.dice1.reset()
        self.dice2.reset()
        self.dice3.reset()
        self.dice4.reset()
        self.dice5.reset()

    # get the bool value of rolled
    def getRolled(self):
        return self.rolled

    # get the dice that have been selected
    def getSelections(self):
        return [self.pressed0, self.pressed1, self.pressed2, self.pressed3, self.pressed4, self.pressed5]

    # get the dice value at that index
    def getDiceAtIndex(self, index):
        return self.dice[index]

    # get number of dice selected
    def diceSelCount(self):
        count = 0
        selections = [self.pressed0, self.pressed1, self.pressed2, self.pressed3, self.pressed4, self.pressed5]
        for sel in selections:
            if sel:
                count += 1
        return count

    # used by the bot selections to selected a dice like the player would
    def selectDice(self, index, screen):
        buttons = [self.dice0, self.dice1, self.dice2, self.dice3, self.dice4, self.dice5]
        buttons[index].click() # select that dice button

# dice button class, all dice are buttons and can be selected
class diceButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.clicked = False

    # draws the dice button to the screen
    def draw(self, screen, num):
        rect = pygame.draw.rect(screen, white, pygame.Rect(self.x, self.y, 46, 50))
        pos = pygame.mouse.get_pos()
        color = black
        if rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]: # check if button was selected
            self.clicked = not self.clicked
            pygame.time.delay(175)  # debounce, useful if not using mouse
        if self.clicked:
            color = green
        else:
            color = black
        roundedRect(screen, white, self.x, self.y, 3, 46, 50)
        if num == 1: # number of dots and locations of dots determined by dice number
            pygame.draw.circle(screen, color, (self.x + 23, self.y + 25), 6)  # middle
        elif num == 2:
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 8), 6)  # top right
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 42), 6)  # top left
        elif num == 3:
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 23, self.y + 25), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 42), 6)
        elif num == 4:
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 42), 6)
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 42), 6)
        elif num == 5:
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 42), 6)
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 42), 6)
            pygame.draw.circle(screen, color, (self.x + 23, self.y + 25), 6)
        elif num == 6:
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 8), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 42), 6)
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 42), 6)
            pygame.draw.circle(screen, color, (self.x + 5, self.y + 25), 6)
            pygame.draw.circle(screen, color, (self.x + 40, self.y + 25), 6)
        return self.clicked

    # reset the clicked value
    def reset(self):
        self.clicked = False

    # used by the bot to automatically select the dice
    def click(self):
        self.clicked = True


def evalSel(prev_sels, selections, dice):
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    score = 0
    for x in range(0, 6, 1):  # counting the number of possible choices
        if selections[x] and not prev_sels[x]:
            if dice.getDiceAtIndex(x) == 1:
                ones += 1
            elif dice.getDiceAtIndex(x) == 2:
                twos += 1
            elif dice.getDiceAtIndex(x) == 3:
                threes += 1
            elif dice.getDiceAtIndex(x) == 4:
                fours += 1
            elif dice.getDiceAtIndex(x) == 5:
                fives += 1
            elif dice.getDiceAtIndex(x) == 6:
                sixes += 1

    if ones == twos == threes == fours == fives == sixes == 1:
        score += 1500
        for x in range(len(selections)):
            selections[x] = True
        return score
    temp_score = 0
    temp_1 = 0
    temp_4 = 0
    temp_score, selections, temp_1, temp_4 = combos(ones, fours, 1, 4, dice, selections, prev_sels)
    score += temp_score
    if fives == 6:
        score += 1000
    elif fives == 5:
        score += 600
    elif fives == 4:
        score += 550
    elif fives == 3:
        score += 500
    elif fives == 2:
        score += 100
    elif fives == 1:
        score += 50

    for x in range(len(selections)):
        if dice.getDiceAtIndex(x) == 5:
            selections[x] = True

    if sixes == 6:
        score += 1200
        for x in range(len(selections)):
            selections[x] = True
        return score
    elif sixes == 3:
        score += 600
        for x in range(len(selections)):
            if dice.getDiceAtIndex(x) == 6:
                selections[x] = True
    temp_score = 0
    temp_2 = 0
    temp_3 = 0
    temp_score, selections, temp_2, temp_3 = combos(twos, threes, 2, 3, dice, selections, prev_sels)
    score += temp_score

    return score

# main game class
class Game(base):

    def __init__(self, screen, font, X, Y):
        self.font = font
        self.screen = screen
        self.mouse = pygame.mouse.get_pos()
        self.size = X, Y
        self.stop = False
        self.players = [] # list to hold player names
        self.num_hp = 0 # number of human players
        self.scores = [0, 0, 0, 0, 0, 0] # scores
        self.turn = 0 # index used to determine whose turn it is
        self.target_score = 10000 # default settings
        self.num_bots = 1
        self.bot_speed = 500

    def setTargetScore(self, score):
        self.target_score = score

    def getTargetScore(self):
        return self.target_score

    def setNumBots(self, number):
        self.num_bots = number

    def getNumBots(self):
        return self.num_bots

    def setBotSpeed(self, speed):
        self.bot_speed = speed

    def getBotSpeed(self):
        return self.bot_speed

    def setPlayers(self, players):
        self.players = players

    def setNumHP(self, value):
        self.num_hp = value

    def getNumHP(self):
        return self.num_hp

    def getPlayers(self):
        return self.players

    def getScores(self):
        return self.scores

    def setScore(self, index, value):
        self.scores[index] += value

    def getTurn(self):
        return self.turn

    def nextTurn(self):
        if self.turn < len(self.players) - 1:
            self.turn += 1
        else:
            self.turn = 0

    def setStop(self, stop):
        self.stop = stop

    def getScreen(self):
        return self.screen

    def getFont(self):
        return self.font

# button class used in main menu and all parts of the game
class button:
    def __init__(self, text, x, y, font, scale):
        self.x = x
        self.y = y
        self.orgText = text # original text
        self.scale = scale # makes the button bigger or smalled
        self.text = text # may be changed with other function calls
        self.font = font
        self.text = font.render(text, True, white, black)
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)
        self.clicked = False # boolean to check for button clicks
        self.width = self.text.get_width()
        self.height = self.text.get_height()
        self.text = pygame.transform.scale(self.text, (int(self.width*scale), int(self.height*scale))) # scale text

    def draw(self, screen,active=green, nonactive=white):
        pos = pygame.mouse.get_pos() # get mouse position
        active_color = active
        nonactive_color = nonactive
        if self.rect.collidepoint(pos):
            # changes color to indicate when mouse is over button
            self.text = self.font.render(self.orgText, True, active_color, black)
            self.text = pygame.transform.scale(self.text, (int(self.width*self.scale), int(self.height*self.scale)))
        else:
            self.text = self.font.render(self.orgText, True, nonactive_color, black)
            self.text = pygame.transform.scale(self.text, (int(self.width * self.scale), int(self.height * self.scale)))
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True # button clicked
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False # button not clicked
        self.rect = self.text.get_rect() # get the rect again
        self.rect.center = (self.x, self.y) # reset the center
        screen.blit(self.text, self.rect) # draw to screen
        return self.clicked # return the clicked valued

    def reset(self):
        self.clicked = False