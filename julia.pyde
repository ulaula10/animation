def setup():
    size(1000,1000)
x=1 
dirkx=10

def draw():
    global x,dirx
#   scale(100)
#   rect(500,500, 100,100)
    ellipse(50,x, 100,100)
    x=x+1
    x= x+dirx
    
    if x>990:
        dirx= -10
        
