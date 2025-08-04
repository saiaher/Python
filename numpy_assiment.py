import numpy as np

    
def vandermonde_matrix(v, N):
    return np.vander(v, N, increasing=True).T

s1=vandermonde_matrix([2, 3, 4,5], 2)
print(s1)


def average(arr, window_size):
    # Create a window of ones, normalize it by dividing by window size
    window = np.ones(window_size) / window_size
    # Use numpy's convolve function to compute the moving average
    return np.convolve(arr, window, mode='valid')


result = average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150], 3)
print(result)




