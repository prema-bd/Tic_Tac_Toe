import turtle

#1 - x:(-105,5) y:(50,150)
#4 - x:(-105,5) y:(-50,50)
#7 - x:(-105,5) y:(-150,-50)

#2 - x:(-5,95) y:(50,150)
#5 - x:(-5,95) y:(-50,50)
#8 - x:(-5,95) y:(-150,-50)

#3 - x:(95,195) y:(50,150)
#6 - x:(95,195) y:(-50,50)
#9 - x:(95,195) y:(-150,-50)


startIndex = {
  1:(-90,135),
  2:(10,135),
  3:(110,135),
  4:(-90,35),
  5:(10,35),
  6:(110,35),
  7:(-90,-65),
  8:(10,-65),
  9:(110,-65)
}

def drawBoard(turtle, size):
  
  turtle.rt(-90)
  turtle.fd(size)
  turtle.pu()
  turtle.rt(90)
  turtle.fd(size/3)
  turtle.pd()
  turtle.rt(90)
  turtle.fd(size)
  turtle.pu()
  turtle.rt(-90)
  turtle.fd(size/3)
  turtle.rt(-90)
  turtle.fd(size/3)
  turtle.rt(-90)
  turtle.pd()
  turtle.fd(size)
  turtle.pu()
  turtle.rt(90)
  turtle.fd(size/3)
  turtle.rt(90)
  turtle.pd()
  turtle.fd(size)
  turtle.pu()
  
  
def printcord(x,y):
  print(x,y)
  
  
def printSquare(x,y):
  if -105 < x < -5:
    if 50 < y < 150:
      print(1)
    elif -50 < y < 50:
      print(4)
    elif -150 < y < -50:
      print(7)
  elif -5 < x < 95:
    if 50 < y < 150:
      print(2)
    elif -50 < y < 50:
      print(5)
    elif -150 < y < -50:
      print(8)
  elif 95 < x < 195:
    if 50 < y < 150:
      print(3)
    elif -50 < y < 50:
      print(6)
    elif -150 < y < -50:
      print(9)
      
      
# def getSquare(x,y):
#   global boxChosen
  
#   if -105 < x < -5:
#     if 50 < y < 150:
#       boxChosen.append(1)
#     elif -50 < y < 50:
#       boxChosen.append(4)
#     elif -150 < y < -50:
#       boxChosen.append(7)
#   elif -5 < x < 95:
#     if 50 < y < 150:
#       boxChosen.append(2)
#     elif -50 < y < 50:
#       boxChosen.append(5)
#     elif -150 < y < -50:
#       boxChosen.append(8)
#   elif 95 < x < 195:
#     if 50 < y < 150:
#       boxChosen.append(3)
#     elif -50 < y < 50:
#       boxChosen.append(6)
#     elif -150 < y < -50:
#       boxChosen.append(9)
      
# def boxChose():
#   return boxChosen
      
      
def drawX(t,boxNum):
  x,y = startIndex[boxNum]
  
  t.pu()
  t.goto(x,y)
  t.seth(0)
  t.right(45)
  t.pd()
  t.forward(98.9)
  t.seth(90)
  t.pu()
  t.forward(70)
  t.left(135)
  t.pd()
  t.forward(98.9)
  
  
def drawO(t,boxNum):
  x,y = startIndex[boxNum]
  
  t.pu()
  t.goto(x,y)
  t.seth(270)
  t.fd(70)
  t.left(90)
  t.fd(35)
  t.pd()
  t.circle(35)
  
  
def drawLine(t, winComboVar):
  
  t.color("red")
  t.pensize(2.5)
  
  if winComboVar == [1,2,3]:
    t.pu()
    t.goto(-90,100)
    t.seth(0)
    t.pd()
    t.goto(175,100)
    t.pu()
  elif winComboVar == [4,5,6]:
    t.pu()
    t.goto(-90,0)
    t.seth(0)
    t.pd()
    t.goto(175,0)
    t.pu()
  elif winComboVar == [7,8,9]:
    t.pu()
    t.goto(-90,-100)
    t.seth(0)
    t.pd()
    t.goto(175,-100)
    t.pu()
  elif winComboVar == [1,4,7]:
    t.pu()
    t.goto(-55,135)
    t.seth(270)
    t.pd()
    t.goto(-55,-135)
    t.pu()
  elif winComboVar == [2,5,8]:
    t.pu()
    t.goto(45,135)
    t.seth(0)
    t.pd()
    t.goto(45,-135)
    t.pu()
  elif winComboVar == [3,6,9]:
    t.pu()
    t.goto(145,135)
    t.seth(0)
    t.pd()
    t.goto(145,-135)
    t.pu()
  elif winComboVar == [1,5,9]:
    t.pu()
    t.goto(-90,135)
    t.seth(0)
    t.pd()
    t.goto(180,-135)
    t.pu()
  elif winComboVar == [3,5,7]:
    t.pu()
    t.goto(180,135)
    t.seth(0)
    t.pd()
    t.goto(-90,-135)
    t.pu()
  else:
    print("???")

  
  
  