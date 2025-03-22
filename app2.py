import numpy as np

test = np.array([0.3064677 , 0.6474286 , 0.2618227 , 0.58560052, 0.07489998,
       0.13525339,
                 
       0.71402409, 0.08298533, 0.52184038, 
       0.9500809 , 0.24574921, 0.40100861, 
                 
       0.21528933, 0.16712098, 0.55118471,
       0.82712615, 0.35169266, 0.92245681,
                 
       0.30681949, 0.35151636,0.68985098,
       0.17765172, 0.66437201, 0.71702622, 
                 
       0.32075419, 0.4200017 , 0.75570551, 
       0.46505716, 0.48177313, 0.32470815,
       
       0.39666765, 0.68322908, 0.29104496,
       0.84904557, 0.67176906, 0.97626922])

# Reshape the array into a 6x6 matrix
test_reshaped = test.reshape(6,6)

# Select elements from rows 0 to 3 (excluding 4) at index 2
test_reshaped[0:4, 2]

# Select all rows but only elements at index 3
test_reshaped[0:, 3]

# Iterate over each row and print
for x in test_reshaped:
  print(x)

# Iterate over each element and print
for y in test_reshaped.flat:
  print(y)

# Iterate with index and value pairs
for y in np.ndenumerate(test_reshaped):
  print(y)

# Horizontal stacking
a = ([1,2])
b = ([3,4])

np.hstack((a,b))  # Merge side by side

# Vertical stacking
np.vstack((a,b))  # Merge vertically

# Concatenation
c = ([1,2,3],[4,5,6])
d = ([7,8,9],[10,11,12])

np.concatenate((c,d),axis=0) # Merge vertically

np.concatenate((c,d),axis=1) # Merge horizontally
