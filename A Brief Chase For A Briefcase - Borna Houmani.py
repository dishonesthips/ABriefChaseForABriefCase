#Borna Houmani
#A Brief Chase for a Briefcase
#1/18/15
#It's a stealth based side scroller video game

#Imports & initializes required modules
import pygame,os,time,pygame.mixer,platform,random
from pygame.locals import *  
from pygame.color import THECOLORS
pygame.init()  
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.mixer.init
#Set-up the main screen display window and caption  in the 
screen = pygame.display.set_mode((1024,640)) 
#Puts a caption in the bar at the top of the window
pygame.display.set_caption("A Brief Chase for a Briefcase - Borna Houmani") 

#Plays instrumental music produced by David Ha used in this game with his permission http://www.soundcloud.com/dxkoszn
song=pygame.mixer.Sound('DXKO - Cut Them Off.wav')
pygame.mixer.Sound.set_volume(song,.05)
song.play(loops=-1)


#Setting up visual assets that will be used in the game. Most character designs and the darts were drawn by Noel Herbert and were used in this game with his permission
#MENU
imageMENU=pygame.image.load('MENU.gif').convert()
#LOGO
LOGO=pygame.image.load('LOGO 2.gif').convert()
#PRESS ENTER
ENTERlogo=pygame.image.load('PRESS ENTER.gif').convert()
#TUTORIAL
imageTUT=pygame.image.load('GRADUATION.gif').convert()
imageTUT=pygame.transform.scale(imageTUT,(80,150))
#PLAY
imagePLAY=pygame.image.load('PLAY.gif').convert()
imagePLAY=pygame.transform.scale(imagePLAY,(200,150))
#LEADERBOARD
imageLEAD=pygame.image.load('NUMBER ONE.gif').convert()
imageLEAD=pygame.transform.scale(imageLEAD,(85,150))
#QUIT
imageQUIT=pygame.image.load('SAD.gif').convert()
imageQUIT=pygame.transform.scale(imageQUIT,(90,150))
#WALK 1
louisWalk=pygame.image.load('louisWALK.gif').convert()
louisWalk=pygame.transform.scale(louisWalk,(64,108))
#WALK 2
louisWalkAlt=pygame.image.load('louisWALKalt.gif').convert()
louisWalkAlt=pygame.transform.scale(louisWalkAlt,(64,108))
#STAND
louisStand=pygame.image.load('louisSTAND.gif').convert()
louisStand=pygame.transform.scale(louisStand,(64,108))
#PICKUP
louisPickup=pygame.image.load('louisPICKUP.gif').convert()
louisPickup=pygame.transform.scale(louisPickup,(64,108))
#FLOAT
louisFloat=pygame.image.load('louisFLOAT.gif').convert()
louisFloat=pygame.transform.scale(louisFloat,(64,108))
#CAUGHT
louisCaught=pygame.image.load('louisHURT.gif').convert()
louisCaught=pygame.transform.scale(louisCaught,(64,108))
#SHOOT
louisShoot=pygame.image.load('louisSHOOT.gif').convert()
louisShoot=pygame.transform.scale(louisShoot,(64,108))
#BRIEFCASE
briefcase=pygame.image.load('BRIEFCASE.gif').convert()
briefcase=pygame.transform.scale(briefcase,(64,108))
#WINNER
louisWinner=pygame.image.load('WINNER.gif').convert()
louisWinner=pygame.transform.scale(louisWinner,(64,152))
#MAPS
tutorialLevel=pygame.image.load('TUTORIAL.gif').convert()
mainLevel=pygame.image.load('MAIN.gif').convert()
#GUARD STAND
guardStand=pygame.image.load('guardSTAND.gif').convert()
guardStand=pygame.transform.scale(guardStand,(64,108))
#GUARD WALK 1
guardWalk=pygame.image.load('guardWALK.gif').convert()
guardWalk=pygame.transform.scale(guardWalk,(64,108))
#GUARD WALK 2
guardWalkAlt=pygame.image.load('guardWALKalt.gif').convert()
guardWalkAlt=pygame.transform.scale(guardWalkAlt,(64,108))
#GUARD SLEEP
guardSleep=pygame.image.load('guardASLEEP.gif').convert()
#STARThallway
STARThallway=pygame.transform.scale(pygame.image.load('STARThallway.gif').convert(),(1024,64))
#BRIEFCASE
briefcase=pygame.image.load('BRIEFCASE.GIF').convert()
briefcase=pygame.transform.scale(briefcase,(64,108))
#FILES
files=pygame.image.load('documents.gif').convert()
files=pygame.transform.scale(files,(32,46))
#DART
dart=pygame.image.load('dart(1).gif').convert()
dart=pygame.transform.scale(dart,(25,11))
#DART DISPLAY
dartDisplay=pygame.image.load('dart(1).gif').convert()
dartDisplay=pygame.transform.scale(dartDisplay,(34,14))
dartDisplay=pygame.transform.rotate(dartDisplay,90)
#CLIPBOARD LOSER
clipboardLoser=pygame.image.load('clipboardLoser.gif').convert()
#CLIPBOARD WINNER
clipboardWinner=pygame.image.load('clipboardWinner.gif').convert()
#SELECTION
circleSelection=pygame.image.load('selection.gif').convert()
#PHONE
phone=pygame.image.load('phone.gif').convert()

#Setting up common fonts and phrases that will be used in the game
courier=pygame.font.SysFont('Courier New',25)
comicSans=pygame.font.SysFont('Comic Sans MS',18)
courierSmall=pygame.font.SysFont('Courier New',15)
consolas=pygame.font.SysFont('Consolas',15)
leaderboardCourier=pygame.font.SysFont('Courier New',20)
segoe=pygame.font.SysFont('Segoe Print',30)
fromText=courierSmall.render('from',True,(0,0,0))
briefcaseText=courierSmall.render('briefcase',True,(0,0,0))
rToRestart=courierSmall.render('Hit r to Restart',True,(255,40,40))
sendIt=courier.render('SEND',True,(248,248,248))
BHF=courier.render('Borna Houmani-Farahani...',True,THECOLORS['black'])
PRE=courier.render('presents...',True,THECOLORS['black'])
NBLP=courier.render('a New Borleans Production...',True,THECOLORS['black'])

