

# import cv2
# from google.colab.patches import cv2_imshow

# In[ ]:


#read and diplay image
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("tomandjerry.jpg",1)
cv2.imshow("display window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
#Type ur code here


# In[ ]:


#WRITE AN IMAGE
img1=cv2.imread("duck.jpeg",0)
cv2.imshow("display window",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('greyscale.jpeg',img1)
#Type ur code here

# Save the original image to a file
original_output_path = "image path"
#Type ur code here
cv2.imwrite(original_output_path, image)
print(f"Original image saved to: {original_output_path}")

# Read the saved image
#Type ur code here

# Display the saved image
#Type ur code here

# Save the saved image to a new file
#Type ur code here
cv2.imwrite(new_output_path, saved_image)
print(f"Saved image saved to: {new_output_path}")
#Shape of the Image
import cv2
img1=cv2.imread("tomandjerry.jpg",1)
print(img1.shape)

# In[ ]:


#ACCESSING ROWS AND COLUMNS
import random
import cv2
image=cv2.imread('duck.jpeg',1)
#image=cv2.resize(image,(400,400))
for i in range (150,200):
    for j in range(image.shape[1]):
        image[i][j]=[random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255)] 
cv2.imshow('part image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Type ur code here
# Get the shape of the image (rows, columns, channels)

print(f"Image Shape: Rows={rows}, Columns={columns}, Channels={channels}")

# Assign random values to pixels in the first row and first column
                                                                 # Random values for the first row
image[:, 0] = np.random.randint(0, 256, size=(rows, channels))  # Random values for the first column
#Type ur code here
# Display the modified image
#Type ur code here


# In[ ]:


#Cut and paste the image
import cv2
img2 = cv2.imread("duck.jpeg")
x = 0
y = 200
x1 = 160
y1 = 450
x2 = 0
y2 = 0
cropimg = img2[x:x1+x2, y:y1+y2]
cv2.imshow("Original Image", img2)
cv2.imshow("Cropped Image", cropimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Type ur code here
# Display the original image

#Type ur code here
# Get the shape of the image (rows, columns, channels)
#Type ur code here

# Define the region to cut (example: top-left corner, width=100, height=100)
cut_region = image[0:100, 0:100]

# Paste the cut region back onto the image (example: paste at (200, 200))
image[] = cut_region
#Display the modified image
#Type ur code here


# In[ ]:


#######COLOR CONVERSION
##Convert BGR and RGB to HSV and GRAY
#Type ur code here
# Convert BGR to RGB
image_rgb = (image_bgr, cv2.COLOR_BGR2RGB)

# Convert BGR to HSV
image_hsv_bgr = cv2.cvtColor(image_bgr, )

# Convert RGB to HSV BGR to Grayscale
import cv2
img = cv2.imread('duck.jpeg',1)
img = cv2.resize(img,(300,200))
cv2.imshow('Original Image',img)
hsv1 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv1)
hsv2 = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',hsv2)
gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray1)
gray2 = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert BGR to Grayscale
#Type ur code here

# Convert RGB to Grayscale
#Type ur code here

# Display the original BGR image
#Type ur code here
# Display the HSV image (BGR and RGB converted)
#Type ur code here
# Display the Grayscale image (BGR and RGB converted)
print("BGR TO GRAY")
cv2_imshow(image_gray_bgr)
print("RGB TO GRAY")
cv2_imshow(image_gray_rgb)


# In[ ]:


##Convert HSV to RGB and BGR
import cv2
img = cv2.imread('duck.jpeg')
img = cv2.resize(img,(300,200))
img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('Original HSV Image',img)
RGB = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
cv2.imshow('2HSV2BGR',RGB)
BGR = cv2.cvtColor(img,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV2RGB',BGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Type ur code here
# Convert BGR to HSV
#Type ur code here
# Convert HSV to RGB
#Type ur code here
# Convert HSV to BGR
image_bgr_hsv = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

# Display the original BGR image
#Type ur code here
cv2_imshow(image_bgr)

# Display the HSV image
#Type ur code here
cv2_imshow(image_hsv)

# Display the RGB image (HSV to RGB)
print("HSV TO RGB")
#Type ur code here

# Display the BGR image (HSV to BGR)

#Type ur code here


# In[ ]:


##Convert RGB and BGR to YCrCb
import cv2
img = cv2.imread('duck.jpeg')
img = cv2.resize(img,(300,200))
cv2.imshow('Original RGB Image',img)
YCrCb1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('RGB-2-YCrCb',YCrCb1)
YCrCb2 = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
cv2.imshow('BGR-2-YCrCb',YCrCb2)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Type ur code here

# Convert BGR to YCrCb
image_ycrcb_bgr = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YCrCb)

# Convert RGB to YCrCb
#Type ur code here
                                                                # Convert BGR to RGB
image_ycrcb_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)

# Display the original BGR image
#Type ur code here

# Display the YCrCb image (BGR to YCrCb)
#Type ur code here

# Display the YCrCb image (RGB to YCrCb)

#Type ur code here


# In[ ]:


#Split and Merge RGB Image
import cv2
img = cv2.imread('duck.jpeg',1)
img = cv2.resize(img,(300,200))
R = img[:,:,2]
G = img[:,:,1]
B = img[:,:,0]
cv2.imshow('R-Channel',R)
cv2.imshow('G-Channel',G)
cv2.imshow('B-Channel',B)
merged = cv2.merge((B,G,R))
cv2.imshow('Merged RGB image',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()


## Split the RGB channels
blue_channel, green_channel, red_channel = cv2.split(image_bgr)

# Display the original BGR image
#Type ur code here

# Display the individual RGB channels
print("BLUE CHANNEL")
cv2_imshow(blue_channel)
#Type ur code here

# Merge the RGB channels back together

#Type ur code here
# Display the merged image
#Type ur code here


# In[ ]:


##Split and merge HSV Image
import cv2
img = cv2.imread("duck.jpeg",1)
img = cv2.resize(img,(300,200))
img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
H,S,V=cv2.split(img)
cv2.imshow('Hue',H)
cv2.imshow('Saturation',S)
cv2.imshow('Value',V)
merged = cv2.merge((H,S,V))
cv2.imshow('Merged',merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Type ur code here
# Convert BGR to HSV
#Type ur code here

# Split the HSV channels
#Type ur code here
# Display the original BGR image and the converted HSV image
print("ORIGINAL IMAGE")
cv2_imshow(image_bgr)
print("HSV IMAGE")
cv2_imshow(image_hsv)

# Display the individual HSV channels
#Type ur code here


# In[ ]:




