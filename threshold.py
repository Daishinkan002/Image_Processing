import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np


def grayscale(image):
    grayscale_image = np.mean(image,axis=2)
    plt.imshow(grayscale_image,cmap='gray')
    plt.show()
    return grayscale_image



def thresholding(image):
    gray_image = grayscale(image)
    thresholded_image = gray_image.copy()
    for i in range(gray_image.shape[0]):
        for j in range(gray_image.shape[1]):
            if gray_image[i][j]>150:
                thresholded_image[i][j]=255
            else:
                thresholded_image[i][j]=0

    plt.imshow(thresholded_image,cmap='gray')
    plt.show()

if __name__ == "__main__":
    image = img.imread('gohan.jpg')
    plt.imshow(image)
    plt.show()
    thresholding(image)