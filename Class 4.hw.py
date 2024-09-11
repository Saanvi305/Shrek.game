import pgzrun 
import random
WIDTH=700
HEIGHT=700
TITLE="Shooting Shrek"
message=""
shrek=Actor("shrek")
def draw():
    screen.clear()
    screen.fill("green")
    shrek.draw()
    screen.draw.text(message,center=(350,10))
            
def place_shrek():
   shrek.x=random.randint(50,WIDTH-100)
   shrek.y=random.randint(50,WIDTH-100)
   

def on_mouse_down(pos):
     global message 
     if shrek.collidepoint(pos):
       message="Good shot!"
       place_shrek()
     else:
       message="Try again!"





pgzrun.go()
