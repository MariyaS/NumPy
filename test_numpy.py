""" For practice on array operations and statistical analysis functions. """

import numpy as np

""" Use to verify or find out the version and configuration details. """
def version_config():
    print(np.__version__)
    np.__config__.show()

""" Example of a few statistical analysis functions. """
def statistic_calculations(array):
    print "Given array: "
    print array
    print "Mean: "
    print np.mean(array)
    print "Median: "
    print np.median(array)
    print "Standard Deviation: "
    print np.std(array)

""" Example of array operations. """
def array_operations():
    print "work in progress"
    
def test_run():
    """ Use this to verify or find out version and config details. """
    # version_config()

    """ Use this for practice on statistical analysis functions. """
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    statistic_calculations(array)

    """ Use for array operations"""
    array_operations()

if __name__ == '__main__':
    test_run()
