import matplotlib.image as img
import numpy as np
import matplotlib.pyplot as plt




def resize(image_name,image,new_width,new_height):
    width,height= image.shape[:2]
    width_factor = width/new_width
    height_factor = height/new_height


    new_image = np.zeros([new_width,new_height,3])

    sum_red = 0
    sum_green = 0
    sum_blue = 0
    x_range = int(width_factor)
    y_range = int(height_factor)

    
    

    

    
    for i in range(1,new_width):
        for j in range(1,new_height):
            sum_red=0
            sum_green=0
            sum_blue=0
            for x in range((i-1)*x_range,i*x_range):
                for y in range((j-1)*y_range,j*y_range):
                    sum_red += image[x][y][0]
                    sum_green += image[x][y][1]
                    sum_blue += image[x][y][2]
                    #print("\n\n Enter in the changing loop \n\n")
            #print("Sum_Red : ",sum_red)
            #print("Sum_Green : ", sum_green)
            #print("Sum_Blue : ",sum_blue)
            #print()
            new_image[i][j][0] = int(sum_red/(x_range*y_range))/255
            new_image[i][j][1] = int(sum_green/(x_range*y_range))/255
            new_image[i][j][2] = int(sum_blue/(x_range*y_range))/255q

            #print("new_image[",i,"][",j,"][0] = ",new_image[i][j][0],end="\t")
            #print("new_image[",i,"][",j,"][1] = ",new_image[i][j][1],end="\t")
            #print("new_image[",i,"][",j,"][2] = ",new_image[i][j][2])


            
    plt.imshow(new_image)
    plt.show()





if __name__ == "__main__":
    print(":: This code is only for resizing new Image into smaller inputs ::\n\n")
    actual_name = input("Enter Image name : ")
    image = img.imread(actual_name)
    width,height = image.shape[:2]
    print("The Image u entered has (width,height) : ",width,height)
    new_width = int(input("Enter new width : "))
    while(new_width >width):
        print("You've entered the width larger than Image_Width")
        new_width = int(input("Enter new_width "))
    new_height = int(input("Enter new Height : "))
    while(new_height > height):
        print("You've entered the height larger than Image_height ")
        new_height = int(input("Enter new_height : "))
    resize(actual_name,image,new_width,new_height)