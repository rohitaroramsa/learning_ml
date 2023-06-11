import numpy
import matplotlib.pyplot as plt


def plot_polynomial_regression():
    x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
    y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]
    my_model = numpy.poly1d(numpy.polyfit(x, y, 3))
    my_line = numpy.linspace(1, 22, 100)
    plt.scatter(x, y)
    plt.plot(my_line, my_model(my_line))
    plt.show()


if __name__ == '__main__':
    plot_polynomial_regression()
