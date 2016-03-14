import numpy as np

def version_config():
    print(np.__version__)
    np.__config__.show()

def statistic_calculations(array):
    print "Given array: "
    print array
    print "Mean: "
    print np.mean(array)
    print "Median: "
    print np.median(array)
    print "Standard Deviation: "
    print np.std(array)


def test_run():
    """ Use this to verify or find out version and config details """
    # version_config()

    """ Use this for practice """
    array = [1, 2, 3, 4, 5]
    statistic_calculations(array)


if __name__ == '__main__':
    test_run()