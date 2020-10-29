# Image Editor and Manager

The Image Editor and Manager aims to deliver fundamental image processing tools using graphical user interface. OpenCV and Numpy was used to implement the image processing operations while graphical user interface was created using PyQt5. Below are the demonstration gifs to show how to use the program. Result images are also included.

The image editor can do the following:

### Pyramid blending
Pyramid blending as described in **A Multiresolution Spline With Application to Image Mosaics** by Burt and Adelson was implemented.

![Pyramid Blending](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/pyramid_blending.gif)

Blended Image Ouput

Apple Image             |  Orange Image
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Pyramid%20Blending/burt_apple.png)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Pyramid%20Blending/burt_orange.png)
**Mask**             |  **Blended Image**
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Pyramid%20Blending/burt_matte.png)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Pyramid%20Blending/blended_image.png)







### Cartoonification
The toonification algorithm as described in **Toonify: Cartoon Photo Effect Application** by Dade was implemented.
![Cartoonification](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/cartoonification.gif)

**Toonification output**

Original             |  Output
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/cars.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Cartoonification/cartoon.jpg)

### Noise Addition
Three different noise patterns can be added to the images. 
![Noise](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/noise.gif)

Original Image             |  Gaussian Noise
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/water.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Noise/gaussian_noise_color.jpg)
**Vertical Noise bands**             |  **Horizontal Noise bands**
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Noise/vertical%20bands.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Noise/horizontal%20bands.jpg)


### Swap color channels
![Swap Color Channels](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/swapcolorchannels.gif)

Original Image             |  Blue and Red swapped
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/mountain.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Color%20Channel%20Swap/blue-red.jpg)
**Green and Blue swapped**             |  **Red and Green Swapped**
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Color%20Channel%20Swap/green-blue.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Color%20Channel%20Swap/red-green.jpg)

### Display color histograms.
4. Convert color image to black and white
### Resize
![Resize](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/resize.gif)

### Mirror
![Mirror](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/mirror.gif)

### Flip upside down
![Flip](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/flip.gif)

8. Rotate
9. Replace color
10. Perform following blurs:
  - Average
  - Median
  -Gaussian
### Add border
![Add Border](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/addborder.gif)

### Display intensity map
![Intenstity Maps](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/colormap.gif)

### Histogram equalization
![Histogram Equalization](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/hist_equal.gif)

Output Image:
![After Histogram Equalization](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Histogram%20Equalization/after_hist_equalization.jpg)

### Edge detection

### extract color


### Gamma correction




### Pixelate
![Pixelate](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/pixelate.gif)

The output image:
![Pixelated Image](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Pixelate/pixelate.png)

Negative

#### Salt and Pepper


### Dither

![Dithering](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/dither.gif)

Output image:
![Dithering](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Dithering/dithered_image.jpg)

### Alpha blending

### Adjust image brightness and contrast.

Contrast Stretching

The following functions are shown in the gif below:
Show image intensity histogram, convert to black and white, perform histogram equalization and then 



