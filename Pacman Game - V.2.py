#    15-112: Principles of Programming and Computer Science
#    Term Project
#    Creator:  Jumana Al-Saeed

#    Modification History:
#    Start             End
#    9/11/19           30/11/2019

#    Raw Images and Sounds files from:
#    Welcome Window Heading: https://www.ssbwiki.com/File:Pac-Man_title.png
#    Game background:        https://www.spriters-resource.com/arcade/pacman/sheet/52631/
#    Character Sprites Map:  https://github.com/rm-hull/big-bang/tree/master/examples/pacman
#    Sounds:                 https://www.sounds-resource.com/arcade/pacman/sound/10603/

import tkinter as tk
import pygame
pygame.init()


class welcomeWnd:
    """Welcome window using tkinter
    Takes 1 string parameter of the path of the folder which contains all the resources
    It has 3 buttons: 1 will start the game, 1 will create a window with the top 5 scores
     and 1 that will create a window with how to play instructions"""
    def __init__(self,dir):
        self.dir = dir
        # tkinter window
        self.wnd = tk.Tk()
        self.wnd.title("Welcome to Pac-Man")
        self.wnd.geometry("900x550")
        self.wnd.configure(bg="black")
        # call a method if the wnd was closed
        self.wnd.protocol("WM_DELETE_WINDOW")
        # Display Game Title
        self.gameTPic = tk.PhotoImage(file=self.dir+"Pacman Title.png")
        self.gameTL = tk.Label(self.wnd,image=self.gameTPic,bd=0)
        self.gameTL.pack()
        # Start game button
        self.startB = tk.Button(self.wnd, text="START GAME", command= self.startG)
        self.startB.configure(font=("fixedsys",35),bg="black",fg="yellow2",relief="flat")
        self.startB.configure(activebackground="black",activeforeground="gold4",bd=0)
        self.startB.pack()
        # high scores button
        self.hScoreB = tk.Button(self.wnd, text="HIGH SCORES",command=self.highScoreD)
        self.hScoreB.configure(font=("fixedsys",20),bg="black",fg="cyan2",relief="flat")
        self.hScoreB.configure(activebackground="black",activeforeground="cyan4",bd=0)
        self.hScoreB.pack()
        # how to play button
        self.hTPlayB = tk.Button(self.wnd, text="HOW TO PLAY",command=self.hTPlayD)
        self.hTPlayB.configure(font=("fixedsys",20),bg="black",fg="SpringGreen2",relief="flat")
        self.hTPlayB.configure(activebackground="black",activeforeground="green4",bd=0)
        self.hTPlayB.pack()
        # keeping track of the open windows
        self.hScoreW = []
        self.hTPlayW = []
        # background music
        self.music = pygame.mixer.music.load(self.dir+"welcomeM.wav")
        pygame.mixer.music.play(-1)
        self.lb = tk.Label(self.wnd,height=2,bg="black")
        self.lb.pack(side="bottom")
        self.animationC = tk.Canvas(self.wnd,width=900,height=50,bg="black",highlightthickness=0)
        self.animationC.pack(side="bottom")
        self.animationCounter = 0
        # pac- man images for animation
        self.faceingL = [tk.PhotoImage(file=self.dir+'WpmL0.png'), tk.PhotoImage(file=self.dir+'WpmL0.png'),
                    tk.PhotoImage(file=self.dir+'WpmL2.png'), tk.PhotoImage(file=self.dir+'WpmL3.png')]
        self.faceingR = [tk.PhotoImage(file=self.dir+'WpmR0.png'), tk.PhotoImage(file=self.dir+'WpmR1.png'),
                    tk.PhotoImage(file=self.dir+'WpmR2.png'), tk.PhotoImage(file=self.dir+'WpmR3.png')]
        # ghosts images for animation - [right direction, left direction]
        self.blinky = [tk.PhotoImage(file=self.dir+"WblinkyR.png"),tk.PhotoImage(file=self.dir+"WblinkyL.png")]
        self.pinky = [tk.PhotoImage(file=self.dir+"WpinkyR.png"),tk.PhotoImage(file=self.dir+"WpinkyL.png")]
        self.inky = [tk.PhotoImage(file=self.dir+"WinkyR.png"),tk.PhotoImage(file=self.dir+"WinkyL.png")]
        self.clyde = [tk.PhotoImage(file=self.dir+"WclydeR.png"),tk.PhotoImage(file=self.dir+"WclydeL.png")]
        # keeping track of animation direction
        self.goingR = True
        # start the animation of the window
        self.nextAni = self.animationC.after(100,self.animation)
        # Doesnt allow users to rezie the window
        self.wnd.resizable(0,0)
        self.wnd.mainloop()

    def animation(self):
        """Controls the animation on the welcome window"""
        self.animationC.delete(tk.ALL)
        # calculating main x location in the canvas
        pos = 10*self.animationCounter
        # if heading towards the right & still in window
        if pos < 1250 and self.goingR == True:
            self.animationC.create_image(pos,30,image=self.faceingR[self.animationCounter%4])
            self.animationC.create_image(1.03*(pos-70),30,image=self.blinky[0])
            self.animationC.create_image((pos-100),30,image=self.pinky[0])
            self.animationC.create_image((pos-170),30,image=self.inky[0])
            self.animationC.create_image(0.9*(pos-220),30,image=self.clyde[0])
            self.animationCounter += 1
        elif self.goingR == True:
            self.goingR = False
            self.animationCounter -= 10
        # if heading in the left direction & still in window
        if pos > -250 and self.goingR == False:
            self.animationC.create_image(pos,30,image=self.faceingL[self.animationCounter % 4])
            self.animationC.create_image((pos+230),30,image=self.clyde[1])
            self.animationC.create_image((pos+130),30,image=self.pinky[1])
            self.animationC.create_image(1.1*(pos+40),30,image=self.inky[1])
            self.animationC.create_image(1.3*(pos+25),30,image=self.blinky[1])
            self.animationCounter -= 1
        else:
            self.goingR = True
        self.nextAni = self.animationC.after(100, self.animation)

    def startG(self):
        """Pressing the start button"""
        # fadeout background music
        pygame.mixer.music.fadeout(1000)
        self.animationC.after_cancel(self.nextAni)
        self.wnd.destroy()
        # start an instance of the game
        game(self.dir)

    def highScoreD(self):
        """Pressing the high scores button to display hScore wnd"""
        if self.hScoreW == [] or self.hScoreW[0].open == False:
            self.hScoreW = [highScoreWnd(self.dir)]

    def hTPlayD(self):
        """Pressing the hTPlay button to display"""
        if self.hTPlayW == [] or self.hTPlayW[0].open == False:
            self.hTPlayW = [hTPlayWnd()]

    def wndClosed(self):
        """if the window was closed"""
        self.animationC.after_cancel(self.nextAni)
        self.wnd.destroy()


