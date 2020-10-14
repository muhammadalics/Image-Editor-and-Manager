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

image = cv2.imread('test.jpg')
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

# img = image_editor.dither(image, 500)
# cv2.imwrite('dithered.png', img)

# img = image_editor.add_Gaussian_noise(image, 50)
# cv2.imwrite('noisyimage.png', img)

img = image_editor.band_noise_vertical(image, 30, 10, 10)
cv2.imwrite('noisyimage.png', img)