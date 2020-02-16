import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import grayscale as gray

def multiply(new_image,matrix,image,i,j):
    value = 0
    x_range = len(matrix)
    y_range = len(matrix[0])
    for x in range(3):
        for y in range(3):
            new_image[i][j][0] += matrix[x][y]*image[i+x][j+y][0]
            new_image[i][j][1] += matrix[x][y]*image[i+x][j+y][1]
            new_image[i][j][2] += matrix[x][y]*image[i+x][j+y][2]
    




def vertical(image_name,image):

    width,height = image.shape[:2]
    matrix = [[-1,2,-1],[0,0,0],[1,2,1]]

    new_image = np.zeros([width,height,3])

    gray_image = gray.convert(image,image_name)

    for i in range(width-2):
        for j in range(height-2):
            multiply(new_image,matrix,gray_image,i,j)

    plt.imshow(new_image)
    plt.show()





def horizontal(image_name,image):

    width,height = image.shape[:2]
    matrix = [[-1,0,1],[2,0,2],[1,0,1]]
    
    new_image = np.zeros([width,height,3])

    gray_image = gray.convert(image,image_name)

    for i in range(width-2):
        for j in range(height-2):
            multiply(new_image,matrix,gray_image,i,j)
    
    plt.imshow(new_image)
    plt.show()







if __name__ == "__main__":
    print("\n\nThis program is fully for applying sobel filtering \n\n")
    image_name = input("Enter Image Name : ")
    image = img.imread(image_name)
    horizontal(image_name,image)