#Main function 
def Main():
    #sets up variables required for the startup sequence
    HIGHSCORES=highscoreCreator('leaderboard - a brief chase....txt')
    STARTUP=True
    MENU=False
    STARTUPcount=0
    count=0
    remember='RIGHT'
    getInfo=False
    clock = pygame.time.Clock()
    BHFx,BHFy=320,640
    PREx,PREy=430,640
    NBLPx,NBLPy=300,640
    LOUx,LOUy=0,5
    LOU2x,LOU2y=1024-32,640-5-54
    scrollup=.5
    LOGOx,LOGOy=247,640
    walkSpeedAnim=23
    louisStandTemp=pygame.transform.scale(louisStand,(32,54))
    louisWalkTemp=pygame.transform.scale(louisWalk,(32,54))
    louisWalkTempAlt=pygame.transform.scale(louisWalkAlt,(32,54))

    #game loop
    keepGoing = True                                            
    while keepGoing:
        #gets the dictionary of keys being pressed
        keys=pygame.key.get_pressed()
        
        #Sing event loop that works throughout the entire game
        for ev in pygame.event.get():
            if ev.type == QUIT:
                keepGoing = False
            #If they've pressed a key
            if ev.type == KEYDOWN:
                #If they are in the mode in which they enter their name for the leaderboard
                if getInfo:
                    #adds the key that they pressed to their name. (works for backspaces as well)
                    if ev.key==K_BACKSPACE: name=name[:-1]
                    elif len(name)<13 and ev.key!=K_RETURN: name+=ev.unicode
                #If they presseed space and are in the game portion of the game (tutorial or regular game)
                elif ev.key==K_SPACE and not STARTUP and not MENU:
                    #reverses gravity and gives them a jolt in the new direction
                    if gravity:
                        gravity=False
                        backy+=fallSpeedActual
                    else:
                        gravity=True
                        backy-=fallSpeedActual
                #If they press enter during the startup sequence
                elif ev.key==K_RETURN and STARTUP:
                    #Skips the startup cutscene by moving them directly onto the menu
                    STARTUP,MENU,showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT,walkSpeedAnim=False,True,False,False,False,False,8
                    screen.fill((255,255,255))
                    screen.blit(imageMENU,(0,0))
                #If they press x during the game
                elif ev.key==K_x and not STARTUP and not MENU:
                    #if they are not out of darts
                    if dartClip>0:
                        #Calculates the distance of the character from the background origine at the time of schooting
                        xDistance=480-backx
                        yDistance=266-backy
                        #Depending on the characters orientation, places the dart at the appropriate location
                        if gravity:
                            yChange=20
                            if remember=='RIGHT': movement,xChange=16,48
                            else: movement,xChange=-16,16
                        else:
                            yChange=76
                            if remember=='RIGHT': movement,xChange=16,48
                            else: movement,xChange=-16,16
                        #finally adds dart to the list of projectiles and subtracts 1 from the dart clip
                        projectileList.append([xChange,yChange,movement,xDistance,yDistance,])
                        dartClip-=1
                #if they press r during the gameplay portion of the game
                elif ev.key==K_r and not STARTUP and not MENU and not LOSE and not WIN:
                    #if they are on the tutorial level, reset all the variables to what they would be once you are spawned in
                    if setting==tutorialLevel:
                        TUTORIAL,MENU,WIN,LOSE=True,False,False,False
                        backx,backy=400,200
                        boundaries,setting,gravity=boundSetup('TUTORIAL'),tutorialLevel,True
                        guardInfo=guardSetup('TUTORIAL')
                        time=0
                        itemList=[(4833,235)]
                        projectileList=[]
                        dartClip=5
                        intel=0
                    #if they are on the main level, reset all the variables to what they would be once you are spawned in
                    else:
                        MENU,WIN,LOSE=False,False,False
                        backx,backy=360,96
                        boundaries,setting,gravity=boundSetup('MAIN'),mainLevel,True
                        guardInfo=guardSetup('MAIN')
                        time=0
                        itemList=[random.choice([(716,626),(1190,162),(1374,754),(1374,602),(1100,1090),(1670,922),(714,482),(600,756)])]
                        projectileList=[]
                        dartClip=5
                        intel=0

                        
                    
                        
        #startup sequence:
        if STARTUP:
            screen.fill((255,255,255))
            #scroll up with my name until it goes off the screen
            if STARTUPcount<=680:
                BHFy-=scrollup
                screen.blit(BHF,(320,BHFy))
            #scroll up with the 'presents' portion until it goes off screen
            elif STARTUPcount<=1360:
                PREy-=scrollup
                screen.blit(PRE,(420,PREy))
            #scroll up with the production name until it goes off screen
            elif STARTUPcount<=2040:
                NBLPy-=scrollup
                screen.blit(NBLP,(300,NBLPy))
            #scroll up with the game logo until it goes to the center of the screen
            elif STARTUPcount<=2283:
                LOGOy-=scrollup*2
                screen.blit(pygame.transform.scale(LOGO,(530,335)),(LOGOx,LOGOy))
            #stops scrolling for a second
            elif STARTUPcount<=2343:
                screen.blit(pygame.transform.scale(LOGO,(530,335)),(LOGOx,LOGOy))
            #flashes the characters and their loading bars
            elif STARTUPcount<=2373 or (STARTUPcount>2403 and STARTUPcount<=2433) or (STARTUPcount>2463 and STARTUPcount<=2493) or (STARTUPcount>2523 and STARTUPcount<=2600):
                screen.blit(pygame.transform.scale(LOGO,(530,335)),(LOGOx,LOGOy))
                screen.blit(STARThallway,(0,0))
                screen.blit(STARThallway,(0,576))
                screen.blit(louisStandTemp,(0,5))
                screen.blit(pygame.transform.flip(louisStandTemp,True,False),(1024-32,640-5-54))
            elif STARTUPcount<=2403 or (STARTUPcount>2433 and STARTUPcount<=2463) or (STARTUPcount>2493 and STARTUPcount<=2523):
                screen.blit(pygame.transform.scale(LOGO,(530,335)),(LOGOx,LOGOy))
            #once the flashing is over, the characters start running along the loading bars and they fill up behind them
            elif STARTUPcount<=3200:
                LOUx+=1
                LOU2x-=1
                screen.blit(pygame.transform.scale(LOGO,(530,335)),(centerTool((512,320),(530,335),False,False)))
                screen.blit(STARThallway,(0,0))
                screen.blit(STARThallway,(0,576))
                pygame.draw.rect(screen, (51,51,255), [0, 5, LOUx, 54])
                pygame.draw.rect(screen, (51,51,255), [LOU2x+32,640-5-54 , LOUx, 54])
                if count>=-walkSpeedAnim and count<0:
                    screen.blit(louisWalkTemp,(LOUx,LOUy))
                    screen.blit(pygame.transform.flip(louisWalkTemp,True,False),(LOU2x,LOU2y))
                elif count>=0 and count<=walkSpeedAnim+1:
                    screen.blit(louisWalkTempAlt,(LOUx,LOUy))
                    screen.blit(pygame.transform.flip(louisWalkTempAlt,True,False),(LOU2x,LOU2y))
                if count>walkSpeedAnim:
                    count=-walkSpeedAnim
                count+=1
            #once the loading bars are finished, displays the direction to press enter to continue
            elif STARTUPcount>3200:
                screen.blit(pygame.transform.scale(ENTERlogo,(530,335)),(centerTool((512,320),(530,335),False,False)))
                screen.blit(STARThallway,(0,0))
                screen.blit(STARThallway,(0,576))
                pygame.draw.rect(screen, (51,51,255), [0, 5, LOUx, 54])
                pygame.draw.rect(screen, (51,51,255), [LOU2x+32,640-5-54 , LOUx, 54])
            pygame.display.flip()
            STARTUPcount+=.5

            

        #Menu selection
        elif MENU:
            #gets the mouse info
            mouseX,mouseY=pygame.mouse.get_pos()
            mouseLeft,mouseMid,mouseRight=pygame.mouse.get_pressed()
            #if the mouse is hovering over the clipboard and it is clicked, draw a little circle at the mouse position
            if mouseX in range(575,970) and mouseY in range(125,590) and mouseLeft: pygame.draw.circle(screen,(0,0,0),(mouseX,mouseY),3)
            
            #If mouse is over the turorial button    
            if mouseX in range(73,233) and mouseY in range(257,395):
                #Set the variables to display the tutorial info and picture
                showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT=True,False,False,False
                #if mouse is clicked, change the variables to start up the game
                if mouseLeft:
                    MENU,WIN,LOSE=False,False,False
                    backx,backy=400,200
                    boundaries,setting,gravity=boundSetup('TUTORIAL'),tutorialLevel,True
                    guardInfo=guardSetup('TUTORIAL')
                    time=0
                    itemList=[(4833,235)]
                    projectileList=[]
                    dartClip=5
                    intel=0
                    getInfo=False
              
            #If the mouse is over the play option
            elif mouseX in range(290,465) and mouseY in range(263,379):
                #Set the variables to display the Play info and picture
                showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT=False,True,False,False
                #If the mouse is clicked
                if mouseLeft:
                    #Picks a bunch of text conversations randomly to be displayed in a little cutscene
                    #note: some of the phrases aren't real sentences or grammatically correct. This is on purpose
                    text1=consolas.render(random.choice(['We need your services.','Agent, we need you.',"You're needed.",'HELP','We need you Louis...Kenobi :^]']),True,(0,0,0))
                    text2=consolas.render(random.choice(["I'm listening...", 'WHAT?!' , 'As usual...' ,  'At your service.' , 'yeah?' , 'k... :^]','Louis here.','AGAIN?!']),True,(0,0,0))
                    text3=consolas.render(random.choice(["Here's your mission:" , "Here's your briefing:","This is what we need:","Here's the scoop:","Get this!:"]),True,(0,0,0))
                    text4=consolas.render(random.choice(['You need to get us a briefcase','Get us a briefcase ASAP',"Get us a briefcase STAT"]),True,(0,0,0))
                    text5=consolas.render(random.choice(['It holds top secret files!','It holds one billion pesos!','It holds $GOLD$ from Fort Knox!','It holds plans for a time machine!','It holds the cure to upsidedown disease!','It holds plans for the new iPhone!',"It holds nuke codes!","It holds a nifty lil' thing!","It holds another briefcase!","It holds my car keys!","It holds xbox for Christmas!","It holds airplane for christmas!","It holds...I'm not sure actually...","It's actually empty.","It holds the secret to the living Force.",'It holds about 20 bucks!','It holds the last albino black panther!','It holds quite a bit!',"It holds Walt Disney's head!",'t hlds ll m vwls!']),True,(0,0,0))
                    text6=consolas.render(random.choice(['I had a hunch...','I knew it!','I had a feeling...',"That's new!",'So predicatble.','So cookie-cutter','xD','Hmmm... :/','tfw...','omg!!!1!',"That's CRAY!","That's NASTY!","Kill 'em!"]),True,(0,0,0))
                    text7=consolas.render(random.choice(["You'll do it?",'Are you ready?','Get ready!','Roll out, Agent!','Move! Move! Move!',"Do you choose to accept the mission?!","You're our only hope!"]),True,(0,0,0))
                    text8=consolas.render(random.choice(["I'll do it!" , "I'm ready.","Let's go!","Copy that.","Affirmative.","Okey dokey!","Gotcha!","This won't self destruct now, right?",'Ugh! Fine!','k.','lol sure','kappa... :^]']),True,(0,0,0))
                    #blits the background of a phone
                    screen.blit(phone,(0,0))
                    #blits the first text after waiting 1 second
                    pygame.display.flip()
                    pygame.time.delay(500)
                    pygame.draw.rect(screen,(190,190,190),[390,110,260,25])
                    screen.blit(text1,(395,115))
                    #blits the second text after waiting 1 second
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[300,160,140,25])
                    screen.blit(text2,(305,165))
                    #and so on...
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[470,210,180,25])
                    screen.blit(text3,(475,215))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[400,260,250,25])
                    screen.blit(text4,(405,265))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[325,310,325,25])
                    screen.blit(text5,(330,315))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[300,360,155,25])
                    screen.blit(text6,(305,365))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[350,410,300,25])
                    screen.blit(text7,(355,415))
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    pygame.draw.rect(screen,(190,190,190),[300,460,310,25])
                    screen.blit(text8,(305,465))
                    pygame.display.flip()
                    pygame.time.delay(1000)

                    #once the texts are all over, the cutscene is done and the variables are set to send the player into the game
                    MENU,WIN,LOSE=False,False,False
                    backx,backy=360,96
                    boundaries,setting,gravity=boundSetup('MAIN'),mainLevel,True
                    guardInfo=guardSetup('MAIN')
                    time=0
                    itemList=[random.choice([(716,626),(1190,162),(1374,754),(1374,602),(1100,1090),(1670,922),(714,482),(600,756)])]
                    projectileList=[]
                    dartClip=5
                    intel=0
                    getInfo=False
       
                    
            #if the mouse is over the 'leaderboard option'
            elif mouseX in range(88,263) and mouseY in range(474,606):
                #Set the variables to display the leaderboard info and picture
                showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT=False,False,True,False
            elif mouseX in range(331,485) and mouseY in range(442,590):
                #Set the variables to display the quit info and picture
                showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT=False,False,False,True
                #if they click. end the game loop
                if mouseLeft: keepGoing=False

            #if the variables are set to show the tutorial info and picture, does so. also stops displaying the tutorial info every frame to allow for drawing on the clipboard
            if showTUTORIAL:
                screen.fill((255,255,255))
                screen.blit(imageMENU,(0,0))
                pygame.draw.rect(screen, (100,100,100), [610, 140, 320, 170],5)
                message=['Learn how to play the game in the tutorial!',"That's probably important, right?",'','','','Quick Controls:','-SPACE : reverse gravity','-ARROW KEYS : move, pickup items','-X : shoot a tranquilizer dart','','','Knowing is half the battle!']
                for line in range(len(message)):
                    screen.blit(comicSans.render(message[line],True,THECOLORS['black']),(585,320+22*line))
                screen.blit(imageTUT,(centerTool((772,10),(80,150),True,False),150))
                showTUTORIAL=False
            #if the variables are set to show the play info and picture, does so. also stops displaying the play info every frame to allow for drawing on the clipboard
            elif showPLAY:
                screen.fill((255,255,255))
                screen.blit(imageMENU,(0,0))
                pygame.draw.rect(screen, (100,100,100), [610, 140, 320, 170],5)
                message=['Play as Louis, a spy working for the BMF, the','Brief Missions Force. Try to infiltrate a','building and retreive top secret files held in','a briefcase. Use everything in your arsenal to','make your mission as brief as possible.']
                for line in range(len(message)):
                    screen.blit(comicSans.render(message[line],True,THECOLORS['black']),(585,320+22*line))
                screen.blit(imagePLAY,(centerTool((772,10),(200,150),True,False),140))
                showPLAY=False
            #if the variables are set to show the leaderboard info and picture, does so. also stops displaying the leaderboard info every frame to allow for drawing on the clipboard
            elif showLEADERBOARD:
                screen.fill((255,255,255))
                screen.blit(imageMENU,(0,0))
                pygame.draw.rect(screen, (100,100,100), [610, 140, 320, 170],5)
                message=['    SCORE'+' '*17+'NAME']
                for line in range(len(message)):
                    screen.blit(leaderboardCourier.render(message[line],True,THECOLORS['black']),(585,320+20*line))
                message=HIGHSCORES
                for line in range(len(message)):
                    if line<8:
                        screen.blit(leaderboardCourier.render(str(line+1)+')  '+message[line],True,THECOLORS['black']),(585,345+30*line))
                screen.blit(imageLEAD,(centerTool((772,10),(85,150),True,False),140))
                showLEADERBOARD=False
            #if the variables are set to show the quit info and picture, does so. also stops displaying the quit info every frame to allow for drawing on the clipboard
            elif showQUIT:
                screen.fill((255,255,255))
                screen.blit(imageMENU,(0,0))
                pygame.draw.rect(screen, (100,100,100), [610, 140, 320, 170],5)
                message=['You would leave the BMF?']
                for line in range(len(message)):
                    screen.blit(comicSans.render(message[line],True,THECOLORS['black']),(585,320+20*line))
                screen.blit(imageQUIT,(centerTool((772,10),(90,150),True,False),140))
                showQUIT=False
            
            pygame.display.flip()
            
            
        #Game option: If not in the startup or the menu, they must be playing the game
        else:
            #makes sure they haven't won or lost before allowing them to move
            if not WIN and not LOSE:
                #Adds to the time milliseconds at a time
                milli=clock.tick(30)
                if milli<100:time+=milli/1000
                #Resets the walk and fallspeeds
                walkSpeedActual,fallSpeedActual=8,8
                screen.fill((0,0,0))


                #MOVEMENT
                #If there is gravity
                if gravity:
                    #Goes through the list of boundaries
                    for bID in range(0,len(boundaries),2):
                        #If the user is touching a boundary, stops moving him down
                        if 480-backx in boundaries[bID] and 380-backy in boundaries[bID+1]:
                            fallSpeedActual=0
                            break
                    backy-=fallSpeedActual
                    #sets the animations appropriately (rightside up)
                    louisWalkTemp,louisWalkTempAlt,louisStandTemp,louisShootTemp=louisWalk,louisWalkAlt,louisStand,louisShoot
                #if there is anti-gravity
                else:
                    #goes through the list of boundaries
                    for bID in range(0,len(boundaries),2):
                        #If the user is touching a boundary, stops moving him up
                        if 480-backx in boundaries[bID] and 280-backy in boundaries[bID+1]:
                            fallSpeedActual=0
                            break
                    backy+=fallSpeedActual
                    #sets animations appropriately (upside down)
                    louisWalkTemp,louisWalkTempAlt,louisStandTemp,louisShootTemp=updownFlip(louisWalk),updownFlip(louisWalkAlt),updownFlip(louisStand),updownFlip(louisShoot)


                #If fallspeed is not 0 (they aren't falling) and they aren't shooting a dart
                if fallSpeedActual==0 and not keys[K_x]:
                    #If they are pressing the right key
                    if keys[K_RIGHT]:
                        #Flips the walking sprites to face right
                        louisWalkTemp,louisWalkTempAlt,louisShootTemp=rightFlip(louisWalkTemp),rightFlip(louisWalkTempAlt),rightFlip(louisShootTemp)
                        #if nothing is in their way, keep them moving, otherwise, stop them from moving that way
                        for bID in range(0,len(boundaries),2):
                            if 555-backx in boundaries[bID] and 266-backy in boundaries[bID+1]:
                                walkSpeedActual=0
                                break
                        backx-=walkSpeedActual
                        #Sets remember to right (the last way they were facing)
                        remember='RIGHT'
                    #If they are pressing the left key
                    elif keys[K_LEFT]:
                        #Flips the walking sprites to face left 
                        louisWalkTemp,louisWalkTempAlt,louisShootTemp=leftFlip(louisWalkTemp),leftFlip(louisWalkTempAlt),leftFlip(louisShootTemp)
                        #if nothing is in their way, keep them moving, otherwise, stop them from moving that way
                        for bID in range(0,len(boundaries),2):
                            if 470-backx in boundaries[bID] and 266-backy in boundaries[bID+1]:
                                walkSpeedActual=0
                                break
                        backx+=walkSpeedActual
                        #Sets remember to left (the last way they were facing)
                        remember='LEFT'
                #If they are floating 
                else:
                    #If there is gravity, changes their sprite to falling
                    if gravity:
                        louisStandTemp=louisFloat
                    #If there is anti-gravity, changes their sprite to falling but inverted
                    else:
                        louisStandTemp=updownFlip(louisFloat)

                
                #Blit the map at the new position
                screen.blit(setting,(backx,backy))

                #BLITTING THE GUARDS
                #For each guard
                for guard in range(len(guardInfo)):
                    #If the status of the guard is asleep, blits that version of them where they last were
                    if guardInfo[guard][5]==False: screen.blit(guardSleep,(backx+guardInfo[guard][0],guardInfo[guard][1]+backy))
                    #If they are still awake
                    else:
                        
                        xPos=backx+guardInfo[guard][0]
                        leftLim=guardInfo[guard][2]+backx
                        rightLim=guardInfo[guard][3]+backx
                        #moves each guard the direction they are going, if they meet a limit, multiply their direction by -1
                        if xPos<=leftLim or xPos>=rightLim: guardInfo[guard][4] *= -1
                        guardInfo[guard][0]+=guardInfo[guard][4]
                        #Depending on the direction they are facing, sets the animation appropriately and calculates their line of sight
                        if guardInfo[guard][4]<0:
                            guardWalkTemp=leftFlip(guardWalk)
                            guardWalkTempAlt=leftFlip(guardWalkAlt)
                            LOS=(range(xPos-184,xPos+32),range(guardInfo[guard][1]+backy,guardInfo[guard][1]+backy+108))
                        else:
                            LOS=(range(xPos+32,xPos+248),range(guardInfo[guard][1]+backy,guardInfo[guard][1]+backy+108))
                            guardWalkTemp=guardWalk
                            guardWalkTempAlt=guardWalkAlt
                        #A loop to determine which walking animation to blit. does each animation half the time
                        if count>=-walkSpeedAnim and count<0:
                            screen.blit(guardWalkTemp,(xPos,guardInfo[guard][1]+backy))
                        else:
                            screen.blit(guardWalkTempAlt,(xPos,guardInfo[guard][1]+backy))
                        #Goes throught the hitbox corners of the player and looks to see if they are within the line of sight
                        for hitboxCorner in [(480,266),(544,266),(480,374),(544,374)]:
                            if hitboxCorner[0] in LOS[0] and hitboxCorner[1] in LOS[1]:
                                #if they are, set LOSE to true and change the animation of the character to louisCaught
                                LOSE=True
                                louisWalkTemp,louisWalkTempAlt,louisStandTemp=louisCaught,louisCaught,louisCaught


                #BLITTING THE PROJECTILES
                #For dart in list of projectiles
                for dartI in range(len(projectileList)):
                    #goes through the boundaries, if the dart is going to hit the boundary next turn, set it to null
                    for bID in range(0,len(boundaries),2):
                        if projectileList[dartI][3]+projectileList[dartI][0]+projectileList[dartI][2] in boundaries[bID] and projectileList[dartI][4]+projectileList[dartI][1] in boundaries[bID+1]:
                                projectileList[dartI]=[0,0,0,0,0]
                                break
                    #Goes through list of guards to see if the dart hit one of them , if it did, sets the guards status to False (asleep)
                    for guard in range(len(guardInfo)):
                        xPos=backx+guardInfo[guard][0]
                        if backx+projectileList[dartI][3]+projectileList[dartI][0]+projectileList[dartI][2]+13 in range(xPos,xPos+65) and backy+projectileList[dartI][4]+projectileList[dartI][1]+5 in range(guardInfo[guard][1]+backy,guardInfo[guard][1]+backy+109) and guardInfo[guard][5]:
                            guardInfo[guard][5]=False
                            xAdd,yAdd=centerTool((42,56),(32,46),False,False)
                            itemList.append((guardInfo[guard][0]+xAdd+20,guardInfo[guard][1]+yAdd-20))
                            projectileList[dartI]=[0,0,0,0,0]
                            break
                    #If the projectile isn't null
                    if projectileList[dartI]!=[0,0,0,0,0]:
                        #blit it on the screen (change the lateral inversion based on the direction it's going)
                        if  projectileList[dartI][2]<0: screen.blit(leftFlip(dart),(backx+projectileList[dartI][3]+projectileList[dartI][0],backy+projectileList[dartI][4]+projectileList[dartI][1]))
                        else:screen.blit(dart,(backx+projectileList[dartI][3]+projectileList[dartI][0],backy+projectileList[dartI][4]+projectileList[dartI][1]))
                        projectileList[dartI][0]+=projectileList[dartI][2]
                    
                
                #BLITTING THE CHARACTER
                #If the animation count is less than 0, and the character is moving left and right
                if count>=-walkSpeedAnim and count<0 and (keys[K_RIGHT] or keys[K_LEFT]) and fallSpeedActual==0 and not keys[K_x]:
                    #blits the temporary walking animation half the time
                    screen.blit(louisWalkTemp,(480,266))
                #If the animation count is above 0 and the character is moving left or right
                elif count>=0 and count<=walkSpeedAnim+1 and (keys[K_RIGHT] or keys[K_LEFT])and fallSpeedActual==0 and not keys[K_x]:
                    #blits the alternate walking animation the other half
                    screen.blit(louisWalkTempAlt,(480,266))
                #If the character is crouching
                elif keys[K_DOWN] and gravity and not LOSE  and not keys[K_x] and fallSpeedActual==0:
                    #Blits the crouch animation
                    if remember=='LEFT': screen.blit(leftFlip(louisPickup),(480,266))
                    else: screen.blit((louisPickup),(480,266))
                    #Checks the item lists to find an item within a radius of 100 pixels from image
                    for item in range(len(itemList)):
                        #If any items are found, sets them null and does the affect of the item. If the item is the first in the list (i.e the objective briefcase), set WIN to true
                        if itemList[item]!=False and distanceOfLine((480,266),(itemList[item][0]+backx,itemList[item][1]+backy))<100 :
                            itemList[item]=False
                            intel+=1
                            if item==0: WIN=True
                #If the character is shooting a dart
                elif keys[K_x] and not LOSE:
                    #blit the dart animation
                    if remember=='LEFT': screen.blit(leftFlip(louisShootTemp),(480,266))
                    else: screen.blit(louisShootTemp,(480,266))
                #If the character is idle
                else:
                    #blit the standing animation
                    if remember=='LEFT': screen.blit(leftFlip(louisStandTemp),(480,266))
                    else: screen.blit(louisStandTemp,(480,266))
                

                #Purging lists of darts rendered useless
                while [0,0,0,0,0] in projectileList:
                    projectileList.remove([0,0,0,0,0])


                #ITEM
                #for each item, if the item isn't null, blit it at a constant location (relative to the background)
                for item in range(len(itemList)):
                    if item==0 and itemList[item]!=False:
                        screen.blit(briefcase,(itemList[item][0]+backx,itemList[item][1]+backy))
                    elif item>0 and itemList[item]!=False:
                        screen.blit(files,(itemList[item][0]+backx,itemList[item][1]+backy))
              
               
                #HUD ELEMENTS
                #Drawing the rectangles that the hud info will be inside
                pygame.draw.rect(screen,(255,255,255),[940,0,104,30])
                pygame.draw.rect(screen,(255,255,255),[0,0,150,70])
                #Displays the timestamp in the top left 
                timeStamp=courier.render(secondsTransfer(time),True,(0,0,0))
                screen.blit(timeStamp,(945,2))
                #Depending on the amount of intel the character has, displays the appropriate distance from the briefcase
                if not WIN: objectiveDistance=distanceOfLine((480,266),(itemList[0][0]+backx,itemList[0][1]+backy))
                if intel==0: distanceKnowledge=courier.render('???',True,(0,0,0))
                elif intel==1: distanceKnowledge=courier.render(str(int(round(objectiveDistance,-3))),True,(0,0,0))
                elif intel==2: distanceKnowledge=courier.render(str(int(round(objectiveDistance,-2))),True,(0,0,0))
                elif intel==3: distanceKnowledge=courier.render(str(int(round(objectiveDistance,-1))),True,(0,0,0))
                elif intel>3: distanceKnowledge=courier.render(str(int(round(objectiveDistance,0))),True,(0,0,0))                
                screen.blit(distanceKnowledge,(4,6))
                screen.blit(fromText,(68,2))
                screen.blit(briefcaseText,(68,18))
                #Depending on how many darts they have left, blits each one
                for clipLoad in range(dartClip): screen.blit(dartDisplay,(4+32*clipLoad,35))
                #If they are all out of darts, lets them know how to restart
                if dartClip==0: screen.blit(rToRestart,(4,40))
                #Flips the image
                pygame.display.flip()

                #ANIMATION COUNT
                #if the count is over the set switch rate, resets it so it is the negative of that switch rage
                if count>walkSpeedAnim:
                    count=-walkSpeedAnim
                #adds to the count
                count+=1

                #If the game is over, sets up a few variables for getting the players information after pausing for 1 second
                if LOSE or WIN:
                    pygame.time.delay(1000)
                    getInfo,name=False,''

                    
            #If the player just lost
            elif LOSE:
                #gets the mouse info
                mouseX,mouseY=pygame.mouse.get_pos()
                mouseLeft,mouseMid,mouseRight=pygame.mouse.get_pressed()
                #blits the clipboard over the last frame of gameplay
                screen.blit(clipboardLoser,centerTool((512,320),(367,520),False,False))
                pygame.draw.rect(screen, (100,100,100), [355, 165, 310, 125],5)
                screen.blit(louisCaught,(380,175))
                screen.blit(leftFlip(guardWalk),(580,175))
                #If the mouse is hovering over the 'redo' option
                if mouseX in range(358,492) and mouseY in range(466,554):
                    #display the pen circle around that option
                    screen.blit(circleSelection,(336,458))
                    #If the mouse is clicked, depending on the map, reset the variables to spawn everthing again
                    if setting==tutorialLevel and mouseLeft:
                        TUTORIAL,MENU,WIN,LOSE=True,False,False,False
                        backx,backy=400,200
                        boundaries,setting,gravity=boundSetup('TUTORIAL'),tutorialLevel,True
                        guardInfo=guardSetup('TUTORIAL')
                        time=0
                        itemList=[(4833,235)]
                        projectileList=[]
                        dartClip=5
                        intel=0
                    elif setting!=tutorialLevel and mouseLeft:
                        MENU,WIN,LOSE=False,False,False
                        backx,backy=360,96
                        boundaries,setting,gravity=boundSetup('MAIN'),mainLevel,True
                        guardInfo=guardSetup('MAIN')
                        time=0
                        itemList=[random.choice([(716,626),(1190,162),(1374,754),(1374,602),(1100,1090),(1670,922),(714,482),(600,756)])]
                        projectileList=[]
                        dartClip=5
                        intel=0
                #if the mouse is hovering over the menu option
                elif mouseX in range(532,666) and mouseY in range(466,554):
                    #display the pen circle around that option
                    screen.blit(circleSelection,(505,458))
                    #If they click the mouse, reset the variables back to the menu
                    if mouseLeft:
                        STARTUP,MENU,showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT,walkSpeedAnim=False,True,False,False,False,False,8
                        screen.fill((255,255,255))
                        screen.blit(imageMENU,(0,0))
                pygame.display.flip()
            #If they won
            elif WIN:
                backToMenu=False
                #get mouse info
                mouseX,mouseY=pygame.mouse.get_pos()
                mouseLeft,mouseMid,mouseRight=pygame.mouse.get_pressed()
                #blit the clipboard and the total score of the player
                screen.blit(clipboardWinner,centerTool((512,320),(367,520),False,False))
                pygame.draw.rect(screen,(100,100,100),[355, 165, 310, 162],5)
                screen.blit(louisWinner,(centerTool((512,320),(64,152),True,False),170))
                finalTime=segoe.render(secondsTransfer(time),True,(0,0,0))
                finalDart=segoe.render(str(5-dartClip),True,(0,0,0))
                finalTotal=segoe.render(secondsTransfer(time+(5-dartClip)*25),True,(0,0,0))
                screen.blit(finalTime,(358,320))
                screen.blit(finalDart,(358,355))
                screen.blit(finalTotal,(358,395))
                #If the mouse is over the leaderboard option
                if mouseX in range(358,492) and mouseY in range(466,554):
                    #blit the circle around that option
                    screen.blit(circleSelection,(336,458))
                    #If they click, set getInfo to True
                    if mouseLeft:
                        getInfo=True
                #If the mouse is over the menu option
                elif mouseX in range(532,666) and mouseY in range(466,554):
                    #Blits the circle
                    screen.blit(circleSelection,(505,458))
                    #set backtomenu to true
                    if mouseLeft: backToMenu=True
                #If they are in getInfo mode
                if getInfo:
                    #draw the box in which they will write their name
                    pygame.draw.rect(screen,(248,248,248),[380,260,205,50])
                    pygame.draw.rect(screen,(0,0,0),[370,260,205,50],5)
                    pygame.draw.rect(screen,(255,0,0),[575,260,75,50])
                    pygame.draw.rect(screen,(0,0,0),[575,260,75,50],5)
                    #blit the flashing cursor half the time
                    if count<0:
                        pygame.draw.rect(screen,(0,0,0),[375+len(name)*15,270,1,30])
                    #blit the name that they typed in
                    blitName=courier.render(name,True,(0,0,0))
                    screen.blit(blitName,(375,272))
                    screen.blit(sendIt,(582,272))
                    #If they click the send option, it writes the name and score to the file
                    if mouseX in range(580,651) and mouseY in range(265,310) and mouseLeft:
                        leaderboardWrite=open('leaderboard - a brief chase....txt','a')
                        leaderboardWrite.write('\n'+str(time+(5-dartClip)*25)+' '+name)
                        leaderboardWrite.close()
                        backToMenu=True
                #if they want to go back to the menu                    
                if backToMenu:
                    #set up the variables to send them back
                    STARTUP,MENU,showTUTORIAL,showPLAY,showLEADERBOARD,showQUIT,walkSpeedAnim=False,True,False,False,False,False,8
                    screen.fill((255,255,255))
                    screen.blit(imageMENU,(0,0))
                    #create an updated highscores list
                    HIGHSCORES=highscoreCreator('leaderboard - a brief chase....txt')        
                if count>walkSpeedAnim+60:
                        count=-walkSpeedAnim-60
                count+=1
                
                pygame.display.flip()

    #once game loop is finished, quit pygame               
    pygame.quit()  



