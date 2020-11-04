# Image Editor and Manager

The Image Editor and Manager aims to deliver fundamental image processing tools using graphical user interface. OpenCV and Numpy were used to implement the image processing operations while graphical user interface was created using PyQt5. Below are the demonstration gifs to show how to use the program. Result images are also included.

The image editor can do the following:

### Pyramid blending
Pyramid blending as described in **A Multiresolution Spline With Application to Image Mosaics** by Burt and Adelson was implemented.

![Pyramid Blending](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/pyramid_blending.gif)

Blended Image Output

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

### Dither
![Dithering](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/dither.gif)

Original Image             |  Dithered Image
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/mountain.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Dithering/dithered_image.jpg)

### Swap color channels
![Swap Color Channels](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/swapcolorchannels.gif)

Original Image             |  Blue and Red swapped
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/mountain.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Color%20Channel%20Swap/blue-red.jpg)
**Green and Blue swapped**             |  **Red and Green Swapped**
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Color%20Channel%20Swap/green-blue.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Color%20Channel%20Swap/red-green.jpg)

### Display intensity map
![Intenstity Maps](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/colormap.gif)

Original Image             |  Jet theme
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/mountain.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Intensity%20Map/heatmap_jet.jpg)
**Magma theme**             |  **Viridis theme**
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Intensity%20Map/heatmap_magma.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Intensity%20Map/heatmap_viridis.jpg)

### Pixelate
![Pixelate](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/pixelate.gif)

Original             |  Output
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/cars.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Pixelate/pixelate.png)

### Histogram equalization
![Histogram Equalization](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Images%20for%20ReadMe/hist_equal.gif)

Original             |  Output
:-------------------------:|:-------------------------:
![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/glacier.jpg)  |  ![](https://github.com/muhammadalics/Image-Editor-and-Manager/blob/main/Test%20Images/Result/Histogram%20Equalization/after_hist_equalization.jpg)


### Resize
![Resize](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/resize.gif)

### Mirror
![Mirror](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/mirror.gif)

### Flip upside down
![Flip](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/flip.gif)


### Add border
![Add Border](https://github.com/muhammadalics/Image-Manager-and-Editor/blob/main/Images%20for%20ReadMe/addborder.gif)

In addition to the above the desktop app can perform the following operations:

* Edge detection using Canny algorithm
* Average, Median and Gaussian blurs
* Extract colors from images
* Gamma correction
* Alpha blending
* Rotate image
* Replace color
* Negative image
* Convert color image to black and white
* Adjust image brightness and contrast

## Setup
To run this app, clone the repo and run 'python main.py'.

##
