import datetime
import image_query
import image_editor
import cv2
# from datetime import date

# date1 = datetime.date.fromisoformat('2020-10-01')
# date2 = datetime.date.fromisoformat('2020-10-09')
#
# # datetime.timedelta(date1,date2)
#
# num_days=date2-date1
#
# date_list = [date1.isoformat()]
#
# for day in range(num_days.days):
#     date1 = date1 + datetime.timedelta(days=1)
#     image_query.query(date1.isoformat())
#     date_list.append(date1.isoformat())

start_date = '2006-10-19'
end_date = '2006-10-22'

# image_query.query(start_date, end_date)

image = cv2.imread('test.jpg', 1)
# mask = cv2.imread('mask.png', 0)
# cartoon = image_editor.cartoonify(image, 0, 100)
# cv2.imwrite('cartoon.png', cartoon)

# apple = cv2.imread('burt_apple.png')
# orange = cv2.imread('burt_orange.png')
# mask1 = cv2.imread('mask1.png')
# mask2 = cv2.imread('mask2.png')
#
# blended = image_editor.blending_pyramids(apple,orange, 255-mask1, 6)
#
# cv2.imwrite('blend.png', blended)

# img = image_editor.dither(image, 80)
# cv2.imwrite('dithered.png', img)

# img = image_editor.add_Gaussian_noise(image, 50, 'Red')
# cv2.imwrite('noisyimage.png', img)

# img = image_editor.band_noise_horizontal(image, 50, 100, 50)
# cv2.imwrite('noisyimage.png', img)

# img = image_editor.band_noise_vertical(image, 50, 100, 50)
# cv2.imwrite('noisyimage.png', img)

# img = image_editor.pixelate(image, 4)
# cv2.imwrite('noisyimage.png', img)

# img = image_editor.negative_color_picture(image)
# cv2.imwrite('neg.png', img)

# img = image_editor.gamma_correction(image, 0.5)
# cv2.imwrite('gamma_corrected.png', img)

# img = image_editor.contrast_stretching_RGB_channel(image, 10, 20)
# cv2.imwrite('gamma_corrected.png', img)

# img = image_editor.ndimage_rotate(image, 45)
# cv2.imwrite('gamma_corrected.png', img)

# img = image_editor.saltnpepper_noise_single_channel(image, 0.6, 255,0)
# cv2.imwrite('gamma_corrected.png', img)

# cv2.imwrite('bw.png', image)

# img = image_editor.intensity_map(image, 'jet')
# cv2.imwrite('heatmap.png', img)

# img = image_editor.edge_detection(image, 100, 200)
# cv2.imwrite('canny.png', img)

# img = image_editor.replace_color(image, '200,200,200', '0,0,0')
# cv2.imwrite('replaced.png', img)

# img = image_editor.extract_color(image, '255, 255, 255')
# cv2.imwrite('extracted_color.png', img)

# img = image_editor.brightness_up(image, 1.1, 0)
# cv2.imwrite('contrast.png', img)

# image_editor.image_histogram(image)

# print(image.shape)
# print(mask.shape)
#
# img = image_editor.mask_result_color(image, mask)
# cv2.imwrite('masked_applied.png', img)

img = image_editor.contrast_stretching_RGB_channel(image, 10, 230)
cv2.imwrite('contrast stretching.png', img)