class highScoreWnd:
    """Creates a tkinter window which displays the top 5 scores with corresponding player names
    It takes a string of the folder with all the resources path as parameter
    Also only one of this window can be open at the same time"""
    def __init__(self,dir):
        self.dir = dir
        # creating the window
        self.wnd = tk.Toplevel()
        self.wnd.title("Pac-Man High Scores")
        self.wnd.configure(bg="black")
        # call a method if the window was closed
        self.wnd.protocol("WM_DELETE_WINDOW", self.wndClosed)
        # keeping track if the wnd is open or not
        self.open = True
        # wnd heading
        self.heading = tk.Label(self.wnd,text="HIGH SCORES",font=("fixedsys", 40))
        self.heading.configure(bg="black",fg="white",pady=30,padx=200)
        self.heading.pack()
        # frame for table placement
        self.frame = tk.Frame(self.wnd,bg="black")
        self.frame.pack()
        # list for each column
        self.iconC = []
        self.scores = []
        self.names = []
        # calling function which creates widgets for scores table
        self.scoreTb()
        self.design = tk.Label(self.frame,bg="black",pady=10)
        self.design.grid(column=0,row=5)
        # Doesnt allow users to rezie the window
        self.wnd.resizable(0,0)

    def scoreTb(self):
        """Displaying top 5 scores"""
        self.iconsPics = [tk.PhotoImage(file=self.dir+'WpmR1.png'), tk.PhotoImage(file=self.dir+"WblinkyR.png"),
                          tk.PhotoImage(file=self.dir+"WpinkyR.png"), tk.PhotoImage(file=self.dir+"WinkyR.png"),
                          tk.PhotoImage(file=self.dir+"WclydeR.png")]
        # opening file to get scores saves
        with open(self.dir+"Scores.txt", "r") as f:
            for i in range(5):
                # Creating canvas widgets to put icons in
                self.iconC.append(tk.Canvas(self.frame,width=50,height=50,bg="black",highlightthickness=0))
                # adding image to canvas
                self.iconC[i].create_image(25,25,image=self.iconsPics[i])
                self.iconC[i].grid(column=0,row=i)
                # getting data from file
                info = f.readline().split("@@")[1:]
                # if file has less than 5 scores saved
                if info == []:
                    info = ["0","---------"]
                # Adding labels to display scores
                self.scores.append(tk.Label(self.frame,font=("fixedsys",15),bg="black",fg="white",
                                            text=str(i+1)+" - " + "0"*(4-len(info[0])) + info[0]))
                self.scores[i].grid(column=1,row=i)
                # adding labels to display player name
                self.names.append(tk.Label(self.frame,font=("fixedsys",15),
                                            text="  " + info[1].replace("\n",""),bg="black",fg="white"))
                self.names[i].grid(column=2,row=i,sticky=tk.W)

    def wndClosed(self):
        """if the window was closed"""
        self.open = False
        self.wnd.destroy()


class hTPlayWnd:
    """Creates a tkinter window with instructions of how to play
    Also only one of this window can be open at the same time"""
    def __init__(self):
        # creating the window
        self.wnd = tk.Toplevel()
        self.wnd.title("How To Play Pac-Man")
        self.wnd.configure(bg="black")
        # call a method if the window was closed
        self.wnd.protocol("WM_DELETE_WINDOW", self.wndClosed)
        # keeping track if the wnd is open or not
        self.open = True
        # wnd heading
        self.heading = tk.Label(self.wnd,text="HOW TO PLAY",font=("fixedsys",40))
        self.heading.configure(bg="black",fg="cyan",pady=30,padx=200)
        self.heading.pack()
        # How to play instructions
        self.instr = tk.Text(self.wnd,width=41,height=8,font=("fixedsys",30))
        self.instr.configure(bg='black',fg="cyan4",bd=0)
        self.instrMsg = "\n Move Pac-Man using Arrow or 'WASD' keys " + \
                        "\n\n\tPause game using 'ESC' key" + \
                        "\n\n\tUnpause game using 'c' key"
        self.instr.insert(tk.END,self.instrMsg)
        # don't allow user to modify textbox
        self.instr.configure(state="disabled")
        self.instr.pack()
        # Doesnt allow users to rezie the window
        self.wnd.resizable(0,0)

    def wndClosed(self):
        """if the window was closed"""
        self.open = False
        self.wnd.destroy()


