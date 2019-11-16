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
        #tkinter window
        self.wnd = tk.Tk()
        self.wnd.title("Welcome to Pac-Man")
        self.wnd.geometry("900x550")
        self.wnd.configure(bg="black")
        #Display Game Title
        self.gameTPic = tk.PhotoImage(file="Pacman Title.png")
        self.gameTL = tk.Label(self.wnd,image=self.gameTPic,bd=0)
        self.gameTL.pack()
        #Start game button
        self.startB = tk.Button(self.wnd, text="START GAME", command= self.startG)
        self.startB.configure(font=("fixedsys",35),bg="black",fg="yellow2",relief="flat")
        self.startB.configure(activebackground="black",activeforeground="gold4",bd=0)
        self.startB.pack()
        #high scores button
        self.hScoreB = tk.Button(self.wnd, text="HIGH SCORES",command=self.highScoreD)
        self.hScoreB.configure(font=("fixedsys",20),bg="black",fg="cyan2",relief="flat")
        self.hScoreB.configure(activebackground="black",activeforeground="cyan4",bd=0)
        self.hScoreB.pack()
        #how to play button
        self.hTPlayB = tk.Button(self.wnd, text="HOW TO PLAY",command=self.hTPlayD)
        self.hTPlayB.configure(font=("fixedsys",20),bg="black",fg="SpringGreen2",relief="flat")
        self.hTPlayB.configure(activebackground="black",activeforeground="green4",bd=0)
        self.hTPlayB.pack()
        #keeping track of the open windows
        self.hScoreW = []
        self.hTPlayW = []
        #animation
        #fixing position for animation canvas
        self.lb = tk.Label(self.wnd,height=2,bg="black")
        self.lb.pack(side="bottom")
        self.animationC = tk.Canvas(self.wnd,width=900,height=50,bg="black",highlightthickness=0)
        self.animationC.pack(side="bottom")
        self.animationCounter = 0
        #Declare images for animation
        #pacman images
        self.faceingL = [tk.PhotoImage(file='WpmL0.png'), tk.PhotoImage(file='WpmL0.png'),
                    tk.PhotoImage(file='WpmL2.png'), tk.PhotoImage(file='WpmL3.png')]
        self.faceingR = [tk.PhotoImage(file='WpmR0.png'), tk.PhotoImage(file='WpmR1.png'),
                    tk.PhotoImage(file='WpmR2.png'), tk.PhotoImage(file='WpmR3.png')]
        #ghosts images - [right direction, left direction]
        self.blinky = [tk.PhotoImage(file="WblinkyR.png"),tk.PhotoImage(file="WblinkyL.png")]
        self.pinky = [tk.PhotoImage(file="WpinkyR.png"),tk.PhotoImage(file="WpinkyL.png")]
        self.inky = [tk.PhotoImage(file="WinkyR.png"),tk.PhotoImage(file="WinkyL.png")]
        self.clyde = [tk.PhotoImage(file="WclydeR.png"),tk.PhotoImage(file="WclydeL.png")]
        #keeping track of animation direction
        self.goingR = True
        #calling animation function
        self.animationC.after(100, self.animation)
        #Doesnt allow users to rezie the window
        self.wnd.resizable(0,0)
        #Add as the last attribute
        self.wnd.mainloop()

    #The animation on the welcome window
    def animation(self):
        #resit canvas
        self.animationC.delete(tk.ALL)
        #calculating main x location in the canvas
        pos = 10*self.animationCounter
        #if heading towards the right & still in window
        if pos < 1250 and self.goingR == True:
            self.animationC.create_image(pos,30,image=self.faceingR[self.animationCounter%4])
            self.animationC.create_image(1.03*(pos-70),30,image=self.blinky[0])
            self.animationC.create_image((pos-100),30,image=self.pinky[0])
            self.animationC.create_image((pos-170),30,image=self.inky[0])
            self.animationC.create_image(0.9*(pos-220),30,image=self.clyde[0])
            self.animationCounter += 1
        elif self.goingR == True:
            #change motion direction
            self.goingR = False
            self.animationCounter -= 10
        #if heading in the left direction & still in window
        if pos > -250 and self.goingR == False:
            self.animationC.create_image(pos,30,image=self.faceingL[self.animationCounter % 4])
            self.animationC.create_image((pos+230),30,image=self.clyde[1])
            self.animationC.create_image((pos+130),30,image=self.pinky[1])
            self.animationC.create_image(1.1*(pos+40),30,image=self.inky[1])
            self.animationC.create_image(1.3*(pos+25),30,image=self.blinky[1])
            self.animationCounter -= 1
        else:
            #change direction
            self.goingR = True
        #recall function
        self.animationC.after(100, self.animation)

    #Pressing the start button
    def startG(self):
        self.wnd.destroy()
        game()

    #Pressing the high scores button to display hScore wnd
    def highScoreD(self):
        if self.hScoreW == [] or self.hScoreW[0].open == False:
            self.hScoreW = [highScoreWnd()]

    #Pressing the hTPlay button to display
    def hTPlayD(self):
        if self.hTPlayW == [] or self.hTPlayW[0].open == False:
            self.hTPlayW = [hTPlayWnd()]

