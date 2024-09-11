#Calculate the sum sqaured difference between two images I and J 
#betweeen two images of the same size

import numpy as np

def SSD(I, J):
    # Ensure that the images have the same size
    if I.shape != J.shape:
        raise ValueError("Images I and J must have the same size.")
    
    # Compute the sum of squared differences
    ssd = np.sum((I - J) ** 2)
    
    return ssd

# Example usage:
# Assuming I and J are numpy arrays representing images
# ssd_value = SSD(I, J)
# print("Sum of Squared Differences (SSD):", ssd_value)
