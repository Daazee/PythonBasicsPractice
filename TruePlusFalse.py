# height is available as a regular list
height_in = [1,2,3,4,5,6,7]
# Import numpy
import numpy as np

# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254


# Print np_height_m
print(np_height_m)

#https://campus.datacamp.com/courses/intro-to-python-for-data-science/chapter-3-functions-and-packages?ex=9