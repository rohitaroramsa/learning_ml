import numpy
import matplotlib.pyplot as plt


def uniform_data_distribution():
    x = numpy.random.uniform(0.0, 5.0, 100000)
    plt.hist(x, 100)
    plt.show()


def normal_data_distribution():
    y = numpy.random.normal(5.0, 1.0, 100000)
    #  an array where the values are concentrated around 5 with deviation of 1
    plt.hist(y, 100)
    plt.show()


if __name__ == '__main__':
    # uniform_data_distribution()
    normal_data_distribution()
