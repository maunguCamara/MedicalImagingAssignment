#Calculate and show the joint histogram of diifferent pairs 
of images. Visualize the outputs using log scale

import numpy as np
import matplotlib.pyplot as plt

# Assuming you have images I1, J1, I2, J2, etc. loaded as numpy arrays

def plot_joint_hist(I, J, bin, pair_name):
    # Calculate the joint histogram
    joint_hist = JointHist(I, J, bin)

    # Plot the joint histogram
    plt.figure(figsize=(8, 6))
    plt.imshow(np.log1p(joint_hist), cmap='hot', interpolation='nearest')
    plt.colorbar(label='Log Frequency')
    plt.title(f'Joint Histogram (Log Scale) of {pair_name}')
    plt.xlabel('I Intensity')
    plt.ylabel('J Intensity')
    plt.show()
