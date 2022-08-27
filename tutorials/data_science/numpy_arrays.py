import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a[0], b[1]) #works as a normal list

c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 , 9]

]) #can create a matrix array

print(c.shape) #shows how big this array is, 3 wide, 3 long

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]

print('\n\nAdding arrays\n\n')
print(x + y)
print(a + b) #adds a[0] with b[0], a[1] with b[1], etc

