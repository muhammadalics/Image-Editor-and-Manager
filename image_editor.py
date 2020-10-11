import cv2
import numpy as np


def brightness_up(image, contrast, brightness):
    return contrast * image + brightness

def swap_bg(image):
    image[:,:,[0,1]] = image[:,:,[1,0]]
    return image

def swap_gr(image):
    image[:,:,[1,2]] = image[:,:,[2,1]]
    return image

def swap_rb(image):
    image[:,:,[0,2]] = image[:,:,[2,0]]
    return image

def hist_color(image):
    hist_b, bins_b = np.histogram(image[:, :, 0])
    hist_g, bins_g = np.histogram(image[:, :, 1])
    hist_r, bins_r = np.histogram(image[:, :, 2])
    return hist_b, bins_b, hist_g, bins_g, hist_r, bins_r

def hist_bw(image):
    hist, bins = np.histogram(image)
    return hist, bins

def convert_to_bw(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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
    image[np.all(image[:,:,0] == color_to_replace[0], image[:,:,1] == color_to_replace[1], image[:,:,2] == color_to_replace[2])] = target_color
    return image

def avg_blur(image, k, times):
    for i in range(times):
        image = cv2.blur(image, (k,k))
    return image

def gaussian_blur(image, k, times):
    for i in range(times):
        image = cv2.GaussianBlur(image, (k,k), 0)
    return image

def median_blur(image, k, times):
    for i in range(times):
        image = cv2.medianBlur(image, k)
    return image

def add_border(image, top=0, bottom=0, left=0, right=0, bordertype=cv2.BORDER_CONSTANT, value=0)
    image = cv2.copyMakeBorder(image, top, bottom, left, right, bordertype, value)
    return image

def intensity_map(image, map):
    return cv2.applyColorMap(image, map)
    #NOTE: get list of colormaps

def histogram_equalization_bw(image):
    return cv2.equalizeHist(image)

def histogram_equalization_color(image):
    YCrCb_image  = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    YCrCb_image[:,:,intensity channel] = cv2.equalizeHist(YCrCb_image[:,:,intensity channel])
    return YCrCb_image

def blend_images_bw(image1, image2, percentage):
    return image1*percentage + image2*(1-percentage)

def blend_images_color(image1, image2, percentage):
    image1[:,:,0] = image1[:,:,0]*percentage + image2[:,:,0]*(1-percentage)
    image1[:,:,1] = image1[:,:,1]*percentage + image2[:,:,1]*(1-percentage)
    image1[:,:,2] = image1[:,:,2]*percentage + image2[:,:,2]*(1-percentage)

    return image1

def non_linear_blend(image1, image2, percentage):
    pass

def edge_detection(image, threshold1, threshold2):
    edges = cv2.Canny(image, threshold1, threshold2)
    return edges

def cartoonify(image):
    # https: // stacks.stanford.edu / file / druid: yt916dh6570 / Dade_Toonify.pdf
    pass

def extract_color(image):
    #extract single color from image

def mask_result(image):
    #when a mask is given, show the resulting image.

def blending_using_pyarmids(image):
    pass

def ndimage_rotate(image):




