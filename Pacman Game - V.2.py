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
        #background music
        self.music = pygame.mixer.music.load("welcomeM.wav")
        pygame.mixer.music.play(-1)
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
        #fadeout background music
        pygame.mixer.music.fadeout(1000)
        #destory windows
        self.wnd.destroy()
        #start an instance of the game
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
        #keeping track if the wnd is open or not
        self.open = True
        #wnd heading
        self.heading = tk.Label(self.wnd,text="HIGH SCORES",font=("fixedsys", 40))
        self.heading.configure(bg="black",fg="white",pady=30,padx=200)
        self.heading.pack()
        #frame for table placment
        self.frame = tk.Frame(self.wnd,bg="black")
        self.frame.pack()
        #list for each column
        self.iconC = []
        self.scores = []
        self.names = []
        #calling function which creates widgets for scores table
        self.scoreTb()
        #adding space at the botton of window
        self.design = tk.Label(self.frame,bg="black",pady=10)
        self.design.grid(column=0,row=5)
        #Doesnt allow users to rezie the window
        self.wnd.resizable(0,0)

    #Displaying top 5 scores
    def scoreTb(self):
        #icons
        self.iconsPics = [tk.PhotoImage(file='WpmR1.png'), tk.PhotoImage(file="WblinkyR.png"),
                          tk.PhotoImage(file="WpinkyR.png"), tk.PhotoImage(file="WinkyR.png"),
                          tk.PhotoImage(file="WclydeR.png")]
        #creating 5 rows for each column
        for i in range(5):
            #Creating canvas widgets to put icons in
            self.iconC.append(tk.Canvas(self.frame,width=50,height=50,bg="black",highlightthickness=0))
            #adding image to canvas
            self.iconC[i].create_image(25,25,image=self.iconsPics[i])
            self.iconC[i].grid(column=0,row=i)
            #Adding labels to display scores
            self.scores.append(tk.Label(self.frame,font=("fixedsys",15),
                                        text=str(i+1)+" - ##### ",bg="black",fg="white"))
            self.scores[i].grid(column=1,row=i)
            #adding labels to display player name
            self.names.append(tk.Label(self.frame,font=("fixedsys",15),
                                        text="---------",bg="black",fg="white"))
            self.names[i].grid(column=2,row=i)

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
        #keeping track if the wnd is open or not
        self.open = True
        #wnd heading DeepSkyBlue3 DarkOrange2 oliveDrab2
        self.heading = tk.Label(self.wnd,text="HOW TO PLAY",font=("fixedsys",40))
        self.heading.configure(bg="black",fg="cyan",pady=30,padx=200)
        self.heading.pack()
        #How to play instructions
        self.instr = tk.Text(self.wnd,width=41,height=8,font=("fixedsys",30))
        self.instr.configure(bg='black',fg="cyan4",bd=0)
        #string of instructions to be displayed
        self.instrMsg = "\n Move Pac-Man using Arrow or 'WASD' keys " + \
                        "\n\n\tPause game using 'ESC' key" + \
                        "\n\n\tUnpause game using 'c' key"
        self.instr.insert(tk.END,self.instrMsg)
        #to not allow user to modify textbox
        self.instr.configure(state="disabled")
        self.instr.pack()
        #Doesnt allow users to rezie the window
        self.wnd.resizable(0,0)

    #if the window was closed
    def wndClosed(self):
        self.open = False
        #close window
        self.wnd.destroy()

