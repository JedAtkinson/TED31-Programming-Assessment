#27/04/2020 Assesment-TrashGame_V2
#Jed Atkinson

#importing libaries
from appJar import gui
import random

#defining varibales
playerHealth = 100 
enemies = [["Plastic bottle", 100, 1, 10, True, "dolphin"], ["Plastic bag", 100, 10, 1, True, "turtle"], ["Plastic bag", 100, 7, 7, True, "puffin"]] #[name[0], health[1], posx[2], posy[3], Dead (bolean)[4]]
posx = 1 #player X position
posy = 1 #player Y position
ymax = 10 #Max Y size of map
xmax = 10 #Max X size of map
walls = [[1,6], [2,2], [2,3], [2,4], [3,2], [3,6], [4,2], [4,3], [4,4], [4,5], [4,6], [4,8], [4,9], [5,9], [6,9], [7,1], [7,2], [7,3], [8,9], [9,5], [9,6], [9,7], [9,8], [9,9], [10,9]] #coardiants for all the walls
btn = str(random.randint(1, 9)) #Button that starts as enemy
time = 6 #battle time
currentTime = 0 

#Class battle
class Game:
    def __init__(self, enemy): #initate all the varibles for battle
        self.enemyName = enemy[0]
        self.enemyHealth = enemy[1]
        self.enemyPosx = enemy[2]
        self.enemyPosy = enemy[3]
        self.good = enemy[5]
        
    def enterBattle(self): #screen before you enter battle
        app.removeAllWidgets()
        app.addLabel("enemyName", "You have run into a "+self.enemyName+" Terrorising Turtles")
        app.addLabel("Click on the "+self.enemyName+" to kill it if you hit a "+self.good+" you lose 10 health")
        app.addButton("fight", self.setBattle)
        
    def setBattle(self): #Inserts all the needed buttons/widgets for battle
        global playerHealth
        app.removeAllWidgets()
        app.hideAllSubWindows() #hides the map
        app.addLabel("enemyHealth", self.enemyName+" health: "+str(self.enemyHealth))
        app.addSplitMeter("enemyHealthMeter", 0,1)
        app.setMeterFill("enemyHealthMeter", ["red", "green"]) 
        app.addLabel("timer", "Time: "+str(time), 0,2)
        app.addImageButton("1", press, self.good+".gif", 1,0)
        app.addImageButton("2", press, self.good+".gif", 1,1)
        app.addImageButton("3", press, self.good+".gif", 1,2)
        app.addImageButton("4", press, self.good+".gif", 2,0)
        app.addImageButton("5", press, self.good+".gif", 2,1)
        app.addImageButton("6", press, self.good+".gif", 2,2)
        app.addImageButton("7", press, self.good+".gif", 3,0) 
        app.addImageButton("8", press, self.good+".gif", 3,1)
        app.addImageButton("9", press, self.good+".gif", 3,2)
        app.addLabel("health", "You're HP: "+str(playerHealth), 4,0)
        app.addSplitMeter("playerHealth", 4,1, 1,0)
        app.setMeterFill("playerHealth", ["green", "red"])   
        app.setMeter("playerHealth", playerHealth)
        global currentTime
        global btn
        currentTime = time
        app.after(1000, end) #starts timer
        btn = str(random.randint(1, 9)) #sets random enemy button
        app.setButtonImage(btn, self.enemyName+".gif")         
            

def setButtons(): #adds all the buttons for moving and labels for health/position
    app.showAllSubWindows()
    app.removeAllWidgets() #Removes everthing on GUI
    app.addLabel("pos", "Position: "+str(posx)+","+str(posy), 0,1)
    app.addLabel("health", "You're HP: "+str(playerHealth), 4,0)
    app.addSplitMeter("playerHealth", 4,1, 1,0)
    app.setMeterFill("playerHealth", ["green", "red"])
    app.setMeter("playerHealth", playerHealth)
    app.addButton("Go left", press, 2,0)
    app.addButton("Go right", press, 2,2)
    app.addButton("Go back", press, 3,1)
    app.addButton("Go foward", press, 1,1)
    start()    
   
def start(): #sets the widgets depending on position
    global time
    global mapPos
    app.setLabel(mapPos, " ")
    mapPos = int( str((posy-10)*-1) + str(posx))
    if mapPos > 99:
        mapPos = int( str((posy-10)*-1 +1) + str(0))
    app.setLabel(mapPos, "\u2B56")

    app.setLabel("pos", "Position: "+str(posx)+","+str(posy)) #prints position on GUI
    turnOptions = [] #Defines list for options to turn
    
    if posx == 3 and posy == 4 and time == 6:
        app.removeAllWidgets() #Removes everthing on GUI
        app.addLabel("pos", "Position: "+str(posx)+","+str(posy), 0,1)
        app.addLabel("health", "You're HP: "+str(playerHealth), 4,0)
        app.addSplitMeter("playerHealth", 4,1, 1,0)
        app.setMeterFill("playerHealth", ["green", "red"])
        app.setMeter("playerHealth", playerHealth)
        app.addButton("Go left", press, 2,0)
        app.addButton("Go right", press, 2,2)
        app.addButton("Go back", press, 3,1)
        app.addButton("Go foward", press, 1,1)
        
    if posx == 3 and posy == 3:
        app.addLabel("magic", "You ran into a magical turtle who grants you the power of time", 2,1)
        app.addLabel("E", "You now have 1 extra second in battle", 3,1)
        app.addImage("magicTurtle", "magicTurtle.gif", 4,1)
        time = 6  
    
    #checks position to asign turn options
    if posy != ymax:
        turnOptions.append("foward")        
    if posx != 1:
        turnOptions.append("left")
    if posx != xmax:
        turnOptions.append("right")
    if posy != 1:
        turnOptions.append("back")
        
    #checks if there is a wall blocking a direction
    for i in walls:
        if i[0]-1 == posx and i[1] == posy:
            turnOptions.remove("right")
        if i[0]+1 == posx and i[1] == posy:
            turnOptions.remove("left")
            
        if i[1]-1 == posy and i[0] == posx:
            turnOptions.remove("foward")
        if i[1]+1 == posy and i[0] == posx:
            turnOptions.remove("back")
        
    setup(turnOptions)
    
    # checks if enemy is dead before it enters battle
    global currentEnemy
    for enemy in enemies:
        if enemy[2] == posx and enemy[3] == posy:
            if enemy[4] == True:
                currentEnemy = enemy
                Game(enemy).enterBattle()

