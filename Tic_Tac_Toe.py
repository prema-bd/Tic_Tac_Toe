
import turtle

# --- Setup Turtle ---
t = turtle.Turtle()
ws = turtle.Screen()
ws.title("Tic-Tac-Toe")
ws.bgcolor("black")
t.hideturtle()
t.speed("fastest")
t.pensize(5)

# --- Colors ---
board_color = "blue"
x_color = "cyan"
o_color = "magenta"
line_color = "red"
win_text_color = "yellow"

# --- Board setup ---
def drawBoard():
    t.color(board_color)
    t.pensize(5)
    
    # Vertical lines at x = -100, 100
    for x in [-100, 100]:
        t.penup()
        t.goto(x, 300)
        t.pendown()
        t.goto(x, -300)
    
    # Horizontal lines at y = -100, 100
    for y in [-100, 100]:
        t.penup()
        t.goto(-300, y)
        t.pendown()
        t.goto(300, y)
    
    t.penup()

drawBoard()

# --- Cell centers for larger cells (200x200) ---
startIndex = {
    1: (-200, 200), 2: (0, 200), 3: (200, 200),
    4: (-200, 0),  5: (0, 0),   6: (200, 0),
    7: (-200, -200), 8: (0, -200), 9: (200, -200)
}

# --- Game state ---
spots = []
xList = []
oList = []
gameOver = False

winCombo = [
    [1,2,3],[4,5,6],[7,8,9],
    [1,4,7],[2,5,8],[3,6,9],
    [1,5,9],[3,5,7]
]

# --- Draw X ---
def drawX(boxNum, color):
    t.color(color)
    x, y = startIndex[boxNum]
    size = 80  # bigger X
    t.penup()
    t.goto(x - size, y - size)
    t.pendown()
    t.goto(x + size, y + size)
    t.penup()
    t.goto(x - size, y + size)
    t.pendown()
    t.goto(x + size, y - size)
    t.penup()

# --- Draw O ---
def drawO(boxNum, color):
    t.color(color)
    x, y = startIndex[boxNum]
    radius = 80  # bigger O
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.circle(radius)
    t.penup()

# --- Draw winning line ---
def drawWinLine(combo, color):
    t.color(color)
    t.pensize(4)
    x1, y1 = startIndex[combo[0]]
    x2, y2 = startIndex[combo[2]]
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.goto(x2, y2)
    t.penup()
    t.pensize(5)

# --- Click detection ---
def getBox(x, y):
    for num, (bx, by) in startIndex.items():
        if bx - 100 < x < bx + 100 and by - 100 < y < by + 100:
            return num
    return 0

# --- Announce winner ---
def announceWin(text, color):
    t.penup()
    t.goto(0, -350)
    t.color(color)
    t.write(text, align="center", font=("Arial", 36, "bold"))

# --- Play function ---
def play(x, y):
    global gameOver
    if gameOver:
        return

    boxChosen = getBox(x, y)
    if boxChosen == 0 or boxChosen in spots:
        return

    spots.append(boxChosen)

    if len(spots) % 2 == 1:
        drawX(boxChosen, x_color)
        xList.append(boxChosen)
    else:
        drawO(boxChosen, o_color)
        oList.append(boxChosen)

    # Check for win
    for combo in winCombo:
        if all(pos in xList for pos in combo):
            drawWinLine(combo, line_color)
            announceWin("X WINS!", win_text_color)
            gameOver = True
            return
        elif all(pos in oList for pos in combo):
            drawWinLine(combo, line_color)
            announceWin("O WINS!", win_text_color)
            gameOver = True
            return

# --- Bind click ---
ws.onclick(play)

# --- Keep window open ---
ws.mainloop()
