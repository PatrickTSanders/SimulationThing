import matplotlib.pyplot as plt
import drawWorld as dw
import runWorld as rw
import pygame as pg


def next_time(half_rate, time_int):

    time = 0
    counter = 0

    time_array = []

    while(counter <= time_int-1):
        time_array.insert(counter, time)
        counter += 1
        time += half_rate
    return time_array


def next_mass(init_mass, time_int):

    mass_array = []

    i = 0

    while(i <= time_int-1):

        mass_array.insert(i, init_mass)
        init_mass = init_mass/2

        i += 1

    return mass_array


response = True


initialMass = int(input('Enter the initial mass of the element: '))
    #massType = raw_input('What unit of mass was given?: ')
decayRate = int(input('Enter the half life of the element: '))
    #timeType = raw_input('What unit of time was given?: ')

x = next_time(int(decayRate), 10)
y = next_mass(int(initialMass), 10)

print(x)
print(y)

plt.plot(x, y)
   # plt.ylabel(massType)
   # plt.xlabel(timeType)
# Initialize world

name = "Half Life"
width = 500
height = 500
rw.newDisplay(width, height, name)

################################################################
#

def updateDisplay(state):
    dw.fill(dw.white)
    dw.drawCircle((0, 0, 255), (250, 250), initialMass, 30)



################################################################

# Change pos by delta-pos, leaving delta-pos unchanged
# Note that pos is accessed as state[0], and delta-pos
# as state[1]. Later on we'll see how to access state
# components by name (as we saw with records in Idris).
#
# state -> state


def updateState(state):
    v = decayRate
    return((100,100, initialMass / v)) 

################################################################

# Terminate the simulation when the x coord reaches the screen edge,
# that is, when pos is less then zero or greater than the screen width
# state -> bool
def endState(state):
    if (state[2] <= 0):
        return True
    else:
        return False

################################################################

# We handle each event by printing (a serialized version of) it on the console
# and by then responding to the event. If the event is not a "mouse button down
# event" we ignore it by just returning the current state unchanged. Otherwise
# we return a new state, with pos the same as in the original state, but
# delta-pos reversed: if the cat was moving right, we update delta-pos so that
# it moves left, and vice versa. Each mouse down event changes the cat
# direction. The game is to keep the cat alive by not letting it run off the
# edge of the screen.
#
# state -> event -> state
#
def handleEvent(state, event):  
#    print("Handling event: " + str(event))
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[1]) == 1:
            newState = -1
        else:
            newState = 1
        return((state[0],newState,state[2]+state[3],state[3]))
    else:
        return(state)

################################################################

# World state will be single x coordinate at left edge of world

# The cat starts at the left, moving right 
initState = (100,100,200)

# Run the simulation no faster than 60 frames per second
frameRate = 3

# Run the simulation!
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
