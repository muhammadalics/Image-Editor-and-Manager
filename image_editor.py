import cv2
import numpy as np
import sys
import scipy.ndimage
import random
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvas

np.set_printoptions(threshold=sys.maxsize)


def brightness_up(image, contrast, brightness):
    return contrast * image + brightness

def brightness_down(image, contrast, brightness):
    return contrast * image - brightness

def swap_bg(image):
    image[:,:,[0,1]] = image[:,:,[1,0]]
    return image

def swap_gr(image):
    image[:,:,[1,2]] = image[:,:,[2,1]]
    return image

def swap_rb(image):
    image[:,:,[0,2]] = image[:,:,[2,0]]
    return image

def image_histogram(image):
    plt.style.use('ggplot')

    fig = Figure()
    canvas = FigureCanvas(fig)
    ax = fig.subplots()
    ax.margins(x=0)

    if len(image.shape) == 3:
        # hist_b, bins_b, hist_g, bins_g, hist_r, bins_r = hist_color(image)
        # plt.plot(bins_b, hist_b, color='blue')
        # plt.plot(bins_g, hist_g, color='green')
        # plt.plot(bins_r, hist_r, color='red')
        # plt.show()
        ax.hist(image[:,:,0].flatten(), np.arange(256), color='blue', label='blue', histtype='step', linewidth=1)
        ax.hist(image[:, :, 1].flatten(), np.arange(256), color='green', label='green', histtype='step', linewidth=1)
        ax.hist(image[:, :, 2].flatten(), np.arange(256), color='red', label='red', histtype='step', linewidth=1)
        ax.set_xlabel('Intensity')
        ax.set_ylabel('Count')
        ax.set_xticks([0,51,51*2,51*3,51*4, 51*5])
        canvas.draw()
        histogram_image = np.array(canvas.renderer.buffer_rgba())
        print(histogram_image.shape)
        # histogram_image[:,:, [0,2]] = histogram_image[:,:, [2,0]] #histogram_image is being converted to BGR

    else:
        # hist, bins = hist_bw(image)
        # plt.plot(bins, hist)
        # plt.show()
        ax.hist(image.flatten(), np.arange(256), histtype='step', linewidth=1, color='black')
        ax.set_xlabel('Intensity')
        ax.set_ylabel('Count')
        ax.set_xticks([0,51,51*2,51*3,51*4, 51*5])
        canvas.draw()
        histogram_image = np.array(canvas.renderer.buffer_rgba())

    cv2.imwrite('hist.png', histogram_image)

    return histogram_image



def hist_color(image):
    hist_b, bins_b = np.histogram(image[:, :, 0], bins=255, range=(0,256))
    hist_g, bins_g = np.histogram(image[:, :, 1], bins=255, range=(0,256))
    hist_r, bins_r = np.histogram(image[:, :, 2], bins=255, range=(0,256))
    return hist_b, bins_b, hist_g, bins_g, hist_r, bins_r

def hist_bw(image):
    hist, bins = np.histogram(image, bins=255, range=(0,256))
    return hist, bins

def convert_to_bw(image):
    if len(image.shape) == 3:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else: #if image has one channel just return the same
        return image

def resize_down(image,w, h):
    w_step = 100 / w
    h_step = 100 / h
    image[:, :, 0] = image[::h_step,::w_step,0]
    image[:, :, 1] = image[::h_step, ::w_step, 1]
    image[:, :, 2] = image[::h_step, ::w_step, 2]

    return image

def mirror(image):
    return np.fliplr(image)

def flip_upsidedown(image):
    return np.flipud(image)

def rotate_image(image):
    return np.rot90(image)

def replace_color(image, color_to_replace, target_color):
    color_to_replace = color_to_replace.split(sep=',')
    color_to_replace = [int(x) for x in color_to_replace]

    target_color = target_color.split(sep=',')
    target_color = [int(x) for x in target_color]

    print(color_to_replace)
    print(target_color)

    image[np.all(image[:,:,0] == color_to_replace[0], image[:,:,1] == color_to_replace[1], image[:,:,2] == color_to_replace[2])] = target_color
    print(image[np.all(image[:,:,0] == color_to_replace[0], image[:,:,1] == color_to_replace[1], image[:,:,2] == color_to_replace[2])])
    print('returning')
    return image

def avg_blur(image, k, times):
    k=int(k)
    times=int(times)
    for i in range(times):
        image = cv2.blur(image, (k,k))
    return image

