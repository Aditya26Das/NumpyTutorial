import numpy as np
# Slicing - It means taking element from one given index to another.
# [start:end],[start:end:step]


# now we will slice an element from 1 to 5
a = np.array([45,36,27,9,8,12,54,36,69])
print(a[1:5])

# slicing from index 4 to end
b = np.array([45,36,27,9,8,12,54,36,69])
print(b[4:])

# slicing from beginning to end
c = np.array([45,36,27,9,8,12,54,36,69])
print(c[:])