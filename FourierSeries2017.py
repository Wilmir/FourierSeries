import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

def Odd(k, b, c, L, t):
    result = 0
    if k<=0:
        return result
    return ((b/(k*np.pi))
            * (((c/(k*np.pi))*np.cos(k*np.pi/L)) - (L*np.cos(k*np.pi)) - 1)
            * np.sin(k*np.pi*t/L)) + Odd(k-1, b, c, L, t)

def oddExample(data):
    k = int(input("Enter the number of terms you want - odd number only: "))
    L = 2
    a0 = 0.0
    LL = -L
    UL = L
    b = 4
    c = 3
    step = 0.01
    size = int((np.absolute(LL)+np.absolute(UL))/step)+1
    print(size)

    x_data = []
    y_data = []

    text_file = open("Odd_Fourier_Data.csv", "w")
    for i in range(size):
        x_data.append(LL)
        y_data.append(a0/2+Odd(k,b,c,L,LL))
        text_file.write("{0:0.5f} , {1:0.5f} \n".format(LL, Odd(k, b, c, L, LL)))
        LL+=step
    text_file.close()

    print("Plotting Step Function")
    x, y = data
    """x = [-5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5]
    y = [2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 12, 12]"""
    rcParams['axes.titlepad'] = 15
    plt.title(r"f(t) =  $\sum_{k=1}^\infty  $$\frac{%d}{k\pi} \left(\frac{%d}{k\pi} \sin\left(k\pi\right) - \left(%d\right) \cos\left({k\pi}\right) \right) \sin\left(\frac{k\pi}{%d}t\right) $ (k=%d)"%(b, c, L, L,k))
    # plt.plot(x, y, linewidth=3)
    plt.plot(x_data, y_data, linewidth=3)
    plt.grid(True)
    plt.savefig("Odd_Square_Wave.png")
    plt.show()


def generateData():
    # generate 1000 values for the x-axis
    xvalues = np.linspace(-2, 2, 17, endpoint=True)
    generatedDataFile = open('Odd_Data.csv','w')
    # compute y for every x and store into the "Odd_Data.csv" file
    for x in xvalues:
        if (x >= 1):
            y = -2
        elif (x >= -1):
            y = 0
        else:
            y = 2
        generatedDataFile.write("{0:0.2f},{1}\n".format(x,y))
    generatedDataFile.close()

def loadData():
    x, y = np.genfromtxt('Odd_Data.csv', unpack=True, delimiter=',')
    return (x, y)

def main():
    print("Fourier Series Plots")
    generateData()
    oddExample(loadData())


if __name__=="__main__":
    main()