#End of the game window
class endWnd:
    def __init__(self,score,end):
        #creating a tkinter window
        self.wnd = tk.Tk()
        self.wnd.title("Game End")
        self.wnd.geometry("700x400")
        self.wnd.configure(bg="black")
        #saving the score the user got
        self.score = score
        #saving how the game was ended (lose or win)
        self.end = end
        #creating heading
        self.hOptions = ["TRY AGAIN","CONGRATULATIONS"]
        self.heading = tk.Label(self.wnd,bg="black",fg="yellow",pady=20)
        self.heading.configure(text=self.hOptions[self.end],font=("fixedsys",50))
        self.heading.pack()
        #displaying the score
        self.scoreL = tk.Label(self.wnd,bg="black",fg="white",font=("fixedsys",20),pady=20)
        self.scoreL.configure(text="SCORE  " + "0"*(4-len(str(self.score))) + str(self.score))
        self.scoreL.pack()
        #player name
        self.nameF = tk.Frame(self.wnd,bg="black")
        self.nameF.pack()
        self.nameL = tk.Label(self.nameF,text="NAME:",padx=15,bg="black",fg="white",font=("fixedsys",10))
        self.nameL.grid(column=0,row=0)
        #entery box for user to insert name
        self.nameE = tk.Entry(self.nameF)
        self.nameE.grid(column=1,row=0)
        #button to save score and player name
        self.saved = False
        self.nameB = tk.Button(self.nameF,text="SUBMIT SCORE",padx=20,bg="black",fg="red",relief="flat",bd=0)
        self.nameB.configure(font=("fixedsys",10),activebackground="black",activeforeground="red4",command=self.submit)
        self.nameB.grid(column=3,row=0)
        #for desgin placement
        self.design = tk.Label(self.wnd,bg="black",height=4)
        self.design.pack()
        #frame to bottom buttons
        self.buttonF = tk.Frame(self.wnd,bg="black")
        self.buttonF.pack()
        #button to play again
        self.playB = tk.Button(self.buttonF,text="PLAY AGAIN",font=("fixedsys",20),bd=0,padx=10,command=self.playA)
        self.playB.configure(bg="black",fg="yellow2",activebackground="black",activeforeground="gold4",relief="flat")
        self.playB.grid(column=0,row=0)
        #button to go back to welcome window
        self.menuB = tk.Button(self.buttonF,text="MAIN MENU",font=("fixedsys",20),bd=0,padx=10,command=self.mainMenu)
        self.menuB.configure(bg="black",fg="cyan2",activebackground="black",activeforeground="cyan4",relief="flat")
        self.menuB.grid(column=1,row=0)
        #button to quit application
        self.quitB = tk.Button(self.buttonF,text="QUIT",font=("fixedsys",20),bd=0,padx=10,command=self.quit)
        self.quitB.configure(bg="black",fg="red",activebackground="black",activeforeground="red4",relief="flat")
        self.quitB.grid(column=2,row=0)
        #Doesnt allow user to resize the window
        self.wnd.resizable(0,0)
        self.wnd.mainloop()

    #function to submit score and player name
    def submit(self):
        if self.saved == False:
            self.saved = True
            #get name from user input
            name = self.nameE.get()
            #call function that will read stored data and sort it with new data
            self.read_order(name)

    #reads socres from file & order from from highest to lowest
    def read_order(self,name):
        #list to store player names
        namesL = [name]
        #list to store scores
        scoresL = [self.score]
        #read saved scores and player names & and them to the lists
        with open("Scores.txt", "r") as f:
            info = f.readline()
            while info:
                #split string into the seperate data
                infoS = info.split("@@")[1:]
                scoresL.append(int(infoS[0]))
                namesL.append(infoS[1].replace("\n", ""))
                info = f.readline()
        #lists to store sorted data
        newNameL = []
        newScoreL = []
        #integer used for loop
        num = len(scoresL)
        for i in range(num):
            #add the data for the player with the highest score into sorted lists
            newScoreL.append(max(scoresL))
            newNameL.append(namesL[scoresL.index(max(scoresL))])
            #remove data of the player with the highest score from list of unsorted data
            namesL.pop(scoresL.index(max(scoresL)))
            scoresL.pop(scoresL.index(max(scoresL)))
        self.saveData(newNameL,newScoreL)

    #function to save data into score file
    def saveData(self,nameL,scoreL):
        #lists to store all the data to save
        newInfo = []
        #join each player data together into 1 element in newInfo list
        for i in range(len(scoreL)):
            playerInfo = "@@" + str(scoreL[i]) + "@@" + nameL[i] + "\n"
            newInfo.append(playerInfo)
        #save the sorted infomation into file
        with open("Scores.txt", "w") as f:
            f.writelines(newInfo)

    #function for the play again bottom
    def playA(self):
        #close current window
        self.wnd.destroy()
        #create an instance of the game
        game()

    #function for the main menu button
    def mainMenu(self):
        #close current window
        self.wnd.destroy()
        #create an instance of the welcome wnd
        welcomeWnd()

    #function for quit button
    def quit(self):
        #close current window
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
        self.lives = 4

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
        #if moving right or left
        if self.vel[0] != 0:
            #make sure the move is valid
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                #move to new location
                self.x += self.speed*self.vel[0]
                #if going though the tunnel from the left side
                if self.x < 0:
                    self.x = 27*15
                #if going though the tunnel from the right side
                elif self.x > 27*15:
                    self.x = 0
        #if moving up or down
        elif self.vel[1] != 0:
            #make sure the move is valid
            if self.validM([self.x,(self.y + self.speed*self.vel[1]*(-1))]):
                #move to new location
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
    def callAI(self,pacLocation,pacDir,blinkyLoc):
        if self.color == "red":
            self.blinkyAI(pacLocation)
        elif self.color == "pink":
            self.pinkyAI(pacLocation,pacDir)
        elif self.color == "blue":
            self.inkyAI(pacLocation,pacDir,blinkyLoc)
        elif self.color == "orange":
            self.clydeAI(pacLocation)

    #red ghost (blinky) AI
    #responsible for movement decision
    def blinkyAI(self,pacLocation):
        #set target coordinates
        self.target = pacLocation
        #get possible travel direction from current location
        possibleDir = self.possibleDirection()
        #travel in direction with shortest distance from target coordinates
        self.minDistance(possibleDir)

    #pink ghost (pinky) AI
    #responsible for movement decision
    def pinkyAI(self,pacLocation,pacDir):
        #setting target location on pacman location and facing direction
        if pacDir == [1,0]:
            self.target = (pacLocation[0]+(15*4),pacLocation[1])
        elif pacDir == [-1,0]:
            self.target = (pacLocation[0]-(15*4),pacLocation[1])
        elif pacDir == [0,1]:
            self.target = (pacLocation[0]-(15*4),pacLocation[1]-(15*4))
        elif pacDir == [0,-1]:
            self.target = (pacLocation[0],pacLocation[1]+(15*4))
        #get possible travel direction from current location
        possibleDir = self.possibleDirection()
        #travel in direction with shortest distance from target coordinates
        self.minDistance(possibleDir)

    #blue ghost (inky) AI
    #responsible for movement decision
    def inkyAI(self,pacLocation,pacDir,blinkyLoc):
        #setting target location on pacman location and facing direction
        if pacDir == [1,0]:
            self.target = (pacLocation[0]+(15*2),pacLocation[1])
        elif pacDir == [-1,0]:
            self.target = (pacLocation[0]-(15*2),pacLocation[1])
        elif pacDir == [0,1]:
            self.target = (pacLocation[0]-(15*2),pacLocation[1] -(15*2))
        elif pacDir == [0,-1]:
            self.target = (pacLocation[0],pacLocation[1]+(15*2))
        self.target = (self.target[0]-(blinkyLoc[0]-self.target[0]),
                       self.target[1]-(blinkyLoc[1]-self.target[1]))
        #get possible travel direction from current location
        possibleDir = self.possibleDirection()
        #travel in direction with shortest distance from target coordinates
        self.minDistance(possibleDir)

    #orange ghost (clyde) AI
    #responsible for movement decision
    def clydeAI(self, pacLocation):
        #calculating distance between pac-man and orange ghost
        distance = (((pacLocation[0]-self.x)**2)+((pacLocation[1]-self.y)**2))*(1/2)
        #target coordinated dependent if ghost is more than 8 tiles away from pac-man
        if distance <= (8*15):
            #set target to bottom left corner
            self.target = (0,31*15)
        else:
            #set target coordinates to pac-man location
            self.target = pacLocation
        # get possible travel direction from current location
        possibleDir = self.possibleDirection()
        # travel in direction with shortest distance from target coordinates
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
        #temparay copy of all possible direction to be used in for loop
        temp = list(possibleDir)
        #for each possible direction check if it is a valid move(doesnt collid with wall)
        for direction in temp:
            if not self.validM([self.x + self.speed*direction[0],self.y + self.speed*direction[1]*(-1)]):
                #remove direction from possible directions list if collided with wall
                possibleDir.remove(direction)
        return possibleDir

    #moves ghost based on individual AI
    def move(self,pacLocation,pacDir,blinkyLoc=(0,0)):
        #function that calls correct AI & decides on the direction of ghost movement
        self.callAI(pacLocation,pacDir,blinkyLoc)
        #if moving right or left
        if self.vel[0] != 0:
            # make sure the move is valid
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                # move the ghost
                self.x += self.speed*self.vel[0]
                #if the ghost goes though the tunnel from the left side
                if self.x < 0:
                    self.x = 27*15
                #if the ghost goes though the tunnel from the right side
                elif self.x > 27*15:
                    self.x = 0
        #if moving up or down
        if self.vel[1] != 0:
            #make sure the move is valid
            if self.validM([self.x,self.y + self.speed*self.vel[1]*(-1)]):
                #move the ghost
                self.y += self.speed*self.vel[1]*(-1)

    #decides whether the movement is valid or not
    """Returns True if character doesnt collide with any walls
        Returns false if the character does collide with a wall"""
    def validM(self, location):
        # each if in any of the walls
        for w in self.walls:
            if w.x <= location[0] < (w.x + w.width) or w.x < ((location[0] + self.width) < (w.x + w.width)):
                if w.y <= location[1] < (w.y + w.length) or w.y < ((location[1] + self.height) < (w.y + w.length)):
                    return False
        #Return True otherwise
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

        #sound effects
        self.eatingS = pygame.mixer.Sound("munch_1.wav")
        self.deathPS = pygame.mixer.Sound("death_1.wav")

        #While the level is running
        self.run = True
        #if the game has ended
        self.end = False
        #current score
        self.score = 0
        #track if game is paused
        self.paused = False
        #start the level
        self.startGame()

    def startGame(self):
        #call game countdown function
        self.countDown()
        #background music
        self.music = pygame.mixer.music.load("siren_2.wav")
        pygame.mixer.music.play(-1)
        while self.run and (not self.paused):
            #setting frames per second
            self.clock.tick(8)
            #updating window
            self.redrawGameWindow()
            #cheching if ghosts and pac-man collided
            self.charCollision()
            # getting all inputs from user like mouse movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Close window without causing error message
                    self.run = False
            self.getUserInput()
            #move all the characters
            self.moveChars()
            #if the game has ended
            if (self.pac.lives <= 0) or (self.foods == []):
                pygame.mixer.music.stop()
                self.run = False
                self.end = True
                self.endC()
        if self.run == False and self.end == False:
            #quiting pygame
            pygame.quit()

    def countDown(self):
        self.redrawGameWindow()
        #display ready message
        font = pygame.font.SysFont("comicsans",30)
        font.set_italic(True)
        readyTxt = font.render("READY!",-1,(255,0,0),(0,0,0))
        self.wnd.blit(readyTxt,(11*15+5,20*15))
        #update window
        pygame.display.update()
        #count down to start game
        pygame.time.delay(2000)
        self.pac.lives = 3

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
        if keys[pygame.K_ESCAPE]:
            self.pauseG()

    #when the game is paused
    def pauseG(self):
        self.paused = True
        #display pause message
        font = pygame.font.SysFont("comicsans",30)
        pauseTxt = font.render("PAUSED",1,(255,0,0),(0,0,0))
        self.wnd.blit(pauseTxt,(11*15+5,20*15))
        pygame.display.update()
        #pause music
        pygame.mixer.music.pause()
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
                #unpause music
                pygame.mixer.music.unpause()

    def redrawGameWindow(self):
        #resetting the window to black
        self.wnd.fill((0,0,0))
        # resetting window to background
        self.wnd.blit(self.bg,(0,3*15))
        #display current score
        self.drawScore()
        """
        #drawing wall
        for w in self.walls:
            w.draw(self.wnd)
        """
        #draw food
        for f in self.foods:
            f.draw(self.wnd)
        #drawing pacman
        self.pac.draw(self.wnd)
        #drawing ghosts
        self.blinky.draw(self.wnd)
        self.pinky.draw(self.wnd)
        self.inky.draw(self.wnd)
        self.clyde.draw(self.wnd)
        #draw lives
        self.drawLives()
        # updating window to show character
        pygame.display.update()

    #function that displays icons to show number of lives left
    def drawLives(self):
        #loading image
        livesPic = pygame.image.load('pmR1.png')
        #display 1 less than the amount of lives left
        for i in range(self.pac.lives-1):
            self.wnd.blit(livesPic,(i*20+5,34*15))

    def drawScore(self):
        #display score heading
        font = pygame.font.SysFont("comicsans",30)
        scoreTxt = font.render("SCORE",2,(250,250, 250),(0,0,0))
        self.wnd.blit(scoreTxt,(11*15+10,5))
        #current score
        scoreStr = "0"*(4-len(str(self.score)))+str(self.score)
        scoreN = font.render(scoreStr,1,(250,250,250),(0,0,0))
        self.wnd.blit(scoreN,(12*15+10,25))

    #calls all the funcions to move all the charcater in the game
    #also calls function for pac-man colliding with food objects (dots & pellets)
    def moveChars(self):
        #move all the characters once
        self.pac.move()
        self.blinky.move((self.pac.x,self.pac.y),self.pac.vel)
        self.pinky.move((self.pac.x,self.pac.y),self.pac.vel)
        self.inky.move((self.pac.x,self.pac.y),self.pac.vel,(self.blinky.x,self.blinky.y))
        self.clyde.move((self.pac.x,self.pac.y),self.pac.vel)
        self.AddScore()

    #addes to the score when pac-man collides with foods
    #Also removes food object from list if it collides with pac-man
    def AddScore(self):
        #each if pacman character collides with any of foods
        for f in self.foods:
            if f.x <= self.pac.x < (f.x + f.width) or f.x < ((self.pac.x + self.pac.width) < (f.x + f.width)):
                if f.y <= self.pac.y < (f.y + f.length) or f.y < ((self.pac.y + self.pac.height) < (f.y + f.length)):
                    #play sound effect
                    self.eatingS.play()
                    #add the food worth to score
                    self.score += f.worth
                    #remove food from foods list
                    self.foods.pop(self.foods.index(f))

    #collsion between characters
    def charCollision(self):
        #list with all ghosts locations
        ghostsLoc = [(self.blinky.x,self.blinky.y),(self.pinky.x,self.pinky.y),
                     (self.inky.x,self.inky.y),(self.clyde.x,self.clyde.y)]
        #check if pac collides with any of the ghots
        for i in ghostsLoc:
            if i[0] == self.pac.x and i[1] == self.pac.y:
                #calling death of pac animation
                self.deathAni()
                #ressting pac character to starting direction and location
                self.pac.vel = [-1,0]
                self.pac.x = 195
                self.pac.y = (17+3)*15
                #decreasing pac-man lives
                self.pac.lives = self.pac.lives - 1

    #pac-man death animation
    def deathAni(self):
        #pause bg music
        pygame.mixer.music.pause()
        self.deathPS.play()
        #Pictures for animation
        deathPics = [pygame.image.load("deathP0.png"),pygame.image.load("deathP1.png"),
                     pygame.image.load("deathP2.png"),pygame.image.load("deathP3.png"),
                     pygame.image.load("deathP4.png"),pygame.image.load("deathP5.png"),
                     pygame.image.load("deathP6.png"),pygame.image.load("deathP7.png"),
                     pygame.image.load("deathP8.png"),pygame.image.load("deathP9.png"),
                     pygame.image.load("deathP10.png"),pygame.image.load("deathP11.png")]
        #display each image
        for i in range(len(deathPics)):
            pygame.time.delay(210)
            self.wnd.blit(deathPics[i],(self.pac.x,self.pac.y))
            #update window
            pygame.display.update()
        #unpdause bg music
        pygame.mixer.music.unpause()

    #checks how the game has ended
    #calls wnd for the end of the games
    def endC(self):
        if self.pac.lives <= 0:
            #closing the game window
            pygame.display.quit()
            #create an instance of the end window
            endWnd(self.score,0)
        elif self.foods == []:
            #closing the game window
            pygame.display.quit()
            #create an instance of the end window
            endWnd(self.score,1)

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

#The path for the folder with all the additional resources
dir = "\\Resources\\"
#Starting the application
App = welcomeWnd()