def gaussian_blur(image, k, times):
    k=int(k)
    times=int(times)
    for i in range(times):
        image = cv2.GaussianBlur(image, (k,k), 0)
    return image

def median_blur(image, k, times):
    k=int(k)
    times=int(times)
    for i in range(times):
        image = cv2.medianBlur(image, k)
    return image

def add_border(image, top=0, bottom=0, left=0, right=0, bordertype=cv2.BORDER_CONSTANT, value=0):
    top =int(top)
    bottom=int(bottom)
    left=int(left)
    right=int(right)
    bordertype_dict={'cv2.BORDER_CONSTANT': cv2.BORDER_CONSTANT,
                     'cv2.BORDER_REFLECT101': cv2. BORDER_REFLECT101,
                     'cv2.BORDER_REFLECT': cv2.BORDER_REFLECT,
                     'cv2.BORDER_REPLICATE': cv2.BORDER_REPLICATE,
                     'cv2.BORDER_WRAP': cv2.BORDER_WRAP
                     }
    if bordertype_dict[bordertype] == cv2.BORDER_CONSTANT:
        image = cv2.copyMakeBorder(image, top, bottom, left, right, bordertype_dict[bordertype], value)
    else:
        image = cv2.copyMakeBorder(image, top, bottom, left, right, bordertype_dict[bordertype])

    return image

def intensity_map(image, map):
    map = 'COLORMAP_'+ map.upper().replace(' ', '_')

    map_dict = {
         'COLORMAP_AUTUMN' : 0,
          'COLORMAP_BONE' : 1,
          'COLORMAP_JET' : 2,
          'COLORMAP_WINTER' : 3,
          'COLORMAP_RAINBOW' : 4,
          'COLORMAP_OCEAN' : 5,
          'COLORMAP_SUMMER' : 6,
          'COLORMAP_SPRING' : 7,
          'COLORMAP_COOL' : 8,
          'COLORMAP_HSV' : 9,
          'COLORMAP_PINK' : 10,
          'COLORMAP_HOT' : 11,
          'COLORMAP_PARULA' : 12,
          'COLORMAP_MAGMA' : 13,
          'COLORMAP_INFERNO' : 14,
          'COLORMAP_PLASMA' : 15,
          'COLORMAP_VIRIDIS' : 16,
          'COLORMAP_CIVIDIS' : 17,
          'COLORMAP_TWILIGHT' : 18,
          'COLORMAP_TWILIGHT_SHIFTED' : 19,
          'COLORMAP_TURBO' : 20,
          'COLORMAP_DEEPGREEN' : 21
                }
    print(map)
    return cv2.applyColorMap(image, map_dict[map])



def histogram_equalization_bw(image):
    if len(image.shape) == 2:
        return cv2.equalizeHist(image)
    else:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        image[:,:,0] = cv2.equalizeHist(image[:,:,0])
        return cv2.cvtColor(image, cv2.COLOR_YUV2BGR)

# def histogram_equalization_color(image):
#     YCrCb_image  = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
#     YCrCb_image[:,:,intensity channel] = cv2.equalizeHist(YCrCb_image[:,:,intensity channel])
#     return YCrCb_image

def blend_images_bw(image1, image2, percentage):
    return image1*percentage + image2*(1-percentage)

def blend_images_color(image1, image2, percentage):
    image1[:,:,0] = image1[:,:,0]*percentage + image2[:,:,0]*(1-percentage)
    image1[:,:,1] = image1[:,:,1]*percentage + image2[:,:,1]*(1-percentage)
    image1[:,:,2] = image1[:,:,2]*percentage + image2[:,:,2]*(1-percentage)
    return image1

def non_linear_blend(image1, image2, percentage):

    pass

def edge_detection(image, threshold1, threshold2, kernelsize, L2grad):
    threshold1 = int(threshold1)
    threshold2 = int(threshold2)
    kernelsize = int(kernelsize)
    if L2grad == 'True': L2grad = True
    else: L2grad = False
    edges = cv2.Canny(image, threshold1, threshold2, apertureSize=kernelsize, L2gradient=L2grad)
    return edges

