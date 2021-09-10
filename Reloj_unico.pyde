x = 0

def setup() :
    size(300, 600)

def draw() :
    global x
    background(175)



    ellipse(150, x, 50, 50)
    fill(19, 28, 237)
    
    if x > height :
        x = 0
    else:
        x = map(minute(), 0, 59, 0, height)


    ellipse(50, x, 50, 50)
    fill(17, 242, 26)
    if x > height :
        x = 0
    else:
        x = map(second(), 0, 59, 0, height)


    ellipse(250, x, 50, 50)
    fill(242, 17, 36)
    if x > height :
        x = 0
    else:
        x = map(hour(), 0, 24, 0, height)
