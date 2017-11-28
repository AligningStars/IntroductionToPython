"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Cheryl He.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
window.delay(5)
up = 270
half = 120
full = 165
down = 240
adjust = 30
Heart = rg.SimpleTurtle()

def heart(up,half,full,down):
    Heart.speed = 10
    Heart.pen = rg.Pen('red', 3)
    Heart.left(45)
    Heart.forward(up)
    Heart.left(75)
    Heart.forward(half)
    Heart.left(100)
    Heart.forward(full)
    Heart.right(75)
    Heart.forward(full)
    Heart.left(105)
    Heart.forward(half)
    Heart.left(65)
    Heart.forward(down)

for k in range (3):
    heart(up,half,full,down)
    Heart.pen_up()
    Heart.left(135)
    Heart.forward(adjust)
    Heart.pen_down()
    Heart.right(90)
    up = 0.7 * up
    half = 0.7 * half
    full = 0.7 * full
    down = 0.7 * down
    adjust = 0.7 * adjust











"""size = 200
Heart = rg.SimpleTurtle()
Heart.speed = 10
Heart.pen = rg.Pen('red', 3)
Heart.left(45)
Heart.forward(90)
Heart.left(75)
Heart.forward(40)
Heart.left(100)
Heart.forward(55)
Heart.right(75)
Heart.forward(55)
Heart.left(105)
Heart.forward(40)
Heart.left(65)
Heart.forward(83)
Heart.left(81)
for k in range(5):
    Heart.draw_regular_polygon(5,size)
    size = size - 20
    """
window.close_on_mouse_click()