# series of functions to quicken the process of flipping images
def leftFlip(image): return pygame.transform.flip(image,True,False)
def rightFlip(image): return pygame.transform.flip(image,False,False)
def updownFlip(image): return pygame.transform.flip(image,False,True)

#function that takes in coordinates and dimensions and returns the coordinates of the centered image in relation to the original coords
def centerTool(centerCoordsTuple,dimensionsTuple,xOnly,yOnly):
    xDim=centerCoordsTuple[0]-int(dimensionsTuple[0]/2)
    yDim=centerCoordsTuple[1]-int(dimensionsTuple[1]/2)
    if xOnly==False and yOnly==False:
        return (xDim,yDim)
    if xOnly:
        return xDim
    if yOnly:
        return yDim

#Function that takes an amount of seconds and returns it as a string in digital clock style time
def secondsTransfer(timeV):
    timeV=int(timeV)
    #calculates minutes and seconds
    minutes=timeV//60
    seconds=timeV%60
    #if those digits are only 1 character long i.e. 1:4, it adds 0s to make them look like: 01:04
    if len(str(minutes))==1:
        minutes='0'+str(minutes)
    if len(str(seconds))==1:
        seconds='0'+str(seconds)
    #returns the digital clock-like time as a string
    return str(minutes)+':'+str(seconds)