#highScore window
class highScoreWnd:
    def __init__(self):
        #creating the window
        self.wnd = tk.Toplevel()
        self.wnd.title("Pac-Man High Scores")
        self.wnd.configure(bg="black")
        #call a method if the window was closed
        self.wnd.protocol("WM_DELETE_WINDOW", self.wndClosed)
        self.open = True
        self.wnd.resizable(0,0)

    #if the window was closed
    def wndClosed(self):
        self.open = False
        #close window
        self.wnd.destroy()

#how to play window
class hTPlayWnd:
    def __init__(self):
        #creating the window
        self.wnd = tk.Toplevel()
        self.wnd.title("How To Play Pac-Man")
        self.wnd.configure(bg="black")
        #call a method if the window was closed
        self.wnd.protocol("WM_DELETE_WINDOW", self.wndClosed)
        self.open = True
        self.wnd.resizable(0,0)

    #if the window was closed
    def wndClosed(self):
        self.open = False
        #close window
        self.wnd.destroy()

#user / pacman character class
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
        #location
        self.x = x
        self.y = y
        #dimensions
        self.width = 15
        self.height = 15
        #number of pixels it moves every time
        self.speed = 15
        #determines direction movement (vector)
        self.vel = [-1,0]
        #used for animation
        self.moveCount = 0
        #number of lives
        self.lives = 3

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
                if self.x < 0:
                    self.x = 27*15
                elif self.x > 27*15:
                    self.x = 0
        elif self.vel[1] != 0:
            if self.validM([self.x,(self.y + self.speed*self.vel[1]*(-1))]):
                self.y += self.speed*self.vel[1]*(-1)

    #decides whether the movement is valid or not
    """Returns True if character doesnt collide with any walls
        Returns false if the character does collide with a wall"""
    def validM(self,location):
        #each if in any of the walls
        for w in self.walls:
            if (w.x <= location[0] < (w.x + w.width)) or (w.x < ((location[0] + self.width) < (w.x + w.width))):
                if (w.y <= location[1] < (w.y + w.length)) or (w.y < ((location[1] + self.height) < (w.y + w.length))):
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
        self.speed = 15
        self.vel = [-1, 0]
        #ghost type
        self.color = c
        #ghost design / look
        self.images = self.setImages()
        self.target = (0,0)
        #walls in the game used for ghost AI
        self.walls = w

    #calls AI method based on color / ghost type
    def callAI(self,pacLocation):
        if self.color == "red":
            self.blinkyAI(pacLocation)
        elif self.color == "pink":
            self.blinkyAI(pacLocation)
        elif self.color == "blue":
            self.blinkyAI(pacLocation)
        elif self.color == "orange":
            self.blinkyAI(pacLocation)

    #red ghost (blinky) AI
    #responsible for movement decision
    def blinkyAI(self,pacLocation):
        self.target = pacLocation
        possibleDir = self.possibleDirection()
        self.minDistance(possibleDir)

    def minDistance(self,possibleDir):
        #list to store calculated distances
        distances = []
        #calculating the distance from potenital location to target location
        for i in possibleDir:
            x = self.target[0] - (self.x + self.speed*i[0])
            y = self.target[1] - (self.y + self.speed*i[1]*(-1))
            dist = (((x)**2)+((y)**2))**(0.5)
            distances.append(dist)
        #finding the minimum distance
        minDist = distances[0]
        for i in range(1,len(distances)):
            if distances[i] < minDist:
                minDist = distances[i]
        #getting direction that gets min distance
        bestDir = possibleDir[distances.index(minDist)]
        #setting the best direction as velocity
        self.vel = [bestDir[0],bestDir[1]]

    #determines all the possible directions that the ghost could turn
    def possibleDirection(self):
        #ghosts not allowed to turn 180 degrees
        if self.vel == [1,0]:
            possibleDir = [(1,0),(0,1),(0,-1)]
        elif self.vel == [-1,0]:
            possibleDir = [(-1, 0),(0, 1),(0, -1)]
        elif self.vel == [0,1]:
            possibleDir = [(1,0),(-1,0),(0,1)]
        elif self.vel == [0,-1]:
            possibleDir = [(1,0),(-1,0),(0,-1)]
        temp = list(possibleDir)
        for direction in temp:
            if not self.validM([self.x + self.speed*direction[0],self.y + self.speed*direction[1]*(-1)]):
                possibleDir.remove(direction)
        return possibleDir

    #moves ghost based on individual AI
    def move(self,pacLocation):
        self.callAI(pacLocation)
        if self.vel[0] != 0:
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                self.x += self.speed*self.vel[0]
                if self.x < 0:
                    self.x = 27*15
                elif self.x > 27*15:
                    self.x = 0
        if self.vel[1] != 0:
            if self.validM([self.x,self.y + self.speed*self.vel[1]*(-1)]):
                self.y += self.speed*self.vel[1]*(-1)

    # decides whether the movement is valid or not
    """Returns True if character doesnt collide with any walls
        Returns false if the character does collide with a wall"""
    def validM(self, location):
        # each if in any of the walls
        for w in self.walls:
            if w.x <= location[0] < (w.x + w.width) or w.x < ((location[0] + self.width) < (w.x + w.width)):
                if w.y <= location[1] < (w.y + w.length) or w.y < ((location[1] + self.height) < (w.y + w.length)):
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
        #location
        self.x = x
        self.y = y
        #dimensions
        self.width = width
        self.length = length
        #rectangle in tuple used for displaying walls
        self.hitbox = (self.x,self.y,self.width,self.length)

    #draws wall block into window
    def draw(self,wnd):
        pygame.draw.rect(wnd,(255,0,0),self.hitbox,2)

