import sys
import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np
import grayscale




def nearest_neighbour(image,image_name,height , width ):
    image_width,image_height = image.shape[:2]
    width_scaling_factor = width/image_width
    height_scaling_factor = height/image_height

    new_image = np.zeros([width,height,3])
    image = grayscale.convert(image,image_name)
    #print("Width_Scaling_factor : ", width_scaling_factor , " Height Scaling Factor : ", height_scaling_factor)
    for i in range(width):
        for j in range(height):
            new_image[i][j] = image[int(i/width_scaling_factor),int(j/height_scaling_factor)]

    new_image_name = "Interpolated_" + image_name

    img.imsave(new_image_name,new_image)
    print("Your Interpolated image got stored with the name : ",new_image_name)
    plt.imshow(new_image)
    plt.show()








if __name__ == "__main__":
    image_name = input("Enter image name : ")
    image = img.imread(image_name)
    print("Size of Given Image (width,height): ", image.shape[:2])
    new_height = int(input("Enter new width : "))
    new_width = int(input("Enter new height : "))
    #print(image,image_name , new_height, new_width)
    nearest_neighbour(image,image_name,new_height,new_width)
