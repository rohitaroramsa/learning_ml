import numpy
from sklearn.metrics import r2_score


def calculate_r_squared():
    x = [1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22]
    y = [100, 90, 80, 60, 60, 55, 60, 65, 70, 70, 75, 76, 78, 79, 90, 99, 99, 100]
    my_model = numpy.poly1d(numpy.polyfit(x, y, 3))
    r_square = r2_score(y, my_model(x))
    print('Value of r-squared of current data is: {}'.format(r_square))


if __name__ == '__main__':
    calculate_r_squared()
