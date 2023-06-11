import numpy


def mean():
    x = numpy.mean(speed)
    print('Mean is: {}'.format(x))


def median_odd_list():
    median = numpy.median(speed)
    print('Median is: {}'.format(median))


def median_even_list():
    speed.append(89)  # to make it even length list
    median = numpy.median(speed)
    print('Median is: {}'.format(median))
    speed.pop()  # to revert the list


def standard_deviation():
    sd = numpy.std(speed)
    print('Standard Deviation is: {}'.format(sd))


def variance():
    variance_value = numpy.var(speed)
    print('Variance is: {}'.format(variance_value))


def percentile():
    percentile_at = 90
    percentile_value = numpy.percentile(speed, percentile_at)
    print('Percentile at {} is {}'.format(percentile_at, percentile_value))


if __name__ == '__main__':
    speed = [99, 86, 87, 88, 111, 86, 103, 91, 94, 78, 77, 85, 86]
    mean()
    median_odd_list()
    median_even_list()
    standard_deviation()
    variance()
    percentile()
