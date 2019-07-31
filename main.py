"""

			main gui file for login app 2.0
					31/7/2019


"""

#################### Imports ####################

from appJar import gui
app = gui('Login','500x300')

#################### FX ####################


#################### main Config ####################

app.setFont(15)
app.setLocation("CENTER")
app.setGuiPadding(20, 10)
app.setBg('#36454f')
app.setFg('#ededed')

#################### main GUI ####################

		########## start screen ##########

app.startFrame('start-page',0,0)
app.addLabel('start-label','Welcome to Login app 2.0')



app.stopFrame()







#################### GUI Config ####################










#################### END ####################
app.go()