# Python function to calculate joint histogram 
import numpy as np

def JointHist(I, J, bin):
    # Ensure that the images have the same size
    if I.shape != J.shape:
        raise ValueError("Images I and J must have the same size.")

    # Flatten the images into 1D arrays
    I_flat = I.flatten()
    J_flat = J.flatten()

    # Calculate the joint histogram
    joint_hist, _, _ = np.histogram2d(I_flat, J_flat, bins=bin, range=[[0, bin-1], [0, bin-1]])

    return joint_hist

# Example usage:
# Assuming I and J are numpy arrays representing images, and bin is the number of bins
# joint_hist = JointHist(I, J, bin)