def cartoonify(image, thresh1, thresh2):
    # https: // stacks.stanford.edu / file / druid: yt916dh6570 / Dade_Toonify.pdf
    thresh1 = int(thresh1)
    thresh2 = int(thresh2)
    if len(image.shape) ==3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
    gray = cv2.medianBlur(gray, 7)
    canny = cv2.Canny(gray, thresh1, thresh2)
    canny = cv2.dilate(canny,(2,2))
    #find contours to remove small regions to reduce clutter.
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print(contours)

    for i, contour in enumerate(contours):
        if cv2.contourArea(contour) < 10:
            for points in contour:
                print(points[0][0])
                print(canny.shape)
                # points[0][:,[0,1]] = points[0][:,[1,0]]
                print([points[0][1],points[0][0]])
                canny[points[0][1],points[0][0]]  = 0

    if len(image.shape)==3:
        color_image = image[::4, ::4, :]
    else:
        color_image = image[::4, ::4]

    for i in range(14):
        color_image = cv2.bilateralFilter(color_image, 9, 0, 0)
    color_image = cv2.resize(color_image, None, fx=4, fy=4, interpolation = cv2.INTER_LINEAR)
    color_image = cv2.medianBlur(color_image, 7)
    #quantize colors
    color_image = color_image // 24 * 24
    #when image is resized above it may get bigger than the original. so cut the extra rows and columns.
    if len(color_image.shape) == 3:
        color_image = color_image[0:canny.shape[0],0:canny.shape[1],:]
    else:
        color_image = color_image[0:canny.shape[0], 0:canny.shape[1]]

    #combining edges and color image
    if len(color_image.shape) ==3:
        color_image[canny == 255, :] = 0
    else:
        color_image[canny == 255] = 0

    return color_image

def extract_color(image, color):
    # extract single color from image
    color = color.split(sep=',')
    color = [int(x) for x in color]

    extracted = np.zeros_like(image)
    extracted[np.all(image[:,:,0] == color[0], image[:,:,1] == color[1], image[:,:,2] == color[2])] = image[np.all(image[:,:,0] == color[0], image[:,:,1] == color[1], image[:,:,2] == color[2])]
    return extracted

def mask_result_color(image, mask):
    #when a mask is given, show the resulting image.
    image[:, :, 0] = image[:, :, 0] * mask
    image[:, :, 1] = image[:, :, 1] * mask
    image[:, :, 2] = image[:, :, 2] * mask
    return image

def mask_result_bw(image, mask):
    #when a mask is given, show the resulting image.
    image[:, :] = image[:, :] * mask
    return image

