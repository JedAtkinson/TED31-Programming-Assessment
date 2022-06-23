#27/04/2020 Assesment-TrashGame_V2
#Jed Atkinson

#importing libaries
from appJar import gui
import random

#defining varibales
playerHealth = 100 
enemies = [["Plastic bottle", 100, 1, 10, True, "dolphin"], ["Plastic bag", 100, 10, 1, True, "turtle"], ["Plastic bag", 100, 7, 7, True, "puffin"]] #[name, health, posx, posy, Dead (bolean)]
posx = 1 #player X position
posy = 1 #player Y position
ymax = 10
xmax = 10
walls = [[1,6], [2,2], [2,3], [2,4], [3,2], [3,6], [4,2], [4,3], [4,4], [4,5], [4,6], [4,8], [4,9], [5,9], [6,9], [7,1], [7,2], [7,3], [8,9], [9,5], [9,6], [9,7], [9,8], [9,9], [10,9]]
btn = str(random.randint(1, 9))
time = 6
currentTime = 0

#Class
class Game:
    def __init__(self, enemy):
        self.enemyName = enemy[0]
        self.enemyHealth = enemy[1]
        self.enemyPosx = enemy[2]
        self.enemyPosy = enemy[3]
        self.good = enemy[5]
        
    def enterBattle(self):
        app.removeAllWidgets()
        app.addLabel("enemyName", "You have run into a "+self.enemyName+" Terrorising Turtles")
        app.addLabel("Click on the "+self.enemyName+" to kill it if you hit a "+self.good+" you lose 10 health")
        app.addButton("fight", self.setBattle)
        
    def setBattle(self):
        global playerHealth
        app.removeAllWidgets()
        app.hideAllSubWindows()
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
        app.after(1000, end)
        btn = str(random.randint(1, 9))
        app.setButtonImage(btn, self.enemyName+".gif")         
            

def setButtons():
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
   
#function for moving
def start():
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
        app.addImage("magicTurtle", "turtle.gif", 3,1)
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
    
    global currentEnemy
    for enemy in enemies:
        if enemy[2] == posx and enemy[3] == posy:
            if enemy[4] == True:
                currentEnemy = enemy
                Game(enemy).enterBattle()
                
            
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
                    app.addLabel("You won")
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
        
      
    img = "" 
    for i in turnOptions:
        if i == turnOptions[0]:
            img = (i)
        elif i == "back":
            pass
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
        app.setMeter("playerHealth", playerHealth)
        app.setLabel("health", "You're HP: "+str(playerHealth))

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
        
a = (str((posy-10)*-1) + str(posx))
app.stopSubWindow()                                                                                    

mapPos = int( str((posy-10)*-1) + str(posx))
       
app.go() #Starts the GUI
