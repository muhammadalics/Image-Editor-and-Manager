import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)


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

def add_border(image, top=0, bottom=0, left=0, right=0, bordertype=cv2.BORDER_CONSTANT, value=0):
    image = cv2.copyMakeBorder(image, top, bottom, left, right, bordertype, value)
    return image

def intensity_map(image, map):
    return cv2.applyColorMap(image, map)
    #NOTE: get list of colormaps

def histogram_equalization_bw(image):
    return cv2.equalizeHist(image)

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

def edge_detection(image, threshold1, threshold2):
    edges = cv2.Canny(image, threshold1, threshold2)
    return edges

def cartoonify(image, thresh1, thresh2):
    # https: // stacks.stanford.edu / file / druid: yt916dh6570 / Dade_Toonify.pdf
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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


    color_image = image[::4, ::4, :]
    for i in range(14):
        color_image = cv2.bilateralFilter(color_image, 9, 0, 0)
    color_image = cv2.resize(color_image, None, fx=4, fy=4, interpolation = cv2.INTER_LINEAR)
    color_image = cv2.medianBlur(color_image, 7)
    #quantize colors
    color_image = color_image // 24 * 24
    #when image is resized above it may get bigger than the original. so cut the extra rows and columns.
    color_image = color_image[0:canny.shape[0],0:canny.shape[1],:]

    #combining edges and color image
    color_image[canny == 255, :] = 0

    return color_image

def extract_color(image, color):
    # extract single color from image
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

def blending_using_pyramids(image):
    pass

def ndimage_rotate(image):
    pass

def gamma_correction():
    pass

def sketch_algo():
    pass

def pixelate():
    pass

def perspective_transform_etc():
    pass





