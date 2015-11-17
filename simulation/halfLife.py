import matplotlib.pyplot as plt


def nextTime(doubleTime, timeInt):

    time = doubleTime
    t = 0

    timeArray = []

    while(t <= timeInt-1):
        timeArray.insert(t, time)
        t += 1
        time = time + doubleTime
    return(timeArray)


def nextMass(initMass, timeInt):

    massArray = []

    i = 0

    while(i <= timeInt-1):

        massArray.insert(i, initMass)
        initMass = initMass//2

        i += 1

    return(massArray)


x = nextTime(20, 6)
y = nextMass(500, 6)

print(x, y)

plt.plot(x, y)
plt.show()
