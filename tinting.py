import matplotlib.image as img
import numpy as np
import matplotlib.pyplot as plt


def tint_1_color(image,color,tint_value):
    im=image.copy()
    if color==1:
        color_name = "Red"
    elif color==0:
        color_name="Blue"
    elif color==2:
        color_name="Green"
    else:
        raise Exception("\n\nGive valid color id\n\n")
    print("\n\nYour ",color_name," tinted Images are processing...\n\n")
    for i in range(n):
        im[:,:,color]+=tint_value
        print("Your ",i+1," image is processed")
        plt.imshow(im)
        plt.show()


def tint_2_color(image,color1,color2,tint_value):
    im=image.copy()
    if(color1==0 and color2==1) or (color1==1 and color2==0) :
        color_name = "Purple"
    elif(color1==1 and color2==2) or (color1==2 and color1==1):
        color_name="Yellow"
    elif(color1==0 and color2==2) or (color1==2 and color1==0):
        color_name="Cyan"
    else:
        raise Exception("\n\nGive valid color id\n\n")
    print("\n\nYour ",color_name," tinted Images are processing...\n\n")
    for i in range(n):
        im[:,:,color1]+=tint_value
        im[:,:,color2]+=tint_value
        print("Your ",i+1," image is processed")
        plt.imshow(im)
        plt.show()


if __name__==    "__main__":
    image_name = input("Enter Image Name : ")
    im = img.imread(image_name)
    plt.imshow(im)
    plt.show()
    green_im=im.copy()
    print(type(im))
    print("Shape = ",im.shape)
    try:
        im.setflags(write=1)
    except Exception as e:
        print(e)
    #raise Exception("Download numpy 1.15.4")
    diff=5
    n=17
    while(True):
        choice=int(input("Choose a tint : \n1.Red\n2.Blue\n3.Green\n4.Yellow\n5.Purple\n6.Cyan\n7.All\n8.Exit\n Enter choice : "))
        if choice==1:
            tint_1_color(im,1,5)
        elif choice==2:
            tint_1_color(im,0,5)
        elif choice==3:
            tint_1_color(im,2,5)
        elif choice==4:
            tint_2_color(im,1,2,5)
        elif choice==5:
            tint_2_color(im,0,1,5)
        elif choice==6:
            tint_2_color(im,0,2,5)
        elif choice==7:
            tint_1_color(im,1,5)
            tint_1_color(im,0,5)
            tint_1_color(im,2,5)
            tint_2_color(im,1,2,5)
            tint_2_color(im,0,1,5)
            tint_2_color(im,0,2,5)
        elif choice==8:
            break
        else:
            print("Enter valid choice")

    plt.figure(1)
    plt.imshow(im)
    plt.figure(2)
    plt.imshow(im)
    plt.show()

    
    print("\n\nDone\n\n")