def blending_pyramids(imageA, imageB, mask, levels):
    dst = np.zeros_like(mask)
    mask = cv2.normalize(mask,None,0,1,cv2.NORM_MINMAX)
    # mask=dst

    # mask = np.divide(mask,255)

    print(mask.max())


    #make Gaussian pyramids of images A and B
    imageA_pyr_g = [imageA]
    imageB_pyr_g = [imageB]
    mask_pyr_g = [mask]

    pyr_g_img_A = imageA_pyr_g[0]
    pyr_g_img_B = imageB_pyr_g[0]
    pyr_g_mask = mask_pyr_g[0]

    for i in range(levels-1):
        pyr_g_img_A = cv2.pyrDown(pyr_g_img_A)
        imageA_pyr_g.append(pyr_g_img_A)
        # print(pyr_g_img_A.shape)
        pyr_g_img_B = cv2.pyrDown(pyr_g_img_B)
        imageB_pyr_g.append(pyr_g_img_B)
        pyr_g_mask = cv2.pyrDown(pyr_g_mask)
        mask_pyr_g.append(pyr_g_mask)

    for items in imageA_pyr_g:
        print(items.shape)

    #make Laplacian pyramids of image A and B
    lap_pyr_a = []
    lap_pyr_b = []
    lap_pyr_a.append(imageA_pyr_g[-1])
    lap_pyr_b.append(imageB_pyr_g[-1])



    i=len(imageA_pyr_g)-1
    print('i')
    print(i)

    while i > -1:
        # print('i')
        # print(i)

        la = cv2.pyrUp(imageA_pyr_g[i])
        # print('la.shape')
        # print(la.shape)
        # print('pyr_g_img_A[i-1].shape')
        # print(pyr_g_img_A[i-1].shape)

        la = la[:imageA_pyr_g[i-1].shape[0], :imageA_pyr_g[i-1].shape[1]]

        # print('la.shape')
        # print(la.shape)

        # lap_pyr_a.append(imageA_pyr_g[i-1] - la) #i-1
        lap_pyr_a.append(cv2.subtract(imageA_pyr_g[i - 1],la))  # i-1
        lb = cv2.pyrUp(imageB_pyr_g[i])
        lb = lb[:imageB_pyr_g[i-1].shape[0], :imageB_pyr_g[i-1].shape[1]]
        # lap_pyr_b.append(imageB_pyr_g[i-1] - lb) #i-1
        lap_pyr_b.append(cv2.subtract(imageB_pyr_g[i - 1], lb))  # i-1
        i-=1

    # lap_pyr_a.append(pyr_g_img_A[-1])
    # lap_pyr_b.append(pyr_g_img_B[-1])

    combined = []
    ci=0
    for a, b, m in zip(lap_pyr_a, lap_pyr_b, mask_pyr_g[::-1]):

        print('Before shape of m')
        print(m.shape)
        print('Before shape of a')
        print(a.shape)
        print('Before shape of b')
        print(b.shape)


        if a.shape[0] > m.shape[0]:
            a = a[:m.shape[0], :]
        if a.shape[1] > m.shape[1]:
            a = a[:, :m.shape[1]]

        if a.shape[0] < m.shape[0]:
            diff = m.shape[0] - a.shape[0]
            a = cv2.copyMakeBorder(src=a, top=0,bottom=diff, right=0, left=0, borderType=cv2.BORDER_REFLECT101)

        if a.shape[1] < m.shape[1]:
            diff = m.shape[1] - a.shape[1]
            a = cv2.copyMakeBorder(src=a, top=0, bottom=0, right=diff, left=0, borderType=cv2.BORDER_REFLECT101)

        if b.shape[0] > m.shape[0]:
            b = b[:m.shape[0], :]
        if b.shape[1] > m.shape[1]:
            b = b[:, :m.shape[1]]

        if b.shape[0] < m.shape[0]:
            diff = m.shape[0] - b.shape[0]
            b = cv2.copyMakeBorder(src=b, top=0, bottom=diff, right=0, left=0, borderType=cv2.BORDER_REFLECT101)

        if b.shape[1] < m.shape[1]:
            diff = m.shape[1] - b.shape[1]
            b = cv2.copyMakeBorder(src=b, top=0, bottom=0, right=diff, left=0, borderType=cv2.BORDER_REFLECT101)

        cv2.imwrite('img%s.png'%ci, a)

        print('After shape of m')
        print(m.shape)
        print('After shape of a')
        print(a.shape)
        print('After shape of b')
        print(b.shape)


        ma = cv2.multiply(m,a)
        one_minus_m_b = cv2.multiply(1-m, b)

        combined.append(cv2.add(ma, one_minus_m_b))

        # combined.append(m*a + (1-m)*b)

        ci+=1

    img = combined[0]
    cv2.imwrite('img_combined.png', combined[0])
    for i, c in enumerate(combined):
        if i !=0:
            img = cv2.pyrUp(img)
            img = img[:c.shape[0], :c.shape[1]]
            img = cv2.add(img,c)
            # cv2.imwrite('img%s.png'%i, img)

    return img

