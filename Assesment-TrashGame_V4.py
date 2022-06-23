#27/04/2020 Assesment-TrashGame_V2
#Jed Atkinson

#importing libaries
from appJar import gui
import random

#defining varibales
playerStats = [100] #[health]
enemies = [["Oil spill", 50, 1, 2], ["Plastic bag", 70, 5, 1], ["litter", 80, 7, 7]] #[name, health, posx, posy]
posx = 1 #player X position
posy = 1 #player Y position
ymax = 10
xmax = 10
walls = [[4,4], [4,5], [4,6], [4,7]]
btn = str(random.randint(1, 9))

#Class
class Game:
    def __init__(self, enemy):
        self.enemyName = enemy[0]
        self.enemyHealth = enemy[1]
        self.enemyPosx = enemy[2]
        self.enemyPosy = enemy[3]

    def enterBattle(self):
        app.removeAllWidgets()
        app.addLabel("enemyName", "You have run into a "+self.enemyName+" Terrorising Turtles")
        app.addButton("fight", self.setBattle)

    def setBattle(self):
        app.removeAllWidgets()
        app.addLabel("enemyHealth", self.enemyName+" health: "+str(self.enemyHealth))
        app.addImageButton("1", press, "turtle.gif", 1,0)
        app.addImageButton("2", press, "turtle.gif", 1,1)
        app.addImageButton("3", press, "turtle.gif", 1,2)
        app.addImageButton("4", press, "turtle.gif", 2,0)
        app.addImageButton("5", press, "turtle.gif", 2,1)
        app.addImageButton("6", press, "turtle.gif", 2,2)
        app.addImageButton("7", press, "turtle.gif", 3,0)
        app.addImageButton("8", press, "turtle.gif", 3,1)
        app.addImageButton("9", press, "turtle.gif", 3,2)
        btn = str(random.randint(1, 9))
        global btn
        app.setButtonImage(btn, "plastic bag.gif")         

    def battle(self):     
        print ("Hello")

#function for moving
def start():
    app.removeAllWidgets() #Removes everthing on GUI
    app.addLabel("pos", "Position: "+str(posx)+","+str(posy), 0,0) #prints position on GUI
    turnOptions = [] #Defines list for options to turn

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

    for enemy in enemies:
        if enemy[2] == posx and enemy[3] == posy:
            currentEnemy = enemy
            global currentEnemy
            Game(enemy).enterBattle()    


#sets the turn buttons and background image from the turnOptions
def setup(turnOptions):
    if "left" in turnOptions:
        app.addButton("Go left", press, 2,0)
    if "right" in turnOptions:
        app.addButton("Go right", press, 2,2)
    if "back" in turnOptions:
        app.addButton("Go back", press, 3,1)
    if "foward" in turnOptions:
        app.addButton("Go foward", press, 1,1)

    img = "" 
    for i in turnOptions:
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
        start()

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
    if btn == button:
        app.setButtonImage(button, "turtle.gif")
        btn = str(random.randint(1, 9))
        app.setButtonImage(btn, "plastic bag.gif")

        currentEnemy[1] -= 10
        app.setLabel("enemyHealth", currentEnemy[0]+" health: "+str(currentEnemy[1]))

#set up GUI
app = gui("Game", "1500x800")
app.setFont(20)
app.setImageLocation("images2")

app.addLabel("Welcome")
app.addButton("start", press)

app.go() #Starts the GUI
