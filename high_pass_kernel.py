import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import grayscale as gray

def multiply(new_image,matrix,image,i,j,color):
    value = 0
    x_range = len(matrix)
    y_range = len(matrix[0])
    for x in range(3):
        for y in range(3):
            new_image[i][j][0] += matrix[x][y]*image[i+x][j+y][0]
            new_image[i][j][1] += matrix[x][y]*image[i+x][j+y][1]
            new_image[i][j][2] += matrix[x][y]*image[i+x][j+y][2]
    







def edge_detect(image_name,image):
    width,height = image.shape[:2]

    matrix = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    new_image = np.zeros([width-2,height-2,3])
    #print(new_image)

    grayimage = gray.convert(image,image_name)

    for i in range(width-2):
        for j in range(height-2):
            multiply(new_image,matrix,grayimage,i,j,0)

    plt.imshow(new_image)
    plt.show()






if __name__ == "__main__":
    print("\n\n This program is For detection of Edges using high pass Kernel \n\n")
    image_name = input("Enter the Image name : ")
    image = img.imread(image_name)
    edge_detect(image_name,image)