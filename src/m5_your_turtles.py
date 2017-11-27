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
window.delay(10)
size = 200
Cheryl = rg.SimpleTurtle()
Cheryl.speed = 10
Cheryl.pen = rg.Pen('red', 3)
Cheryl.left(45)
Cheryl.forward(90)
Cheryl.left(75)
Cheryl.forward(40)
Cheryl.left(100)
Cheryl.forward(55)
Cheryl.right(75)
Cheryl.forward(55)
Cheryl.left(105)
Cheryl.forward(40)
Cheryl.left(65)
Cheryl.forward(83)
Cheryl.left(81)
for k in range(5):
    Cheryl.draw_regular_polygon(5,size)
    size = size - 20
window.close_on_mouse_click()