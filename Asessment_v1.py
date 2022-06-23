#importing libaries
from appJar import gui

#defining varibales
playerStats = [100]
enemies = [["Oil spill", 50], ["Plastic bag", 70], ["litter", 80]]
posx = 1
posy = 1

#Class
class Game:
    def __init__(self, playerHealth, enemyName, enemyHealth):
        self.playerHealth = playerHealth
        self.enemyName = enemyName
        self.enemyHealth = enemyHealth
    
    def start(self):
        app.removeAllWidgets()
        app.addLabel("Position: "+str(posx)+","+str(posy))
        if posx != 1:
            app.addButton("Turn left", press, 2,0)
        if posx != 6:
            app.addButton("Turn right", press, 2,2)
        if posy != 1:
            app.addButton("Go back", press, 3,1)
        if posy != 6:
            app.addButton("Go foward", press, 1,1)
            
    def battle(self):
        pass
    
    
def press(button):
    global posx
    global posy
    if button == "start":
        Game(playerStats[0], (enemies[0])[0], (enemies[0])[1]).start()
    if button == "Turn left":
        posx -= 1
        Game(playerStats[0], (enemies[0])[0], (enemies[0])[1]).start()
    if button == "Turn right":
        posx += 1
        Game(playerStats[0], (enemies[0])[0], (enemies[0])[1]).start()
    if button == "Go back":
        posy -= 1
        Game(playerStats[0], (enemies[0])[0], (enemies[0])[1]).start()
    if button == "Go foward":
        posy += 1
        Game(playerStats[0], (enemies[0])[0], (enemies[0])[1]).start()

#set up GUI
app = gui("Game", "1000x800")
app.setFont(20)

app.addLabel("Welcome")
app.addButton("start", press)

app.go() #Starts the GUI