class endWnd:
    """Creates a tkinter window for when the game ends.
    It take the following 3 parameters:
      the score at the end of the game, 0 if the game was lost or 1 if the game was won
      and a string for the path of the folder that contains the txt file with all the scores"""
    def __init__(self,score,end,dir):
        self.dir = dir
        # creating a tkinter window
        self.wnd = tk.Tk()
        self.wnd.title("Game End")
        self.wnd.geometry("700x400")
        self.wnd.configure(bg="black")
        self.score = score
        self.end = end
        # creating heading
        self.hOptions = ["TRY AGAIN","CONGRATULATIONS"]
        self.heading = tk.Label(self.wnd,bg="black",fg="yellow",pady=20)
        self.heading.configure(text=self.hOptions[self.end],font=("fixedsys",50))
        self.heading.pack()
        # displaying the score
        self.scoreL = tk.Label(self.wnd,bg="black",fg="white",font=("fixedsys",20),pady=20)
        self.scoreL.configure(text="SCORE  " + "0"*(4-len(str(self.score))) + str(self.score))
        self.scoreL.pack()
        # player name label
        self.nameF = tk.Frame(self.wnd,bg="black")
        self.nameF.pack()
        self.nameL = tk.Label(self.nameF,text="NAME:",padx=15,bg="black",fg="white",font=("fixedsys",10))
        self.nameL.grid(column=0,row=0)
        # entry box for user to insert name
        self.nameE = tk.Entry(self.nameF)
        self.nameE.grid(column=1,row=0)
        # button to save score and player name
        self.saved = False
        self.nameB = tk.Button(self.nameF,text="SUBMIT SCORE",padx=20,bg="black",fg="red",relief="flat",bd=0)
        self.nameB.configure(font=("fixedsys",10),activebackground="black",activeforeground="red4",command=self.submit)
        self.nameB.grid(column=3,row=0)
        # for placement desgin
        self.design = tk.Label(self.wnd,bg="black",height=4)
        self.design.pack()
        # frame to put buttons
        self.buttonF = tk.Frame(self.wnd,bg="black")
        self.buttonF.pack()
        # button to play again
        self.playB = tk.Button(self.buttonF,text="PLAY AGAIN",font=("fixedsys",20),bd=0,padx=10,command=self.playA)
        self.playB.configure(bg="black",fg="yellow2",activebackground="black",activeforeground="gold4",relief="flat")
        self.playB.grid(column=0,row=0)
        # button to go back to welcome window
        self.menuB = tk.Button(self.buttonF,text="MAIN MENU",font=("fixedsys",20),bd=0,padx=10,command=self.mainMenu)
        self.menuB.configure(bg="black",fg="cyan2",activebackground="black",activeforeground="cyan4",relief="flat")
        self.menuB.grid(column=1,row=0)
        # button to quit application
        self.quitB = tk.Button(self.buttonF,text="QUIT",font=("fixedsys",20),bd=0,padx=10,command=self.quit)
        self.quitB.configure(bg="black",fg="red",activebackground="black",activeforeground="red4",relief="flat")
        self.quitB.grid(column=2,row=0)
        # Doesnt allow user to resize the window
        self.wnd.resizable(0,0)
        self.wnd.mainloop()

    def submit(self):
        """function for submit button
        It only allows the user to submit their score once and
        it calls the method read_order that will store the score and player name into a txt file"""
        if self.saved == False:
            self.saved = True
            name = self.nameE.get()
            self.read_order(name)

    def read_order(self,name):
        """reads socres from file & order from from highest to lowest"""
        namesL = [name]
        scoresL = [self.score]
        # read saved scores and player names & and them to the lists
        with open(self.dir+"Scores.txt", "r") as f:
            info = f.readline()
            while info and info != "\n":
                # split string into the seperate data
                infoS = info.split("@@")[1:]
                scoresL.append(int(infoS[0]))
                namesL.append(infoS[1].replace("\n", ""))
                info = f.readline()
        # lists to store sorted data
        newNameL = []
        newScoreL = []
        num = len(scoresL)
        for i in range(num):
            # add the data for the player with the highest score into sorted lists
            newScoreL.append(max(scoresL))
            newNameL.append(namesL[scoresL.index(max(scoresL))])
            # remove data of the player with the highest score from list of unsorted data
            namesL.pop(scoresL.index(max(scoresL)))
            scoresL.pop(scoresL.index(max(scoresL)))
        self.saveData(newNameL,newScoreL)

    def saveData(self,nameL,scoreL):
        """function to save data into score file"""
        # lists to store all the data to save
        newInfo = []
        # join each player data together into 1 element in newInfo list
        for i in range(len(scoreL)):
            playerInfo = "@@" + str(scoreL[i]) + "@@" + nameL[i] + "\n"
            newInfo.append(playerInfo)
        # save the sorted infomation into file
        with open(self.dir+"Scores.txt", "w") as f:
            f.writelines(newInfo)

    def playA(self):
        """function for the play again button"""
        self.wnd.destroy()
        # create an instance of the game
        game(self.dir)

    def mainMenu(self):
        """function for the main menu button"""
        self.wnd.destroy()
        # create an instance of the welcome wnd
        welcomeWnd(self.dir)

    def quit(self):
        """function for quit button"""
        self.wnd.destroy()


