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
    array_1D = np.array([1, 2, 3, 4], float)
    print array_1D
    array_2D = np.array([[1, 2, 3, 4],[5, 6, 7, 8]], float)
    print array_2D
    
    """ Arithmetics on 1D arrays """
    array_1D_1 = np.array([0, 1, 2], float)
    array_1D_2 = np.array([3, 4, 5], float)
    print array_1D_1 + array_1D_2
    print array_1D_1 - array_1D_2
    print array_1D_1 * array_1D_2
    
    """ Arithmetics on 2D arrays """
    array_2D_1 = np.array([[1, 2, 3], [4, 5, 6]], float)
    array_2D_2 = np.array([[4, 5, 6], [7, 8, 9]], float)
    print array_2D_1 + array_2D_2
    print array_2D_1 - array_2D_2
    print array_2D_1 * array_2D_2
    print array_2D_1 / array_2D_2
    
""" Example of dot product operations. """
def dot_product():
    array_1 = np.array( [0, 1, 2] , float)
    print array_1
    array_2 = np.array( [[1], [2], [3]] , float)
    print array_2
    print " Dot product: "
    print np.dot(array_1, array_2)

def test_run():
    """ Use this to verify or find out version and config details. """
    # version_config()

    """ Use this for practice on statistical analysis functions. """
    print " 1D array statistical operations: "
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    statistic_calculations(array)
    print ""
    
    print " 2D array statistical operations: "
    array_2D = np.array( [ [0, 1, 2], [3, 4, 5] ] , float )
    statistic_calculations(array_2D)
    print ""

    """ Use for array operations"""
    print " Array operations: "
    array_operations()

    """ Use for dot product practice """
    print " Dot Product operations: "
    dot_product()

if __name__ == '__main__':
    test_run()
