#Verify sum oof all the elements in the joint histogram  is equal to the number of 
#pixels in the images
import numpy a np 

def verify_joint_hist(I, J, bin):
    #Ensure images are of the same size
    if I.shape != J.shape:
        raise ValueErro("Images must be of the same size")

    #Get the image dimensions
    n, p = I.shape


    #calculate joint histogram
    joint_hist = JointHist(I, J, bin)

    # Sum all the elements of the joint histogram
    
    sum_hist = np.sum(joint_hist)


    #Check if the sum equals the total number of pixels

    return sum_hist == n * p