class pacman:
    """Used to create the character the user controls; pac-man
    Contains methods that display and animate pac-man and
        the movement of the character and movement validation
    It requires the following 4 parameters:
        x coords, y coords, a list of the walls in the game
        and a string for the path for the folder with all the images"""
    def __init__(self,x,y,w,dir):
        self.dir = dir
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        #number of pixels it moves every time
        self.speed = 15
        #determines direction movement (vector)
        self.vel = [-1,0]
        #moveCount is used for animation
        self.moveCount = 0
        self.lives = 4
        self.walls = w
        #Declare images for pacman animation
        self.faceingL = [pygame.image.load(self.dir+'pmL0.png'), pygame.image.load(self.dir+'pmL1.png'),
                         pygame.image.load(self.dir+'pmL2.png'), pygame.image.load(self.dir+'pmL3.png')]
        self.faceingR = [pygame.image.load(self.dir+'pmR0.png'), pygame.image.load(self.dir+'pmR1.png'),
                         pygame.image.load(self.dir+'pmR2.png'), pygame.image.load(self.dir+'pmR3.png')]
        self.faceingU = [pygame.image.load(self.dir+'pmU0.png'), pygame.image.load(self.dir+'pmU1.png'),
                         pygame.image.load(self.dir+'pmU2.png'), pygame.image.load(self.dir+'pmU3.png')]
        self.faceingD = [pygame.image.load(self.dir+'pmD0.png'), pygame.image.load(self.dir+'pmD1.png'),
                         pygame.image.load(self.dir+'pmD2.png'), pygame.image.load(self.dir+'pmD3.png')]

    def draw(self,wnd):
        """Used to display pac-man on the game window
            It is based on pac-man's velocity to determine which direction he is facing
            It is responsible for the animation of pac-man as well"""
        # if out of animation images
        if self.moveCount > 3:
            self.moveCount = 0
        if self.vel[0] == 1:
            wnd.blit(self.faceingR[self.moveCount],(self.x,self.y))
        elif self.vel[0] == -1:
            wnd.blit(self.faceingL[self.moveCount], (self.x, self.y))
        elif self.vel[1] == 1:
            wnd.blit(self.faceingU[self.moveCount], (self.x, self.y))
        elif self.vel[1] == -1:
            wnd.blit(self.faceingD[self.moveCount], (self.x, self.y))
        self.moveCount += 1

    def move(self):
        """changes the coords of pac-man based on its velocity if the move is valid
        It also makes the necessary changes if he goes through the tunnel in the game"""
        # if moving right or left
        if self.vel[0] != 0:
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                self.x += self.speed*self.vel[0]
                # changes coordinates if goes through the tunnel from either side
                if self.x < 0:
                    self.x = 27*15
                elif self.x > 27*15:
                    self.x = 0
        # if moving up or down
        elif self.vel[1] != 0:
            if self.validM([self.x,(self.y + self.speed*self.vel[1]*(-1))]):
                self.y += self.speed*self.vel[1]*(-1)

    def validM(self,location):
        """Checks if the move is valid or not based on the coordinates in the parameter location.
            Returns True if character doesnt collide with any walls
            Returns false if the character does collide with a wall"""
        for w in self.walls:
            if (w.x <= location[0] < (w.x + w.width)) or (w.x < ((location[0] + self.width) < (w.x + w.width))):
                if (w.y <= location[1] < (w.y + w.length)) or (w.y < ((location[1] + self.height) < (w.y + w.length))):
                    return False
        return True


