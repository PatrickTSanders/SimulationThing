import matplotlib.pyplot as plt
import drawWorld as dw
import catFun as cf
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

while(response == True):
    initialMass = input('Enter the initial mass of the element: ')
    #massType = raw_input('What unit of mass was given?: ')
    decayRate = input('Enter the half life of the element: ')
    #timeType = raw_input('What unit of time was given?: ')

    x = next_time(int(decayRate), 10)
    y = next_mass(int(initialMass), 10)

    print(x)
    print(y)

    plt.plot(x, y)
   # plt.ylabel(massType)
   # plt.xlabel(timeType)
    plt.show()

    response = input('Would you like to try a different element (True/False):  ')

