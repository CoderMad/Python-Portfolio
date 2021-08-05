import random, pygame, sys
from pygame.locals import *

FPS = 30
WindowWidth = 640
WindowHeight = 480
RevealSpeed = 8
BoxSize = 40
GapSize = 10
BoardWidth = 10
BoardHeight = 7
assert (BoardWidth * BoardHeight) % 2 == 0, 'Board needs to have an even number of boxes for pair of matches.'
Xmargin = int((WindowWidth - (BoardWidth * (BoxSize + GapSize))) / 2)
Ymargin = int((WindowHeight - (BoardHeight * (BoxSize + GapSize))) / 2)

#color       R    G    B
GREY     = (100, 100, 100)
NAVYBLUE = (60,  60,  100)
WHITE    = (255, 255, 255)
RED      = (255, 0,   0)
GREEN    = (0,   255, 0)
BLUE     = (0,   0,   255)
YELLOW   = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BgColor = NAVYBLUE
LightBgColor = GREY
BoxColor = WHITE
HighlightColor = BLUE

Donut = 'donut'
Square = 'square'
Diamond = 'diamond'
Lines = 'lines'
Oval = 'oval'

AllColors = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
AllShapes = (Donut, Square, Diamond, Lines, Oval)
assert len(AllColors) * len(AllShapes) * 2 >= BoardWidth * BoardHeight, "Board is too big for the number of " \
                                                                        "shapes/colors defined"


def main():
    global FPSClock, DisplaySurf
    pygame.init()
    FPSClock = pygame.time.Clock()
    DisplaySurf = pygame.display.set_mode((WindowWidth, WindowHeight))

    mousex = 0 #to store x coord for mouse event
    mousey = 0 #to store y coord for mouse event
    pygame.display.set_caption('Memory Puzzle')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None #stores (x, y) of first box clicked

    DisplaySurf.fill(BgColor)
    startGameAnimation(mainBoard)

    while True:
        mouseClicked = False

        DisplaySurf.fill(BgColor)
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)

        if boxx != None and boxy != None:
            #Mouse is currently over box
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True #set the box as revealed

                if firstSelection == None: #the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else:
                    icon1shape, icon1color = getShapeColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        #icons dont match. Recover up both selections
                        pygame.time.wait(1000)
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                    elif hasWon(revealedBoxes): #check if all pairs found
                        gameWonAnimation(mainBoard)
                        pygame.time.wait(2000)

                        #Reset the board
                        mainBoard = getRandomizedBoard()
                        revealedBoxes = generateRevealedBoxesData(False)

                        #Show the fully unrevealed board for a second
                        drawBoard(mainBoard, revealedBoxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        #Replay the start game animation
                        startGameAnimation(mainBoard)
                    firstSelection = None #reset firstSelection variable

        pygame.display.update()
        FPSClock.tick(FPS)


def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BoardWidth):
        revealedBoxes.append([val] * BoardHeight)
    return revealedBoxes


def getRandomizedBoard():
    #get a list of every possible shape in every possible color
    icons = []
    for color in AllColors:
        for shape in AllShapes:
            icons.append((shape, color))

    random.shuffle(icons) #randomize the order of icons list
    numIconsUsed = int(BoardWidth * BoardHeight / 2) #calculate the num of icons needed
    icons = icons[:numIconsUsed] * 2 #make two of each
    random.shuffle(icons)

    #create the board data structure with randomly placed icons
    board = []
    for x in range(BoardWidth):
        column = []
        for y in range(BoardHeight):
            column.append(icons[0])
            del icons[0]
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    #splits a list into list of lists, where the inner lists have at most groupsize number of items
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i: i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    #convert board coordinates into pixel coordinates
    left = boxx * (BoxSize + GapSize) + Xmargin
    right = boxy * (BoxSize + GapSize) + Ymargin
    return (left, right)


def getBoxAtPixel(x, y):
    for boxx in range(BoardWidth):
        for boxy in range(BoardHeight):
            left, top = leftTopCoordsOfBox(boxx, boxy) #get pixel coords from board coords
            boxRect = pygame.Rect(left, top, BoxSize, BoxSize)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawIcon(shape, color, boxx, boxy):
def drawIcon(shape, color, boxx, boxy):
    quarter = int(BoxSize * 0.25) #syntatic sugar
    half = int(BoxSize * 0.5)  #syntatic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy)#get pixel coords from board coords
    #Draw shapes
    if shape == Donut:
        pygame.draw.circle(DisplaySurf, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DisplaySurf, BgColor, (left + half, top + half), quarter - 5)
    elif shape == Square:
        pygame.draw.rect(DisplaySurf, color, (left + quarter, top + quarter, BoxSize - half, BoxSize - half))
    elif shape == Diamond:
        pygame.draw.polygon(DisplaySurf, color, ((left + half, top), (left + BoxSize - 1, top + half), (left + half, top + BoxSize - 1), (left, top + half)))
    elif shape == Lines:
        for i in range(0, BoxSize, 4):
            pygame.draw.line(DisplaySurf, color, (left, top + i), (left + i, top))
            pygame.draw.line(DisplaySurf, color, (left + i, top + BoxSize - 1), (left + BoxSize - 1, top + i))
    elif shape == Oval:
        pygame.draw.ellipse(DisplaySurf, color, (left, top + quarter, BoxSize, half))


def getShapeColor(board, boxx, boxy):
    #shape value for x, y spot is stored in board[x][y][0]
    #color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # draw boxes being covered/revealed. 'boxes' is a list of two-item lists, which have x and y spot of box
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DisplaySurf, BgColor, (left, top, BoxSize, BoxSize))
        shape, color = getShapeColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: #only draw the cover if there is a coverage
            pygame.draw.rect(DisplaySurf, BoxColor, (left, top, coverage, BoxSize))
    pygame.display.update()
    FPSClock.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    #do the box reveal animation
    for coverage in range(BoxSize, (-RevealSpeed) - 1, -RevealSpeed):
        drawBoxCovers(board, boxesToReveal, coverage)


def coverBoxesAnimation(board, boxesToCover):
    #do the box cover animation
    for coverage in range(0, BoxSize + RevealSpeed, RevealSpeed):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    #draw all boxes in covered/revealed state
    for boxx in range(BoardWidth):
        for boxy in range(BoardHeight):
            left, top = leftTopCoordsOfBox(boxx, boxy) #get pixel coords from board coords
            if not revealed[boxx][boxy]:
                #draw a covered box
                pygame.draw.rect(DisplaySurf, BoxColor, (left, top, BoxSize, BoxSize))
            else:
                #draw revealed icon
                shape, color = getShapeColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)


def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DisplaySurf, HighlightColor, (left - 5, top - 5, BoxSize + 10, BoxSize + 10), 4)


def startGameAnimation(board):
    #Randomly reveal the boxes 8 at a time
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BoardWidth):
        for y in range(BoardHeight):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    #flash the BG color when player won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LightBgColor
    color2 = BgColor

    for i in range(13):
        color1, color2 = color2, color1 #swap colors
        DisplaySurf.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealBoxes):
    #return true if all boxes have been revealead, else false
    for i in revealBoxes:
        if False in i:
            return False
    return True


if __name__ == '__main__':
    main()















