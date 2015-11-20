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

initialMass = int(input('Enter the initial mass of the element, between 100-450: '))

decayRate = int(input('Enter the half life of the element: '))

x = next_time(int(decayRate), 10)
y = next_mass(int(initialMass), 10)

print(x)
print(y)

plt.plot(x, y)
plt.show()

name = "Half Life,clicking the mouse will delay the decrease of an element by one tick. Would you let it die?"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

def updateDisplay(state):
    dw.fill(dw.white)
    dw.drawCircle((0, 0, 255), (500,500), state[2], state[2]-20)

v = decayRate/10+1

def updateState(state):
    return((500,500, int(state[2]/v))) 

def endState(state):
    if (state[2] <= 20):
        return True
    else:
        return False

def handleEvent(state, event):
    v = decayRate/10+1
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[2]) <= 300:
            newstate = int(state[2]*v)
        else:
            newstate = int(state[2]/v)
        return(500,500,newstate)
    else:
        return (state)
            
initState = (500,500,initialMass)

frameRate = 1

rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
