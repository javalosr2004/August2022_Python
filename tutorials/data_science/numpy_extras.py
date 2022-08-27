import numpy as np

a = np.zeros((3, 3)) #creates a 3 x 3 array matrix with zeros

a = np.ones((3, 3)) #creates a 3 x 3 array matrix with ones

a = np.full((3, 3), 'test') #creates a 3 x 3 array matrix with 'test'

a = np.full((5, 3, 3), 9) #creates a 5 arrays of 3 x 3

a = np.empty((5, 4, 2)) #creates uninitialized variables inside of the array, even though it appears that they have a value they really don't

print(a)