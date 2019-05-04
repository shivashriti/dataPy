# Open a file: file
file = open('moby_dick.txt', 'r')

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Read & print the first 3 lines
with open('moby_dick.txt') as file:
    print(file.readline())

############################################################################################################

## open files with numpy
import numpy as np

# Load file as array: digits (handwritten digits dataset)
digits = np.loadtxt('digits.csv', delimiter=',')  # type(digits) = <class 'numpy.ndarray'>
# Additional argument examples: 
# skiprows=1 (to skip header),
# usecols=[0,2] (for specifi columns)
# dtype = str (for text data)

# Select and reshape a row
im = digits[21, 1:]
print(im)
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()  # shows handwritten digit 6

# import data with mixed types:
np.recfromcsv(file)