class food:
    #pictures to display on the window
    foodPics = [pygame.image.load("food10.png"),pygame.image.load("food50.png")]
    def __init__(self,x,y,w):
        #location
        self.x = x
        self.y = y
        #dimensions
        self.width = 15
        self.length = 15
        #how many points its worth
        self.worth = w

    #function that displays the food object on the window
    def draw(self,wnd):
        #food type dot
        if self.worth == 10:
            wnd.blit(self.foodPics[0],(self.x,self.y))
        #food type pellet
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
        #current score
        self.score = 0
        #if game is paused
        self.paused = False
        #start the level
        self.startGame()

    def startGame(self):
        while self.run and (not self.paused):
            #setting frames per second
            self.clock.tick(8)
            #updating window
            self.redrawGameWindow()
            # getting all inputs from user like mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Close window without causing error message
                    self.run = False
            self.getUserInput()
            self.moveChars()
        if self.run == False:
            #quiting pygame
            pygame.quit()

    def getUserInput(self):
        #getting keys pressed
        keys = pygame.key.get_pressed()
        #Turning pacman to face right if valid move
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.pac.validM([self.pac.x + self.pac.speed,self.pac.y]):
                self.pac.vel = [1,0]
        #Turning pacman to face left if valid move
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.pac.validM([self.pac.x - self.pac.speed,self.pac.y]):
                self.pac.vel = [-1,0]
        #Turning pacman to face up if valid move
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.pac.validM([self.pac.x,self.pac.y - self.pac.speed]):
                self.pac.vel = [0,1]
        #Turning pacman to face down if valid move
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.pac.validM([self.pac.x, self.pac.y + self.pac.speed]):
                self.pac.vel = [0,-1]
        #pausing the game
        if keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE] or keys[pygame.K_p]:
            self.pauseG()

    #when the game is paused
    def pauseG(self):
        self.paused = True
        # display pause message
        font = pygame.font.SysFont("comicsans",30)
        pauseTxt = font.render("PAUSED",1,(255,0,0),(0,0,0))
        self.wnd.blit(pauseTxt,(11*15+5,20*15))
        pygame.display.update()
        while self.paused == True:
            #if window closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Close window without causing error message
                    self.paused = False
                    self.run = False
            #keys pressed
            keys = pygame.key.get_pressed()
            #if unpaused
            if keys[pygame.K_c]:
                self.paused = False

    def redrawGameWindow(self):
        #resetting the window to black
        self.wnd.fill((0,0,0))
        # resetting window to background
        self.wnd.blit(self.bg,(0,3*15))
        """
        #drawing wall
        for w in self.walls:
            w.draw(self.wnd)
        """
        #draw food
        for f in self.foods:
            f.draw(self.wnd)
        # drawing pacman
        self.pac.draw(self.wnd)
        #drawing ghosts
        self.blinky.draw(self.wnd)
        self.pinky.draw(self.wnd)
        self.inky.draw(self.wnd)
        self.clyde.draw(self.wnd)

        # updating window to show character
        pygame.display.update()

    def moveChars(self):
        #move all the characters once
        #self.AddScore()
        self.pac.move()
        self.blinky.move((self.pac.x,self.pac.y))
        self.pinky.move((self.pac.x,self.pac.y))
        self.inky.move((self.pac.x,self.pac.y))
        self.clyde.move((self.pac.x,self.pac.y))
        self.AddScore()

    def AddScore(self):
        #each if pacman character collides with any of foods
        for f in self.foods:
            if f.x <= self.pac.x < (f.x + f.width) or f.x < ((self.pac.x + self.pac.width) < (f.x + f.width)):
                if f.y <= self.pac.y < (f.y + f.length) or f.y < ((self.pac.y + self.pac.height) < (f.y + f.length)):
                    #add the food worth to score
                    self.score += f.worth
                    #remove food from foods list
                    self.foods.pop(self.foods.index(f))

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