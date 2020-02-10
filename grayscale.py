import matplotlib.image as mat
import numpy as np
import matplotlib.pyplot as plt

#Here image is a n*3 array
def grayscale(image,image_name):
    avg = 0
    width,height = image.shape[:2]
    new_image = np.zeros([width,height,3])
    

    for i in range(width):
        for j in range(height):
            
            sum = float(image[i][j][0]) + float(image[i][j][1]) + float(image[i][j][2])
            avg = (sum/3)/256

            new_image[i][j][0] = avg
            new_image[i][j][1] = avg
            new_image[i][j][2] = avg
            
    
    gray_image_name = "Gray_" + image_name
    mat.imsave(gray_image_name,new_image)
    plt.imshow(new_image)
    plt.show()
    print("Your Image stored in the following folder with the name : " , gray_image_name)
    return new_image

if __name__ == "__main__":
    actual_image = input("Enter Image Name : ")
    image = mat.imread(actual_image)
    grayscale(image,actual_image)
