import pgzrun, random, time, itertools 

WIDTH = 500
HEIGHT= 500

blockPositions = [(50, 50), (450, 50), (450, 450), (50, 450)]
bp = itertools.cycle(blockPositions)

ship = Actor("ship", center = (WIDTH/2, HEIGHT/2))
block = Actor("block", center = (50, 50))

def draw():
    screen.clear()
    
    ship.draw()
    block.draw()
    
def moveBlock():
    animate(block, "bounce_end", duration = 1, pos = next(bp))

moveBlock()
clock.schedule_interval(moveBlock, 2)

def shipTarget():
    x = random.randint(100, WIDTH - 100)
    y = random.randint(100, HEIGHT - 100)
    
    ship.target = x, y
    targetAngle = ship.angle_to(ship.target)
    targetAngle += 360*((ship.angle - targetAngle + 180)//360)
    animate(ship, angle = targetAngle, duration = 0.3, on_finished = moveShip)

def moveShip():
    animate(ship, tween = "accel_decel", pos = ship.target, duration = ship.distance_to(ship.target)/200, on_finished = shipTarget)
shipTarget()    
pgzrun.go()        