#Function that calculates the distance of a line using the pythagorean theorum
def distanceOfLine(point1,point2):
    deltaX=point1[0]-point2[0]
    deltaY=point1[1]-point2[1]
    pyth=(deltaX**2)+(deltaY**2)
    return pyth**.5

#Function that returns the list of boundaries depending on the name of the level that you input
def boundSetup(name):
    #each boundary list works through having an xrange and a yrange for each surface. 
    if name=='TUTORIAL':
                 #left wall                   #floor                            #roof                           #right wall                         #obstacle roof                      #obstacle right wall                #obstacle left wall          
        return [range(-24,-7),range(-10,+341),range(-64,+5121),range(+347,+356),range(-64,+5121),range(+8,+17),range(+5127,+5144),range(-10,+341),range(+1619,+1908),range(+193,+210),range(+1690,+1707),range(+186,+343),range(+1891,+1908),range(+186,+343)]
    elif name=='MAIN':
                #left wall                    #floor                               #roof                       #right wall                          #Hanging left wall 1          #Hanging right wall 1              #hanging wall bot 1                #start floor                           #cill wall                       #cill                               # underway roof                       #under way right                   #under way floor                      #hidden room roof                     #hidden pike roof                     #subway roof                           #compartment floors                 #hidden room left                  #hidden room cliff                    #hidden room right                 #compartment left wall             #right platform                       #right platform guard              #compartment roof                       #compartment pike left               #compartment pike right              #compartment pike bot                  #compartment platform                   #compartment platform bot           #compartment shelf top                   #compartment shelf bot               #compartment right                   #right shaft                          #cupboard roof                          #subway wall                           #subway cliff 
        return [range(-24,-7),range(-10,1200),range(-10,1788),range(1200-1,1200+8),range(-64,1790),range(7,24),range(1766+8,1783+8),range(-10,1200),range(1051,1068),range(0,100),range(1080-24,1080-7),range(0,100),range(1044-64,1080),range(108,116),range(205-64,820),range(268+8,268+17),range(196+8,196+25),range(271,434),range(122-64,196),range(430,430+8),range(123-64,781),range(457+8,457+17),range(780+8,780+25),range(450,730),range(354-64,788),range(585+8,585+17),range(354-64,790),range(607+8,607+17),range(204-60,260),range(585+8,585+17),range(204-60,1472),range(881+8,881+17),range(240,1453),range(859+8,859+17),range(266-25,266-8),range(589,876),range(694-60,788),range(726+8,726+16),range(695+8,695+25),range(734,864),range(826-25,827-8),range(270,872),range(963-59,1472),range(273-1,273+8),range(971-1,971+16),range(275,460),range(963-59,1457),range(477+16,477+25),range(1144-1,1144+16),range(480,570),range(1164-16,1164+1),range(480,570),range(1137-60,1165),range(600-8,600+1),range(1044-60,1264),range(704+8,704+17),range(1044-60,1264),range(738,738+8),range(1370-60,1460),range(704+8,704+17),range(1370-60,1460),range(738,738+8),range(1454-1,1454+16),range(472,872),range(1595+16,1595+33),range(-10,881),range(1601-60,1788),range(881+8,881+17),range(1164+8,1164+25),range(1030,1200),range(1166-60,1788),range(1030-1,1030+8)]
