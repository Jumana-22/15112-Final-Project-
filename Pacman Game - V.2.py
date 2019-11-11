import tkinter as tk
import pygame
pygame.init()

#welcome window
"""Options
- Start Game 
- High Scores
- How to play
- Exit"""
class welcomeWnd:
    def __init__(self):
        self.wnd = tk.Tk()
        self.wnd.title("Welcome to PacMan")
        self.startB = tk.Button(self.wnd, text="Start Game", command= self.startG)
        self.startB.pack()
        #Doesnt allow users to rezie the window
        #Must be added after adding everything in window
        self.wnd.resizable(0,0)
        #Add as the last attribute
        self.wnd.mainloop()

    #Pressing the start button
    def startG(self):
        self.wnd.destroy()
        thisGame = game()


class pacman:
    #Declare images for pacman animation
    faceingL = [pygame.image.load('pmL0.png'),pygame.image.load('pmL1.png'),
                pygame.image.load('pmL2.png'),pygame.image.load('pmL3.png')]
    faceingR = [pygame.image.load('pmR0.png'),pygame.image.load('pmR1.png'),
                pygame.image.load('pmR2.png'),pygame.image.load('pmR3.png')]
    faceingU = [pygame.image.load('pmU0.png'),pygame.image.load('pmU1.png'),
                pygame.image.load('pmU2.png'),pygame.image.load('pmU3.png')]
    faceingD = [pygame.image.load('pmD0.png'),pygame.image.load('pmD1.png'),
                pygame.image.load('pmD2.png'),pygame.image.load('pmD3.png')]
    def __init__(self,x,y,w):
        #Basic attributes
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.speed = 5
        #determines direction movement (vector)
        self.vel = [-1,0]
        #used for animation
        self.moveCount = 0

        #walls that restrict movement
        self.walls = w

    #loads pacman into window
    def draw(self,wnd):
        #if out of animation frames
        if self.moveCount > 3:
            self.moveCount = 0
        #facing right
        if self.vel[0] == 1:
            wnd.blit(self.faceingR[self.moveCount],(self.x,self.y))
        #facing left
        elif self.vel[0] == -1:
            wnd.blit(self.faceingL[self.moveCount], (self.x, self.y))
        #facing up
        elif self.vel[1] == 1:
            wnd.blit(self.faceingU[self.moveCount], (self.x, self.y))
        #facing down
        elif self.vel[1] == -1:
            wnd.blit(self.faceingD[self.moveCount], (self.x, self.y))
        #increment move counter
        self.moveCount += 1

    #called to move pacman
    def move(self):
        if self.vel[0] != 0:
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                self.x += self.speed*self.vel[0]
        if self.vel[1] != 0:
            if self.validM([self.x,self.y + self.speed*self.vel[1]]):
                self.x += self.speed*self.vel[1]

    #decides whether the movement is valid or not
    """Returns True if character doesnt collide with any walls
        Returns false if the character does collide with a wall"""
    def validM(self,location):
        #each if in any of the walls
        for w in self.walls:
            if w.x < location[0] < (w.x + w.width) or w.x < ((location[0] + self.width) < (w.x + w.width)):
                if w.y < location[1] < (w.y + w.length) or w.y < ((location[1] + self.height) < (w.y + w.length)):
                    return False
        #Return True otherwise
        return True

