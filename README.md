Split and merge HSV Image

##### Program:
### Developed By:KABILAN T
### Register Number:212222230059




### i) Read and display the image
```
import cv2
import matplotlib.pyplot as plt
img=cv2.imread("tomandjerry.jpg",1)
cv2.imshow("display window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img.shape)
```

## output:
<img width="544" alt="Screenshot 2024-02-15 190636" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/f2e0b473-c41d-4158-b71b-a15352e70001">


### ii)Write the image
```
img1=cv2.imread("duck.jpeg",0)
cv2.imshow("display window",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('greyscale.jpeg',img1)
```
## output:
<img width="540" alt="Screenshot 2024-02-15 190857" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/d7c4adf8-c857-4157-a477-5c880142a2c8">



### iii)Shape of the Image
```
import cv2
img1=cv2.imread("tomandjerry.jpg",1)
print(img1.shape)
```
## output:
<img width="474" alt="Screenshot 2024-02-15 191844" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/91cef9c7-2c85-4398-930c-5b8400189773">



### iv)Access rows and columns
```
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
```

## output:
<img width="543" alt="Screenshot 2024-02-15 192022" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/2727909d-ea19-48fe-bb33-8a71e9b0ed0c">



### v)Cut and paste portion of image
```
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
```

## output:
<img width="545" alt="Screenshot 2024-02-15 192405" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/94e8a5bb-b265-49cd-90a9-6cecb435a323">


<img width="190" alt="Screenshot 2024-02-15 192338" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/ce18dc64-d586-49d7-8b37-bdf16652f721">



### vi) BGR and RGB to HSV and GRAY
```
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
```
## output:
<img width="901" alt="Screenshot 2024-02-15 192809" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/cf8e7c71-5fed-4844-9cae-9257a8a9eb98">
<img width="227" alt="Screenshot 2024-02-15 192835" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/942fb37a-81e8-499b-8e05-1b98ccf5b7f6">




### vii) HSV to RGB and BGR
```
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
```

## output:
<img width="679" alt="Screenshot 2024-02-15 193119" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/2bb47042-6de0-4a84-8f4e-c8573471881a">





### viii) RGB and BGR to YCrCb
```
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
```

## output:
<img width="680" alt="Screenshot 2024-02-15 193309" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/23a99d92-6759-45ce-bb9b-b8fd3014fd96">



### ix) Split and merge RGB Image
```
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
```

## output:
<img width="451" alt="Screenshot 2024-02-15 193641" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/5d3f30b7-bf0e-4e56-93a9-0b6f26eb1350">




### x) Split and merge HSV Image
```
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
```

## output:
<img width="440" alt="Screenshot 2024-02-15 193838" src="https://github.com/22009071/COLOR_CONVERSIONS_OF-IMAGE/assets/120206067/67a608ec-a790-41a5-9c1d-4375243062e2">