class ghost:
    """used to create the ghosts (enemies) in the game
    requires the following 6 parameters:
        x coords, y coords, color, a list of the walls in the game,
        current behaviour mode and a sting to the directory that contains all the images
    It contains methods to display the ghosts on the window and the methods that control the
    movement of the ghosts including the different AIs"""
    def __init__(self,x,y,c,w,mode,dir):
        self.dir = dir
        self.x = x
        self.y = y
        self.width = 15
        self.height = 15
        self.speed = 15
        self.vel = [-1, 0]
        self.mode = mode
        #ghost type
        self.color = c
        #images used for diplay
        self.blinkyPics = [pygame.image.load(self.dir+"blinkyL.png"), pygame.image.load(self.dir+"blinkyR.png"),
                           pygame.image.load(self.dir+"blinkyU.png"), pygame.image.load(self.dir+"blinkyD.png")]
        self.pinkyPics = [pygame.image.load(self.dir+"pinkyL.png"), pygame.image.load(self.dir+"pinkyR.png"),
                          pygame.image.load(self.dir+"pinkyU.png"), pygame.image.load(self.dir+"pinkyD.png")]
        self.inkyPics = [pygame.image.load(self.dir+"inkyL.png"), pygame.image.load(self.dir+"inkyR.png"),
                         pygame.image.load(self.dir+"inkyU.png"), pygame.image.load(self.dir+"inkyD.png")]
        self.clydePics = [pygame.image.load(self.dir+"clydeL.png"), pygame.image.load(self.dir+"clydeR.png"),
                          pygame.image.load(self.dir+"clydeU.png"), pygame.image.load(self.dir+"clydeD.png")]
        #ghost design / look based on type (color)
        self.images = self.setImages()
        self.target = (0,0)
        #walls in the game used for ghost AI
        self.walls = w

    def callAI(self,pacLocation,pacDir,blinkyLoc):
        """calls AI method based on color / ghost type"""
        if self.color == "red":
            self.blinkyAI(pacLocation)
        elif self.color == "pink":
            self.pinkyAI(pacLocation,pacDir)
        elif self.color == "blue":
            self.inkyAI(pacLocation,pacDir,blinkyLoc)
        elif self.color == "orange":
            self.clydeAI(pacLocation)

    def blinkyAI(self,pacLocation):
        """AI responsible for movement decisions for red ghost blinky
        If the ghost is in scatter mode
            then the target coordinates are set to coordinates in the top right corner of the game board
        Otherwise the target coordinates are set to pac-man's coordinates
        Calls possibleDir method that will determine all possible valid moves
        and then calls minDistance method that will set the ghost velocity corresponding to
            the shortest path to target coordinates"""
        if self.mode == "chase":
            self.target = pacLocation
        elif self.mode == "scatter":
            self.target = (25*15,-1*15)
        possibleDir = self.possibleDirection()
        self.minDistance(possibleDir)

    def pinkyAI(self,pacLocation,pacDir):
        """AI responsible for movement decisions for pink ghost pinky
        If the ghost is in scatter mode then the target coords are set to...
            coords in the top left corner of the game
        Otherwise the target coordinates are set to 4*15px from pac-man's...
            coords in the direction he is facing unless ...
            he is facing up then it is 4*15px over and 4*15px to the left
        Calls possibleDir method that will determine all possible valid moves
        and then calls minDistance method that will set the ghost velocity corresponding to...
            the shortest path to target coordinates"""
        if self.mode == "chase":
            # setting target location on pacman location and facing direction
            if pacDir == [1,0]:
                self.target = (pacLocation[0]+(15*4),pacLocation[1])
            elif pacDir == [-1,0]:
                self.target = (pacLocation[0]-(15*4),pacLocation[1])
            elif pacDir == [0,1]:
                self.target = (pacLocation[0]-(15*4),pacLocation[1]-(15*4))
            elif pacDir == [0,-1]:
                self.target = (pacLocation[0],pacLocation[1]+(15*4))
        elif self.mode == "scatter":
            self.target = (2*15,-1*15)
        possibleDir = self.possibleDirection()
        self.minDistance(possibleDir)

    def inkyAI(self,pacLocation,pacDir,blinkyLoc):
        """AI responsible for movement decisions for blue ghost inky
        If the ghost is in scatter mode then the target coords are set to ...
            coords in the bottom right corner of the game
        Otherwise the a temp target coords are set to pac-man's similar to pinky's target coords,
            the vector from temp target coords to blinky's coords is reflected to get inky's target coords
        Calls possibleDir method that will determine all possible valid moves
        and then calls minDistance method that will set the ghost velocity corresponding to
            the shortest path to target coordinates"""
        if self.mode == "chase":
            # setting target location on pacman location and facing direction
            if pacDir == [1,0]:
                self.target = (pacLocation[0]+(15*2),pacLocation[1])
            elif pacDir == [-1,0]:
                self.target = (pacLocation[0]-(15*2),pacLocation[1])
            elif pacDir == [0,1]:
                self.target = (pacLocation[0]-(15*2),pacLocation[1] -(15*2))
            elif pacDir == [0,-1]:
                self.target = (pacLocation[0],pacLocation[1]+(15*2))
            # setting target coordinates that is a reflection from blinky's coordinates
            self.target = (self.target[0]-(blinkyLoc[0]-self.target[0]),
                           self.target[1]-(blinkyLoc[1]-self.target[1]))
        elif self.mode == "scatter":
            self.target = (27*15,31*15)
        possibleDir = self.possibleDirection()
        self.minDistance(possibleDir)

    def clydeAI(self, pacLocation):
        """AI responsible for movement decisions for orange ghost clyde
        If the ghost is within 8 tiles (15*8 px) or in scatter mode...
            then the target coordinates are set to coordinates in the bottom left corner of the game
        Otherwise the target coordinates are set to pac-man's coordinates
        Calls possibleDir method that will determine all possible valid moves
        and then calls minDistance method that will set the ghost velocity corresponding to
            the shortest path to target coordinates"""
        distance = (((pacLocation[0]-self.x)**2)+((pacLocation[1]-self.y)**2))*(1/2)
        if distance <= (8*15) or self.mode == "scatter":
            self.target = (0,31*15)
        else:
            self.target = pacLocation
        possibleDir = self.possibleDirection()
        self.minDistance(possibleDir)

    def minDistance(self,possibleDir):
        """calculates the distance from every possible move to the target coordinates
            and sets the ghost velocity to the move that has the smallest distance
        It has a parameter of a list of tuples that contains all possible directions"""
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
        bestDir = possibleDir[distances.index(minDist)]
        self.vel = [bestDir[0],bestDir[1]]

    def possibleDirection(self):
        """determines all the possible directions that the ghost could turn
        A ghost is not allowed to turn 180 degrees and not allowed to turn into a wall
        Returns a list of tuples of possible directions (velocities)"""
        # ghosts not allowed to turn 180 degrees
        if self.vel == [1,0]:
            possibleDir = [(1,0),(0,1),(0,-1)]
        elif self.vel == [-1,0]:
            possibleDir = [(-1, 0),(0, 1),(0, -1)]
        elif self.vel == [0,1]:
            possibleDir = [(1,0),(-1,0),(0,1)]
        elif self.vel == [0,-1]:
            possibleDir = [(1,0),(-1,0),(0,-1)]
        temp = list(possibleDir)
        # for each possible direction check if it is a valid move(doesnt collid with wall)
        for direction in temp:
            if not self.validM([self.x + self.speed*direction[0],self.y + self.speed*direction[1]*(-1)]):
                possibleDir.remove(direction)
        return possibleDir

    def move(self,pacLocation,pacDir,blinkyLoc=(0,0)):
        """Responsible for the movement of a ghost object
        It takes the following 3 parameters but only needs the first 2:
            a tuple of pac-man's coordinates, pac-man's velocity,
            and a tuple of the ghost blinky's coordinates
        It calls the method callAI and based on the AI changes, moves the ghost to its new coordinates.
        It also makes the necessary changes if the ghost goes through the tunnel in the game"""
        self.callAI(pacLocation,pacDir,blinkyLoc)
        # if moving right or left
        if self.vel[0] != 0:
            if self.validM([self.x + self.speed*self.vel[0],self.y]):
                self.x += self.speed*self.vel[0]
                # changes coordinates if goes through the tunnel from either side
                if self.x < 0:
                    self.x = 27*15
                elif self.x > 27*15:
                    self.x = 0
        # if moving up or down
        if self.vel[1] != 0:
            if self.validM([self.x,self.y + self.speed*self.vel[1]*(-1)]):
                self.y += self.speed*self.vel[1]*(-1)

    def validM(self, location):
        """Checks if the move is valid or not based on the coordinates in the parameter location.
        Returns True if character doesnt collide with any walls
        Returns false if the character does collide with a wall"""
        for w in self.walls:
            if w.x <= location[0] < (w.x + w.width) or w.x < ((location[0] + self.width) < (w.x + w.width)):
                if w.y <= location[1] < (w.y + w.length) or w.y < ((location[1] + self.height) < (w.y + w.length)):
                    return False
        return True

    def draw(self,wnd):
        """Displays ghost image based on velocity to decide which direction its facing.
        needs the parameter of the game window"""
        if self.vel[0] == 1:
            wnd.blit(self.images[1],(self.x,self.y))
        elif self.vel[0] == -1:
            wnd.blit(self.images[0],(self.x,self.y))
        elif self.vel[1] == 1:
            wnd.blit(self.images[2],(self.x,self.y))
        else:
            wnd.blit(self.images[3],(self.x,self.y))

    def setImages(self):
        """Setting the right list of images for that type of ghost based on its color"""
        if self.color == "red":
            return self.blinkyPics
        elif self.color == "pink":
            return self.pinkyPics
        elif self.color == "blue":
            return self.inkyPics
        elif self.color == "orange":
            return self.clydePics