class ghost:
    blinkyPics = [pygame.image.load("blinkyL.png"),pygame.image.load("blinkyR.png"),
                  pygame.image.load("blinkyU.png"),pygame.image.load("blinkyD.png")]
    pinkyPics = [pygame.image.load("pinkyL.png"),pygame.image.load("pinkyR.png"),
                 pygame.image.load("pinkyU.png"),pygame.image.load("pinkyD.png")]
    inkyPics = [pygame.image.load("inkyL.png"),pygame.image.load("inkyR.png"),
                pygame.image.load("inkyU.png"),pygame.image.load("inkyD.png")]
    clydePics = [pygame.image.load("clydeL.png"),pygame.image.load("clydeR.png"),
                 pygame.image.load("clydeU.png"),pygame.image.load("clydeD.png")]
    def __init__(self,x,y,c,w):
        #ghost location
        self.x = x
        self.y = y
        #ghost dimentsions
        self.width = 15
        self.height = 15
        #ghost motion variables
        self.speed = 5
        self.vel = [-1, 0]
        #ghost type
        self.color = c
        #ghost design / look
        self.images = self.setImages()
        self.target = self.calTarget()
        #walls in the game used for ghost AI
        self.walls = w

    #calculate traget position based on color / ghost type 
    def calTarget(self):
        #change the velocity of the ghost
        pass

    #moves ghost in the direction of dir
    def move(self):
        self.calTarget()
        if self.vel[0] != 0:
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                self.x += self.speed*self.vel[0]
        if self.vel[1] != 0:
            if self.validM([self.x,self.y + self.speed*self.vel[1]]):
                self.x += self.speed*self.vel[1]

    # decides whether the movement is valid or not
    """Returns True if character doesnt collide with any walls
        Returns false if the character does collide with a wall"""
    def validM(self, location):
        # each if in any of the walls
        for w in self.walls:
            if w.x < location[0] < (w.x + w.width) or w.x < ((location[0] + self.width) < (w.x + w.width)):
                if w.y < location[1] < (w.y + w.length) or w.y < ((location[1] + self.height) < (w.y + w.length)):
                    return False
        # Return True otherwise
        return True
    
    #loads ghost into window
    def draw(self,wnd):
        if self.vel[0] == 1:
            wnd.blit(self.images[1],(self.x,self.y))
        elif self.vel[0] == -1:
            wnd.blit(self.images[0],(self.x,self.y))
        elif self.vel[1] == 1:
            wnd.blit(self.images[2],(self.x,self.y))
        else:
            wnd.blit(self.images[3],(self.x,self.y))

    #Setting the right list of images for that type of ghost
    def setImages(self):
        if self.color == "red":
            return self.blinkyPics
        elif self.color == "pink":
            return self.pinkyPics
        elif self.color == "blue":
            return self.inkyPics
        elif self.color == "orange":
            return self.clydePics

