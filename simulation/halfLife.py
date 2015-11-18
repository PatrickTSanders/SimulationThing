import matplotlib.pyplot as plt


def nextTime(doubleTime, timeInt):

    time = 0
    t = 0

    timeArray = []

    while(t <= timeInt-1):
        timeArray.insert(t, time)
        t += 1
        time = time + doubleTime
    return timeArray


def nextMass(initMass, timeInt):

    massArray = []

    i = 0

    while(i <= timeInt-1):

        massArray.insert(i, initMass)
        initMass = initMass/2

        i += 1

    return massArray

response = True

while(response == True):
    initialMass = input('Enter the initial mass of the element: ')
    decayRate = input('Enter the half life of the element: ')

    x = nextTime(decayRate, 15)
    y = nextMass(initialMass, 15)

    print(x)
    print(y)

    plt.plot(x, y)
    plt.show()

    response = input('Would you like to try a different element (True/False):  ')



