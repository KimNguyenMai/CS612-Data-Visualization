# In this programming exercise, you are expected to calculate the crossing time of a random walk. 
# The section 4.7 of the textbook has an illustrative example for this programming exercise.

# The section shows how to generate normally distributed steps with mean 0 and standard deviation of 0.25.

# In [272]: steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))

# Please make sure you meet the following requirements.

# Use the random seed of 1234 to generate the same random sequences.
# Generate normally distributed steps described above.
# Set the step +1 if the generated random number is nonnegative; otherwise -1.
# Use nwalks = 5000 and nsteps = 1000 to generate 5000 instances of 1000 random walks.
# Calculate the minimum crossing time to -50 (not 50), 
# which is the minimum time for a random walk to reach -50. (This is a slight deviation from the textbook example.)
# Your code needs to generate the following:

# Print the number of random walks that hit -50.
# Print the average minimum crossing time.
# Your code should have the following display:
# The number of random walks that hit -50: your answer for #1
# The average minimum crossing time: your answer for #2


import random
position = 0
walk = [position]