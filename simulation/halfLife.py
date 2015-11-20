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

initialMass = int(input('Enter the initial mass of the element: '))

decayRate = int(input('Enter the half life of the element: '))

x = next_time(int(decayRate), 10)
y = next_mass(int(initialMass), 10)

print(x)
print(y)

plt.plot(x, y)
plt.show()

name = "Half Life"
width = 500
height = 500
rw.newDisplay(width, height, name)

def updateDisplay(state):
    dw.fill(dw.white)
    dw.drawCircle((0, 0, 255), (250, 250), state[2], 30)

def updateState(state):
    v = decayRate
    return((100,100, state[2]-v)) 

def endState(state):
    if (state[2] <= 30):
        return True
    else:
        return False

def handleEvent(state, event):  
    if (event.type == pg.MOUSEBUTTONDOWN):
        if (state[1]) == 1:
            newState = -1
        else:
            newState = 1
        return((state[0],newState,state[2]+state[3],state[3]))
    else:
        return(state)

initState = (100,100,initialMass)

frameRate = 20

rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)