def ndimage_rotate(image, angle, axes=(1,0), reshape=True, output=None, order=3, mode='constant', cval=0.0, prefilter=True):
    return scipy.ndimage.rotate(image, angle, axes, reshape=True, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

def gamma_correction(image, gamma):
    gamma= float(gamma)
    return 255 * (image/255)**(1/gamma)

def sketch_algo():
    pass

def pixelate(image, n):
    n = int(n)
    image_copy= image.copy()
    for i in range(n):
        image_copy = cv2.pyrDown(image_copy)
    pixelated =cv2.resize(src=image_copy, dsize=(image.shape[1], image.shape[0]), interpolation=cv2.INTER_NEAREST)
    return pixelated

def perspective_transform_etc():
    pass

def negative_color_picture(image):
    return 255-image


def pseudo_solarised():
    pass

def add_Gaussian_noise(image, sigma, channel):
    sigma = float(sigma)

    if len(image.shape) == 2: channel = -1 #check if image is grayscale
    else:
        if channel == 'Blue': channel = 0
        if channel == 'Green': channel = 1
        if channel == 'Red': channel = 2

    random = np.random.normal(loc=0, scale=sigma, size=(image.shape[0], image.shape[1]))
    if channel !=-1: #if color
        image[:,:,channel] = image[:,:,channel] + random
    else: #if grayscale
        image = image + random
    return image

def add_noise02():
    pass

def noise_bands(image, width, period, orientation):

    if orientation == 'horizontal':
        shape_val = image.shape[0]

    if orientation == 'vertical':
        shape_val = image.shape[1]

    band = np.arange(width)

    tiled = np.tile(band, int(shape_val/period))
    tiled = tiled.reshape(-1, width)

    addition_arr = np.arange(period, shape_val, period)

    addition_arr = addition_arr.T

    addition_arr = np.expand_dims(addition_arr,axis=1)

    # print(addition_arr)

    addition_arr = np.repeat(addition_arr, tiled.shape[1], axis=1)

    print('add shape')
    print(addition_arr.shape)

    print('tiled shape')
    print(tiled.shape)

    tiled = tiled + addition_arr

    tiled = tiled.flatten()

    tiled = tiled[tiled < shape_val]

    return tiled

def band_noise_horizontal(image, width, period, magnitude):
    width = int(width)
    period = int(period)
    magnitude = int(magnitude)

    bands = noise_bands(image, width, period, 'horizontal')
    print(bands)
    image[bands, :, :] = image[bands, :, :] + magnitude
    return image

def band_noise_vertical(image, width, period, magnitude):
    width = int(width)
    period = int(period)
    magnitude = int(magnitude)

    bands = noise_bands(image, width, period, 'vertical')
    image[:, bands, :] = image[:, bands, :] + magnitude
    return image

def saltnpepper_noise_single_channel(image, amount, lower_threshold, upper_threshold):
    #amount should be a float
    # mask = np.random.rand(image.shape[0], image.shape[1])
    # empty_image = np.zeros_like(image)
    # empty_image[mask < amount] = 1

    # flat_empty = empty_image.flatten()

    # flat_image = image.flatten()
    # print(flat_image[flat_image==0].shape)
    # sample = random.sample(range(flat_image.shape[0]), int(amount * flat_image.shape[0]))
    #
    # print(flat_image.shape)
    # print(len(sample))
    #
    # chosen = flat_image[sample]
    #
    # print(chosen.shape)
    #
    # print(chosen[chosen==0].shape)
    # chosen[chosen > upper_threshold] = 0
    # print(chosen[chosen == 0].shape)
    # print(flat_image[flat_image == 0].shape)
    # flat_image[sample][flat_image[sample] > upper_threshold] = 0
    # print(flat_image[flat_image == 0].shape)
    # returned_image = flat_image.reshape(image.shape)
    #
    # return returned_image

    zero_arr = np.zeros_like(image)
    flatimage = image.flatten()

    lower_list = [1,255]

    flatimage[flatimage>upper_threshold] = np.random.randint(0,2,flatimage[flatimage>upper_threshold].shape) * flatimage[flatimage>upper_threshold]
    flatimage[flatimage < lower_threshold] = np.random.choice(lower_list, size=flatimage[flatimage < lower_threshold].shape) * \
                                             flatimage[flatimage < lower_threshold]
    flatimage = flatimage.reshape(image.shape)

    return flatimage


def dither(image, n):
    # Implements ordered dithering using a 2x2 matrix as described in https://en.wikipedia.org/wiki/Ordered_dithering
    # M = np.array([[0, 0.5], [0.75, 0.25]])

    n = int(n)

    img = image[::2, ::2]
    img[img>0] = 255

    img1 = image[::2, 1::2]
    img1[img1 > 0.5*n] = 255

    img2 = image[1::2, ::2]
    img2[img2 > 0.75*n] = 255

    img3 = image[1::2, 1::2]
    img3[img3 > 0.25*n] = 255

    return image

def contrast_stretching_single_channel(image, lower_threshold, upper_threshold):
    original_copy = image.copy()
    original_copy[image >= upper_threshold] = 255
    original_copy[image <= lower_threshold] = 0
    original_copy = 255 * (image - lower_threshold) / (upper_threshold - lower_threshold)
    return original_copy

# def contrast_stretching_RGB_channel(image, lower_threshold, upper_threshold):
#     image[:, :, 0] = contrast_stretching_single_channel(image[:, :, 0], lower_threshold, upper_threshold)
#     image[:, :, 1] = contrast_stretching_single_channel(image[:, :, 1], lower_threshold, upper_threshold)
#     image[:, :, 2] = contrast_stretching_single_channel(image[:, :, 2], lower_threshold, upper_threshold)
#     return image