class wall:
    """used to create the walls in the game that resict character movement
    Needs the following 4 parameters:
        x coordinates, y coordinates,width and length"""
    def __init__(self,x,y,width,length):
        self.x = x
        self.y = y
        self.width = width
        self.length = length


class food:
    """Used for creating the dots and pellets (food) in the game
    Needs the following 3 parameter:
        x coordinate, y coordinate and how many points its worth"""
    def __init__(self,x,y,w):
        #directory for resources
        self.dir = "Resources\\"
        self.x = x
        self.y = y
        self.width = 15
        self.length = 15
        self.foodPics = [pygame.image.load(self.dir+"food10.png"), pygame.image.load(self.dir+"food50.png")]
        self.worth = w

    def draw(self,wnd):
        """Displays the correct image based on how much many points the object is worth"""
        if self.worth == 10:
            wnd.blit(self.foodPics[0],(self.x,self.y))
        elif self.worth == 50:
            wnd.blit(self.foodPics[1],(self.x,self.y))


class game:
    """Uses pygame to create a window and is responsible for running the game
    It uses other classes and their methods within the game.
    Responsible for the interaction between the different class objects,
    creating a user interface for the game, and runs the game overall
    It needs a string of the path to the folder that contains all the resources as parameter """
    def __init__(self,dir):
        # directory for resources
        self.dir = dir
        # Creating game window
        self.wnd = pygame.display.set_mode((28*15,(31+5)*15))
        pygame.display.set_caption("PACMAN")
        self.bg = pygame.image.load(self.dir+"background.png")
        self.wnd.blit(self.bg,(0,3 *15))

        self.clock = pygame.time.Clock()

        # lists to store wall objects and food objects and call methods to create the objects
        self.walls = []
        self.createWalls()
        self.foods = []
        self.createFoods()
        # creating an instance of the class pac-man
        # the character the user controls
        self.pac = pacman(195,(23+3)*15,self.walls,self.dir)
        # creates the 4 enemies in the game using ghost class
        self.blinky = ghost(195,(11+3)*15,"red",self.walls,"scatter",self.dir)
        self.pinky = ghost(195,(11+3)*15,"pink",self.walls,"scatter",self.dir)
        self.inky = ghost(195,(11+3)*15,"blue",self.walls,"scatter",self.dir)
        self.clyde = ghost(195,(11+3)*15,"orange",self.walls,"scatter",self.dir)

        # loading sound effects
        self.eatingS = pygame.mixer.Sound(self.dir+"munch_1.wav")
        self.deathPS = pygame.mixer.Sound(self.dir+"death_1.wav")

        self.time = 0
        self.run = True
        self.end = False
        self.score = 0
        self.paused = False

        #call method to start the game
        self.startGame()

    def startGame(self):
        """Contains the main loop for the game.
        It calls all needed game functions while the game is running and not currently paused
        Calls countDown method and starts background music before game while loop
        In game loop it calls the methods that does the following:
            updates the display, gets user input, moves all the characters, changes ghosts game modes
        It also checks if the game has ended or if the user quit the window"""
        self.countDown()
        self.music = pygame.mixer.music.load(self.dir+"siren_2.wav")
        pygame.mixer.music.play(-1)
        while self.run and (not self.paused):
            self.clock.tick(8)
            self.redrawGameWindow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.getUserInput()
            self.changeGM()
            self.moveChars()
            if (self.pac.lives <= 0) or (self.foods == []):
                pygame.mixer.music.stop()
                self.run = False
                self.end = True
                self.endC()
            self.time += 1
        if self.run == False and self.end == False:
            pygame.quit()

    def countDown(self):
        """Displays ready message for about 3 seconds when the game window first starts
            before the actual game can start"""
        self.redrawGameWindow()
        font = pygame.font.SysFont("comicsans",30)
        font.set_italic(True)
        readyTxt = font.render("READY!",-1,(255,0,0),(0,0,0))
        self.wnd.blit(readyTxt,(11*15+5,20*15))
        pygame.display.update()
        pygame.time.delay(2000)
        self.pac.lives = 3

    def getUserInput(self):
        """Gets input from user and make appropriate changes.
        Will change the velocity (direction) of pac-man based on the user
        input only if the direction is considered valid.
        If the ESC key is pressed pauseG method is called."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            if self.pac.validM([self.pac.x + self.pac.speed,self.pac.y]):
                self.pac.vel = [1,0]
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            if self.pac.validM([self.pac.x - self.pac.speed,self.pac.y]):
                self.pac.vel = [-1,0]
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            if self.pac.validM([self.pac.x,self.pac.y - self.pac.speed]):
                self.pac.vel = [0,1]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if self.pac.validM([self.pac.x, self.pac.y + self.pac.speed]):
                self.pac.vel = [0,-1]
        if keys[pygame.K_ESCAPE]:
            self.pauseG()

    def pauseG(self):
        """What happens when the game is paused(using the ESC key)
        Displays pause message on window, pauses and unpauses background music.
        Stays paused until c key pressed or the window is closed"""
        self.paused = True
        font = pygame.font.SysFont("comicsans",30)
        pauseTxt = font.render("PAUSED",1,(255,0,0),(0,0,0))
        self.wnd.blit(pauseTxt,(11*15+5,20*15))
        pygame.display.update()
        pygame.mixer.music.pause()
        while self.paused == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.paused = False
                    self.run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                self.paused = False
                pygame.mixer.music.unpause()

    def redrawGameWindow(self):
        """Responsible for displaying everything on the game window.
        It resets the background and then calls all necessary functions
        to display all game components"""
        self.wnd.fill((0,0,0))
        self.wnd.blit(self.bg,(0,3*15))
        self.drawScore()
        for f in self.foods:
            f.draw(self.wnd)
        self.pac.draw(self.wnd)
        self.blinky.draw(self.wnd)
        self.pinky.draw(self.wnd)
        self.inky.draw(self.wnd)
        self.clyde.draw(self.wnd)
        self.drawLives()
        pygame.display.update()

    def drawLives(self):
        """displays icons that represent how many chances (lives) pac-man has"""
        livesPic = pygame.image.load(self.dir+'pmR1.png')
        for i in range(self.pac.lives-1):
            self.wnd.blit(livesPic,(i*20+5,34*15))

    def drawScore(self):
        """displays the current score on the window and the heading score"""
        font = pygame.font.SysFont("comicsans",30)
        scoreTxt = font.render("SCORE",2,(250,250, 250),(0,0,0))
        self.wnd.blit(scoreTxt,(11*15+10,5))
        scoreStr = "0"*(4-len(str(self.score)))+str(self.score)
        scoreN = font.render(scoreStr,1,(250,250,250),(0,0,0))
        self.wnd.blit(scoreN,(12*15+10,25))

    def moveChars(self):
        """calls all the functions to move all the characters in the game with
        their needed parameters. It also call the method charCollisions to each
        if any of the ghosts collided with pac-man. Lastly it calls the method
        Addscore"""
        self.pac.move()
        self.charCollision()
        self.blinky.move((self.pac.x,self.pac.y),self.pac.vel)
        self.pinky.move((self.pac.x,self.pac.y),self.pac.vel)
        self.inky.move((self.pac.x,self.pac.y),self.pac.vel,(self.blinky.x,self.blinky.y))
        self.clyde.move((self.pac.x,self.pac.y),self.pac.vel)
        self.charCollision()
        self.AddScore()

    def AddScore(self):
        """If pac-man collides with a food objects (a dot or pellet), it adds points to the score
        corresponding with how much the food object is worth
        and removes the object from the list foods which stores all
        instances of the food class. It also plays the sound effect for pac-man eating"""
        for f in self.foods:
            if f.x <= self.pac.x < (f.x + f.width) or f.x < ((self.pac.x + self.pac.width) < (f.x + f.width)):
                if f.y <= self.pac.y < (f.y + f.length) or f.y < ((self.pac.y + self.pac.height) < (f.y + f.length)):
                    self.eatingS.play()
                    self.score += f.worth
                    self.foods.pop(self.foods.index(f))

    def changeGM(self):
        """changes the modes of the ghosts at set times in the game.
        The ghost modes effect each ghosts's AI which controls their movement"""
        if self.time == 70 or self.time == 340 or self.time == 590 or self.time == 840:
            self.blinky.mode = "chase"
            self.pinky.mode = "chase"
            self.inky.mode = "chase"
            self.clyde.mode = "chase"
        elif self.time == 270 or self.time == 540 or self.time == 790:
            self.blinky.mode = "scatter"
            self.pinky.mode = "scatter"
            self.inky.mode = "scatter"
            self.clyde.mode = "scatter"

    def charCollision(self):
        """Checks if any of the ghost have collided with pac-man.
        If they have, decrease lives left, call deathAni method,
        reset pac-man coordinates and velocity, and call
        resetGhostLoc method"""
        ghostsLoc = [(self.blinky.x,self.blinky.y),(self.pinky.x,self.pinky.y),
                     (self.inky.x,self.inky.y),(self.clyde.x,self.clyde.y)]
        for i in ghostsLoc:
            if i[0] == self.pac.x and i[1] == self.pac.y:
                self.deathAni()
                self.pac.vel = [-1,0]
                self.pac.x = 195
                self.pac.y = (23+3)*15
                self.pac.lives = self.pac.lives - 1
                self.resetGhostLoc()

    def resetGhostLoc(self):
        """when pac-man dies, if a ghost is within a few tiles of pac-man's
        spawning coordinates then the ghost is transported to its initial
        coordinated from the start of the game"""
        ghosts = [self.blinky,self.pinky,self.inky,self.clyde]
        for g in ghosts:
            if (195-45 <= g.x <= 195+45) and g.y == (23+3)*15:
                g.x = 195
                g.y = (11+3)*15
                g.vel = [-1,0]

    def deathAni(self):
        """This method is called when one of the ghosts collide with the character pac-man.
        It pauses and unpauses the background music and plays the sound effect for pac-man's
        death. The main purpose of this method is to display the animation for pac-man's deaths"""
        pygame.mixer.music.pause()
        self.redrawGameWindow()
        self.deathPS.play()
        deathPics = [pygame.image.load(self.dir+"deathP0.png"),pygame.image.load(self.dir+"deathP1.png"),
                     pygame.image.load(self.dir+"deathP2.png"),pygame.image.load(self.dir+"deathP3.png"),
                     pygame.image.load(self.dir+"deathP4.png"),pygame.image.load(self.dir+"deathP5.png"),
                     pygame.image.load(self.dir+"deathP6.png"),pygame.image.load(self.dir+"deathP7.png"),
                     pygame.image.load(self.dir+"deathP8.png"),pygame.image.load(self.dir+"deathP9.png"),
                     pygame.image.load(self.dir+"deathP10.png"),pygame.image.load(self.dir+"deathP11.png")]
        for i in range(len(deathPics)):
            pygame.time.delay(210)
            self.wnd.blit(deathPics[i],(self.pac.x,self.pac.y))
            pygame.display.update()
        pygame.mixer.music.unpause()

    def endC(self):
        """This method is called when the game has ended.
        It closes the current game window and creates an instance
        of the class endWnd with the appropriate parameters based on how
        the game ended; either with a lose or a win for the user."""
        if self.pac.lives <= 0:
            pygame.display.quit()
            endWnd(self.score,0,self.dir)
        elif self.foods == []:
            pygame.display.quit()
            endWnd(self.score,1,self.dir)

    def createWalls(self):
        """Creates all the walls in the game using the class wall. All the wall
         objects are added to the list walls that is an attribute of the class game.
         The walls restrict the movement of the characters in the game."""
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
        self.walls.append(wall((7*15),((15+3)*15),(2*15),(5*15)))
        self.walls.append(wall((19*15),((15+3)*15),(2*15),(5*15)))
        self.walls.append(wall((13*15),((20+3)*15),(2*15),(3*15)))
        self.walls.append(wall((4*15),((21+3)*15),(2*15),(5*15)))
        self.walls.append(wall((22*15),((21+3)*15),(2*15),(5*15)))
        self.walls.append(wall((7*15),((24+3)*15),(2*15),(3*15)))
        self.walls.append(wall((19*15),((24+3)*15),(2*15),(3*15)))
        self.walls.append(wall((13*15),((26+3)*15),(2*15),(3*15)))
        self.walls.append(wall((10*15),((18+3)*15),(8*15),(2*15)))
        self.walls.append(wall((2*15),((21+3)*15),(2*15),(2*15)))
        self.walls.append(wall((24*15),((21+3)*15),(2*15),(2*15)))
        self.walls.append(wall((7*15),((21+3)*15),(5*15),(2*15)))
        self.walls.append(wall((16*15),((21+3)*15),(5*15),(2*15)))
        self.walls.append(wall((10*15),((24+3)*15),(8*15),(2*15)))
        self.walls.append(wall((2*15),((27+3)*15),(10*15),(2*15)))
        self.walls.append(wall((16*15),((27+3)*15),(10*15),(2*15)))
        self.walls.append(wall((10*15),((12+3)*15),(8*15),(1*15)))
        self.walls.append(wall((10*15),((16+3)*15),(8*15),(1*15)))
        self.walls.append(wall((10*15),((13+3)*15),(1*15),(3*15)))
        self.walls.append(wall((17*15),((13+3)*15),(1*15),(3*15)))

    def createFoods(self):
        """Creates all the dots/pellets (foods) that will be in the game
         using the food class and adding all the food objects to a list that stores
         all the food objects. The list is an attribute of the class game and starts
         as an empty list. Some food objects that are in a straight line are grouped
         together an added using for loops."""
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
        self.foods.append(food((1*15),((3+3)*15),50))
        self.foods.append(food((26*15),((3+3)*15),50))
        self.foods.append(food((1*15),((23+3)*15),50))
        self.foods.append(food((26*15),((23+3)*15),50))


# The path for the folder with all the additional resources
dir = "Resources\\"
# Starting the application
App = welcomeWnd(dir)