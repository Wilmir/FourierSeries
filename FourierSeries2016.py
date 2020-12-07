import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

def Even(k, b, L, t):
    result = 0
    if k<=0:
        return result
    return ((b/(k*np.pi))*(np.sin(k*np.pi/L) + np.sin(2*k*np.pi/L)) * np.cos(k*np.pi*t/L)) + Even(k - 1, b, L, t)

def evenExample(data):
    k = int(input("Enter the number of terms you want - odd number only: "))
    L = 3
    a0 = 2.0
    LL = -L
    UL = L
    b = 2
    step = 0.25
    size = int((np.absolute(LL)+np.absolute(UL))/step)+1
    print(size)

    x_data = []
    y_data = []

    text_file = open("Even_Fourier_Data.csv", "w")
    for i in range(size):
        x_data.append(LL)
        y_data.append(a0 / 2 + Even(k, b, L, LL))
        text_file.write("{0:0.5f} , {1:0.5f} \n".format(LL, Even(k, b, L, LL)))
        LL+=step
    text_file.close()

    print("Plotting Step Function")
    x, y = data
    """x = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
    y = [2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 12, 12]"""
    rcParams['axes.titlepad'] = 15
    plt.title(r"f(t) = %d+$\sum_{k=1}^\infty$$\frac{%d}{k\pi} \left( \sin\left(\frac{k\pi}{%d}\right) + \sin\left(\frac{2k\pi}{%d}\right) \right) \sin\left(\frac{k\pi}{%d}t\right) $ (k=%d)"%((a0/2),b,L,L,L,k))
    plt.plot(x, y, linewidth=3)
    plt.plot(x_data, y_data, linewidth=3)
    plt.grid(True)
    plt.savefig("Odd_Square_Wave.png")
    plt.show()


def generateData():
    # generate 1000 values for the x-axis
    xvalues = np.linspace(-3, 3, 25, endpoint = True)
    generatedDataFile = open('Even_Data.csv','w')

    # compute y for every x and store into the "Odd_Data.csv" file
    for x in xvalues:
        if (x >= 2.25):
            y = 0
        elif (x >= 1.75):
            y = -2*x + 4.5
        elif (x >= 1.25):
            y = 1
        elif (x >= 0.75):
            y = -2*x + 3.5
        elif (x >= -0.75):
            y = 2
        elif (x >= -1.25):
            y = 2*x + 3.5
        elif (x >= -1.75):
            y = 1
        elif (x >= -2.25):
            y = 2*x + 4.5
        else:
            y = 0
        generatedDataFile.write("{0:0.2f},{1}\n".format(x,y))
    generatedDataFile.close()

def loadData():
    x, y = np.genfromtxt('Even_Data.csv', unpack=True, delimiter=',')
    return (x, y)

def main():
    print("Fourier Series Plots")
    generateData()
    evenExample(loadData())


if __name__=="__main__":
    main()