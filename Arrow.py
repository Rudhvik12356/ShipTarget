import pgzrun, random, time

WIDTH = 900
HEIGHT = 1000
TITLE = "GALAGA"

direction = 1

crossbow = Actor("crossbow")
crossbow.pos = (WIDTH/2, HEIGHT-60)

enemies = [] 
for i in range(8):
    for j in range(3): 
        enemy = Actor("person")
        enemies.append(enemy)

        enemies[-1].x = 80 * i + 100
        enemies[-1].y = -20 + 50*j
enemiesPebble = []        

crossbow.dead = False
crossbow.countdown = 90
arrows = []

score = 0
speed = 5
game_over = False

def draw():
    screen.clear()
    screen.fill("black")
    
    crossbow.draw()
    for i in enemies: 
        i.draw()
    for i in arrows:
        i.draw()
    if len(enemies) == 0:
        win() 
        
    screen.draw.text("Score: " + str(score), (50, 50))
    screen.draw.text("Countdown: " + str(crossbow.countdown), (50, 70))
    
    for i in enemiesPebble:
        i.draw()
        i.y += 2
    if game_over:
        gameOver()
        return

def eArrows():
    for i in enemies:
        b = Actor("pebbles")
        x = i.x
        y = i.y
        b.pos = x,y
        enemiesPebble.append(b)  
           
clock.schedule_interval(eArrows, 10)       
      
def update():
    global score, speed, direction, enemies, game_over
    
    if game_over:
        return
     
    if keyboard.left:
        crossbow.x -= speed
        if crossbow.x < 50:
            crossbow.x = 50
         
    elif keyboard.right:
        crossbow.x += speed
        if crossbow.x > WIDTH-50:
            crossbow.x = WIDTH-50
            
    if len(enemies) > 0 and (enemies[0].x < 50 or enemies[-1].x > WIDTH - 50):
        direction = direction * (-1)
    
    for i in enemies:
        i.x += 2 * direction
        i.y += 2
        if i.y > HEIGHT:
            i.y = -100
        for j in arrows:
            if j.colliderect(i):
                score += 100
                enemies.remove(i)
                arrows.remove(j)
        if i.colliderect(crossbow):
            print("Collided")
            crossbow.dead = True
            game_over = True  

    if crossbow.dead:
        crossbow.countdown -= 1
    if crossbow.countdown == 0:
        crossbow.dead = False
        crossbow.countdown = 90
        
    for i in arrows:
        if i.y < 0:
            arrows.remove(i)
        else:
            i.y -= 5        

def on_key_down(key):
    if key == keys.SPACE:
        arrow = Actor("arrow")
        arrows.append(arrow)                  
        
        arrows[-1].x = crossbow.x
        arrows[-1].y = crossbow.y-50
        
def gameOver():
    screen.draw.text("Game Over!", (WIDTH/2-100, HEIGHT/2), fontsize=64, color="red")
    
def win():
    screen.draw.text("You win!", (WIDTH/2-100, HEIGHT/2), fontsize=64, color="green")

pgzrun.go()