#Function that returns the list of guard informationfo each level
def guardSetup(name):
    #[startx,starty,leftlim,rightlim,speed,status]
    if name=='TUTORIAL': return [[2776,235,2656,2896,4,True],[3740,235,3532,3952,-4,True]]
    elif name=='MAIN': return [[528,162,308,700,4,True],[528,162,308,700,-4,True],[1189,162,964,1412,-4,True],[1189,162,964,1412,4,True],[556,481,420,575,-4,True],[458,754,414,575,4,True],[1100,754,918,1200,4,True],[1148,601,1044,1200,-4,True],[300,1090,30,500,4,True],[400,1090,300,800,-4,True],[798,1090,564,1111,-4,True],[798,1090,564,1111,4,True],[1406,922,1200,1666,4,True]]

#Function that calculates the highscore list (top 8) by reading a file
def highscoreCreator(filename):
    #reads the file and puts every line onto a list
    leaderboardInfo=open(filename,'r')
    linebyline=leaderboardInfo.readlines()
    scores=[]
    names=[]
    #Goes through the list to remove any empty lines (helps to bulletproof against people artifically changing the scores)
    while '' in linebyline:
        linebyline.remove('')
    #Goes through the list and seperates the scores fromt he names
    for line in linebyline:
        findSpace=line.index(' ')
        scores.append(float(line[:findSpace]))
        names.append(line[findSpace+1:].rstrip('\n'))
    leaderboardInfo.close()
    
    HIGHSCORES=[]
    #Takes the highest scores from each list and places them and their corresponding names in the Highscores list
    while [False]*len(scores) != scores:
        HIGHSCORES.append(secondsTransfer(max(scores))+'%21s'%names[scores.index(max(scores))])
        scores[scores.index(max(scores))]=False
    HIGHSCORES.reverse()
    return HIGHSCORES



Main()
