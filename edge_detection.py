import matplotlib.image as img 
import matplotlib.pyplot as plt
import numpy as np 


def grayscale(image):
    grayscale_image =np.mean(image, axis=2)
    #grayscale_image/=255
    plt.imshow(grayscale_image,cmap='gray')
    plt.show()
    return grayscale_image


def edge_detect(image):
    gray_image=grayscale(image)
    edge_image1=gray_image.copy()
    main_filter=[[-3,0,3],[0,0,0],[3,0,-3]]
    for i in range(gray_image.shape[0]-2):
        for j in range(gray_image.shape[1]-2):
            edge_image1[i,j]=np.sum(gray_image[i:i+3,j:j+3]*main_filter)
    plt.imshow(edge_image1,cmap='gray')
    plt.show()

if __name__=='__main__':
    image = img.imread('gohan.jpg')
    plt.imshow(image)
    plt.show()
    edge_detect(image)