#Function to run when you die           
def die():
    app.removeAllWidgets()
    app.addLabel("You died fighting the "+currentEnemy[0])
    app.addButton("Exit", press)
                
#Function to update the timer in battle and cheack if you or the enemy has died          
def end():
    global currentTime
    global playerHealth
    global currentEnemy
    currentTime -= 1
    if currentTime < 0:
        app.removeAllWidgets()
        if currentEnemy[1] > 0:
            app.addLabel("You fail and lose 20 health")
            playerHealth -= 20
            if playerHealth <= 0:
                die()
            else:
                app.after(1000, setButtons)
        else:
            app.addLabel("you smash the "+currentEnemy[0])
            currentEnemy[4] = False
            i = 0
            for enemy in enemies:
                if enemy[4] == False:
                    i += 1
                if i == len(enemies):
                    app.removeAllWidgets()
                    app.addLabel("You defeted all the enemies and saved the wildlife")
                else:
                    app.after(1000, setButtons)
    else:
        app.setLabel("timer", "Time: "+str(currentTime))
        app.after(1000, end)

#sets the turn buttons and background image from the turnOptions
def setup(turnOptions):
    
    if "left" not in turnOptions:
        app.hideButton("Go left")
    else:
        app.showButton("Go left")
    if "right" not in turnOptions:
        app.hideButton("Go right")
    else:
        app.showButton("Go right")    
    if "back" not in turnOptions:
        app.hideButton("Go back")
    else:
        app.showButton("Go back")    
    if "foward" not in turnOptions:
        app.hideButton("Go foward")
    else:
        app.showButton("Go foward")    
        
    
    #uses the turnOptions to make the correct BG image file name  
    img = "" 
    for i in turnOptions:
        if i == "back":
            pass
        else:
            if i == turnOptions[0]:
                img = (i)
            else:
                img = (img+"-"+i)
    app.setBgImage(img+".gif")

#function that runs on button press
def press(button):
    global posx
    global posy
    if button == "start":
        app.showSubWindow("Map")
        setButtons()
        
    #changing player position
    if button == "Go left":
        posx -= 1
        start()
    if button == "Go right":
        posx += 1
        start()
    if button == "Go back":
        posy -= 1
        start()
    if button == "Go foward":
        posy += 1
        start()        
    
    global btn
    global currentEnemy
    global playerHealth
    if btn == button:
        app.setButtonImage(button, currentEnemy[5]+".gif")
        btn = str(random.randint(1, 9))
        app.setButtonImage(btn, currentEnemy[0]+".gif")
        
        currentEnemy[1] -= 10
        app.setMeter("enemyHealthMeter", currentEnemy[1])
        app.setLabel("enemyHealth", currentEnemy[0]+" health: "+str(currentEnemy[1]))
    elif button in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        playerHealth -= 10
        if playerHealth <= 0:
            die()
        else:
            app.setMeter("playerHealth", playerHealth)
            app.setLabel("health", "You're HP: "+str(playerHealth))
    
    if button == "Exit":
        app.stop()
    
#set up GUI
app = gui("Game", "1500x800")
app.setExpand("both")
app.setFont(20)
app.setBg("black")
app.setFg("white")
app.setImageLocation("images")
app.setFullscreen()

app.addLabel("Welcome")
app.addLabel("Navagate the your way through to find the animals in danger and save them")
app.addButton("start", press)

#Mini Map sub window
app.startSubWindow("Map")
app.setBg("black")
app.setFg("white")
app.setFont(20)
app.setStretch("both")
app.setSticky("nesw")
app.setSubWindowLocation("Map", 0, 0 )
app.setOnTop(stay=True)

for i in range(1, 11):
    app.addLabel(-110-i, i, 10,i)
    
for i in range(10):
    app.addLabel(110+i, (i-10)*-1, i,0)

a = 1
for e in range(10):
    for i in range(10):
        app.addLabel(a, " ", e,i+1)
        for wall in walls:
            if i == (wall[0]-1) and e == ((wall[1]-10)*-1) :
                app.setLabel(a, "\u2B1C")
                
        a += 1
        
app.setLabel(100, "?")
app.setLabel(1, "?")
app.setLabel(37, "?")
app.setLabel(73, "?")

a = (str((posy-10)*-1) + str(posx))
app.stopSubWindow()                                                                                    

mapPos = int( str((posy-10)*-1) + str(posx))
       
app.go() #Starts the GUI