class wall: 
    def __init__(self,x,y,width,length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.hitbox = (self.x,self.y,self.width,self.length)

    #draws wall block into window
    def draw(self,wnd):
        pygame.draw.rect(wnd,(255,0,0),self.hitbox,2)

class food:
    foodPics = [pygame.image.load("food10.png"),pygame.image.load("food50.png")]
    def __init__(self,x,y,w):
        self.x = x
        self.y = y
        self.width = 15
        self.length = 15
        self.worth = w

    def draw(self,wnd):
        if self.worth == 10:
            wnd.blit(self.foodPics[0],(self.x,self.y))
        elif self.worth == 50:
            wnd.blit(self.foodPics[1],(self.x,self.y))

class game:
    def __init__(self):
        #Creating game window
        self.wnd = pygame.display.set_mode((28*15,(31+5)*15))
        #Setting window name 
        pygame.display.set_caption("PACMAN")
        #level background
        self.bg = pygame.image.load("background.png")
        # resetting window to all black
        self.wnd.blit(self.bg, (0, 3 * 15))

        #game clock
        self.clock = pygame.time.Clock()

        #game objects
        #walls
        self.walls = []
        self.createWalls()
        #food/points
        self.foods = []
        self.createFoods()
        #pacman character
        self.pac = pacman(195,(17+3)*15,self.walls)
        #The 4 ghosts
        self.blinky = ghost(195,(11+3)*15,"red",self.walls)
        self.pinky = ghost(195,(11+3)*15,"pink",self.walls)
        self.inky = ghost(195,(11+3)*15,"blue",self.walls)
        self.clyde = ghost(195,(11+3)*15,"orange",self.walls)

        #While the level is running
        self.run = True

        #start the level
        self.startGame()

    def startGame(self):
        while self.run:
            #setting frames per second
            self.clock.tick(15)
            #updating window
            self.redrawGameWindow()
            # getting all inputs from user like mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Close window without causing error message
                    self.run = False
            self.moveChars()
        #quiting pygame
        pygame.quit()

    def redrawGameWindow(self):
        # resetting window to background
        self.wnd.blit(self.bg, (0, 3 * 15))
        """
        #drawing wall
        for w in self.walls:
            w.draw(self.wnd)"""
        #draw food
        for f in self.foods:
            f.draw(self.wnd)
        #drawing ghosts
        self.blinky.draw(self.wnd)
        self.pinky.draw(self.wnd)
        self.inky.draw(self.wnd)
        self.clyde.draw(self.wnd)
        #drawing pacman
        self.pac.draw(self.wnd)

        # updating window to show character
        pygame.display.update()

    def moveChars(self):
        #move all the characters once
        self.pac.move()
        self.blinky.move()
        self.pinky.move()
        self.inky.move()
        self.clyde.move()

    def createWalls(self):
        #borders / outer walls 
        self.walls.append(wall((0*15),((0+3)*15),(28*15),(1*15)))
        self.walls.append(wall((0*15),((1+3)*15),(1*15),(9*15)))
        self.walls.append(wall((1*15),((9+3)*15),(5*15),(1*15)))
        self.walls.append(wall((5*15),((10+3)*15),(1*15),(3*15)))
        self.walls.append(wall((0*15),((13+3)*15),(6*15),(1*15)))
        self.walls.append(wall((0*15),((15+3)*15),(6*15),(1*15)))
        self.walls.append(wall((0*15),((19+3)*15),(6*15),(1*15)))
        self.walls.append(wall((5*15),((16+3)*15),(1*15),(3*15)))
        self.walls.append(wall((0*15),((20+3)*15),(1*15),(10*15)))
        self.walls.append(wall((1*15),((24+3)*15),(2*15),(2*15)))
        self.walls.append(wall((0*15),((30+3)*15),(28*15),(1*15)))
        self.walls.append(wall((27*15),((1+3)*15),(1*15),(9*15)))
        self.walls.append(wall((22*15),((9+3)*15),(5*15),(1*15)))
        self.walls.append(wall((22*15),((10+3)*15),(1*15),(3*15)))
        self.walls.append(wall((22*15),((13+3)*15),(6*15),(1*15)))
        self.walls.append(wall((22*15),((15+3)*15),(6*15),(1*15)))
        self.walls.append(wall((22*15),((19+3)*15),(6*15),(1*15)))
        self.walls.append(wall((22*15),((16+3)*15),(1*15),(3*15)))
        self.walls.append(wall((27*15),((20+3)*15),(1*15),(10*15)))
        self.walls.append(wall((25*15),((24+3)*15),(2*15),(2*15)))
        #upper inner walls
        self.walls.append(wall((2*15),((2+3)*15),(4*15),(3*15)))
        self.walls.append(wall((22*15),((2+3)*15),(4*15),(3*15)))
        self.walls.append(wall((7*15),((2+3)*15),(5*15),(3*15)))
        self.walls.append(wall((16*15),((2+3)*15),(5*15),(3*15)))
        self.walls.append(wall((13*15),((1+3)*15),(2*15),(4*15)))
        self.walls.append(wall((2*15),((6+3)*15),(4*15),(2*15)))
        self.walls.append(wall((22*15),((6+3)*15),(4*15),(2*15)))
        self.walls.append(wall((7*15),((6+3)*15),(2*15),(8*15)))
        self.walls.append(wall((19*15),((6+3)*15),(2*15),(8*15)))
        self.walls.append(wall((13*15),((8+3)*15),(2*15),(3*15)))
        self.walls.append(wall((9*15),((9+3)*15),(3*15),(2*15)))
        self.walls.append(wall((16*15),((9+3)*15),(3*15),(2*15)))
        self.walls.append(wall((10*15),((6+3)*15),(8*15),(2*15)))
        #vertical under inner walls
        self.walls.append(wall((7*15),((15+3)*15),(2*15),(5*15)))
        self.walls.append(wall((19*15),((15+3)*15),(2*15),(5*15)))
        self.walls.append(wall((13*15),((20+3)*15),(2*15),(3*15)))
        self.walls.append(wall((4*15),((21+3)*15),(2*15),(5*15)))
        self.walls.append(wall((22*15),((21+3)*15),(2*15),(5*15)))
        self.walls.append(wall((7*15),((24+3)*15),(2*15),(3*15)))
        self.walls.append(wall((19*15),((24+3)*15),(2*15),(3*15)))
        self.walls.append(wall((13*15),((26+3)*15),(2*15),(3*15)))
        #horizontal under inner walls
        self.walls.append(wall((10*15),((18+3)*15),(8*15),(2*15)))
        self.walls.append(wall((2*15),((21+3)*15),(2*15),(2*15)))
        self.walls.append(wall((24*15),((21+3)*15),(2*15),(2*15)))
        self.walls.append(wall((7*15),((21+3)*15),(5*15),(2*15)))
        self.walls.append(wall((16*15),((21+3)*15),(5*15),(2*15)))
        self.walls.append(wall((10*15),((24+3)*15),(8*15),(2*15)))
        self.walls.append(wall((2*15),((27+3)*15),(10*15),(2*15)))
        self.walls.append(wall((16*15),((27+3)*15),(10*15),(2*15)))
        #ghost house
        self.walls.append(wall((10*15),((12+3)*15),(8*15),(1*15)))
        self.walls.append(wall((10*15),((16+3)*15),(8*15),(1*15)))
        self.walls.append(wall((10*15),((13+3)*15),(1*15),(3*15)))
        self.walls.append(wall((17*15),((13+3)*15),(1*15),(3*15)))

    def createFoods(self):
        #food in a horizonal line
        for i in range(1,13):
            self.foods.append(food((i*15),((1+3)*15),10))
        for i in range(15,27):
            self.foods.append(food((i*15),((1+3)*15),10))
        for i in range(1,27):
            self.foods.append(food((i*15),((5+3)*15),10))
        for i in range(1,7):
            self.foods.append(food((i*15),((8+3)*15),10))
        for i in range(9,13):
            self.foods.append(food((i*15),((8+3)*15),10))
        for i in range(15,19):
            self.foods.append(food((i*15),((8+3)*15),10))
        for i in range(21,27):
            self.foods.append(food((i*15),((8+3)*15),10))
        for i in range(9,19):
            self.foods.append(food((i*15),((11+3)*15),10))
        for i in range(0,10):
            self.foods.append(food((i*15),((14+3)*15),10))
        for i in range(18,28):
            self.foods.append(food((i*15),((14+3)*15),10))
        for i in range(9,19):
            self.foods.append(food((i*15),((17+3)*15),10))
        for i in range(1,13):
            self.foods.append(food((i*15),((20+3)*15),10))
        for i in range(15,27):
            self.foods.append(food((i*15),((20+3)*15),10))
        for i in range(2,4):
            self.foods.append(food((i*15),((23+3)*15),10))
        for i in range(6,22):
            self.foods.append(food((i*15),((23+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((i*15),((23+3)*15),10))
        for i in range(1,7):
            self.foods.append(food((i*15),((26+3)*15),10))
        for i in range(9,13):
            self.foods.append(food((i*15),((26+3)*15),10))
        for i in range(15,19):
            self.foods.append(food((i*15),((26+3)*15),10))
        for i in range(21,27):
            self.foods.append(food((i*15),((26+3)*15),10))
        for i in range(1,27):
            self.foods.append(food((i*15),((29+3)*15),10))
        #food in a vertical line
        for i in range(2,3):
            self.foods.append(food((1*15),((i+3)*15),10))
        for i in range(4,5):
            self.foods.append(food((1*15),((i+3)*15),10))
        for i in range(2,5):
            self.foods.append(food((6*15),((i+3)*15),10))
        for i in range(2,5):
            self.foods.append(food((12*15),((i+3)*15),10))
        for i in range(2,5):
            self.foods.append(food((15*15),((i+3)*15),10))
        for i in range(2,5):
            self.foods.append(food((21*15),((i+3)*15),10))
        for i in range(2,3):
            self.foods.append(food((26*15),((i+3)*15),10))
        for i in range(4,5):
            self.foods.append(food((26*15),((i+3)*15),10))
        for i in range(6,8):
            self.foods.append(food((1*15),((i+3)*15),10))
        for i in range(6,8):
            self.foods.append(food((6*15),((i+3)*15),10))
        for i in range(6,8):
            self.foods.append(food((9*15),((i+3)*15),10))
        for i in range(6,8):
            self.foods.append(food((18*15),((i+3)*15),10))
        for i in range(6,8):
            self.foods.append(food((21*15),((i+3)*15),10))
        for i in range(6,8):
            self.foods.append(food((26*15),((i+3)*15),10))
        for i in range(9,14):
            self.foods.append(food((6*15),((i+3)*15),10))
        for i in range(9,14):
            self.foods.append(food((21*15),((i+3)*15),10))
        for i in range(9,11):
            self.foods.append(food((12*15),((i+3)*15),10))
        for i in range(9,11):
            self.foods.append(food((15*15),((i+3)*15),10))
        for i in range(12,14):
            self.foods.append(food((9*15),((i+3)*15),10))
        for i in range(12,14):
            self.foods.append(food((18*15),((i+3)*15),10))
        for i in range(15,20):
            self.foods.append(food((6*15),((i+3)*15),10))
        for i in range(15,20):
            self.foods.append(food((21*15),((i+3)*15),10))
        for i in range(15,17):
            self.foods.append(food((9*15),((i+3)*15),10))
        for i in range(15,17):
            self.foods.append(food((18*15),((i+3)*15),10))
        for i in range(18,20):
            self.foods.append(food((9*15),((i+3)*15),10))
        for i in range(18,20):
            self.foods.append(food((18*15),((i+3)*15),10))
        for i in range(21,23):
            self.foods.append(food((1*15),((i+3)*15),10))
        for i in range(21,23):
            self.foods.append(food((6*15),((i+3)*15),10))
        for i in range(21,23):
            self.foods.append(food((12*15),((i+3)*15),10))
        for i in range(21,23):
            self.foods.append(food((15*15),((i+3)*15),10))
        for i in range(21,23):
            self.foods.append(food((21*15),((i+3)*15),10))
        for i in range(21,23):
            self.foods.append(food((26*15),((i+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((3*15),((i+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((6*15),((i+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((9*15),((i+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((18*15),((i+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((21*15),((i+3)*15),10))
        for i in range(24,26):
            self.foods.append(food((24*15),((i+3)*15),10))
        for i in range(27,29):
            self.foods.append(food((1*15),((i+3)*15),10))
        for i in range(27,29):
            self.foods.append(food((12*15),((i+3)*15),10))
        for i in range(27,29):
            self.foods.append(food((15*15),((i+3)*15),10))
        for i in range(27,29):
            self.foods.append(food((26*15),((i+3)*15),10))
        #50 point foods
        self.foods.append(food((1*15),((3+3)*15),50))
        self.foods.append(food((26*15),((3+3)*15),50))
        self.foods.append(food((1*15),((23+3)*15),50))
        self.foods.append(food((26*15),((23+3)*15),50))

#Starting the application
App = welcomeWnd()