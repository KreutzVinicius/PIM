from skimage import io, color
import histogram_equalizer as hteq
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def pxl_map_eq_hist(pxl_val, eq_map):
    return eq_map[pxl_val]


def equalize_map(histogram, size):
    # nk/n
    normalized_hist = list()
    for i in histogram:
        normalized = i/size
        normalized_hist.append(normalized)

    # gk
    acc_probability = list()
    total_sum = 0
    for i in normalized_hist:
        total_sum = total_sum + i
        acc_probability.append(total_sum)

    # round(gk*L)
    rounded = list()
    for i in acc_probability:
        equalized = round(i * 255)
        rounded.append(equalized)

    return rounded


def hist_equalize(image, histogram):
    height, width = image.size
    size = width * height
    map = equalize_map(histogram, size)
    new_image = image.point(lambda p: pxl_map_eq_hist(p, map))
    return new_image


def hist_equalize_rgb(image, histogram_r, histogram_b, histogram_g):
    height, width = image.size
    size = width * height
    map_r = equalize_map(histogram_r, size)
    map_b = equalize_map(histogram_b, size)
    map_g = equalize_map(histogram_g, size)

    new_image = Image.new(mode="RGB", size=(height, width))

    for i in range(0, height):
        for j in range(0, width):
            r, g, b = image.getpixel((i, j))
            new_image.putpixel((i, j), (pxl_map_eq_hist(
                r, map_r), pxl_map_eq_hist(g, map_g), pxl_map_eq_hist(b, map_b)))

    return new_image


np.set_printoptions(threshold=np.inf)

image = Image.open('assets/lena_B.png')
image.show()

plt.figure(0)
histogram = image.histogram()
red_h = histogram[0:256]
green_h = histogram[256:512]
blue_h = histogram[512:768]

width = 0.25

for i in range(0, 256):
    plt.bar(i, red_h[i], +width, color='r')
for i in range(0, 256):
    plt.bar(i+width, green_h[i], +width, color='g')
for i in range(0, 256):
    plt.bar(i+width*2, blue_h[i], +width, color='b')

eq_image = hteq.hist_equalize_rgb(image, red_h, blue_h, green_h)

plt.figure(1)
new_histogram = eq_image.histogram()
n_red_h = new_histogram[0:256]
n_blue_h = new_histogram[256:512]
n_green_h = new_histogram[512:768]

width = 0.25

for i in range(0, 256):
    plt.bar(i, n_red_h[i], +width, color='r')
for i in range(0, 256):
    plt.bar(i+width, n_green_h[i], +width, color='g')
for i in range(0, 256):
    plt.bar(i+width*2, n_blue_h[i], +width, color='b')

eq_image.show()

height, width = image.size
size = height*width
yiq_image = color.rgb2yiq(image)
y_channel = yiq_image[:, :, 0]
y_channel_sorted = np.sort(y_channel.flatten())

y_hist, bins = np.histogram(y_channel.flatten())
cdf = y_hist.cumsum()
cdf = y_channel_sorted[-1] * cdf / cdf[-1]
y_eq = np.interp(y_channel.flatten(), bins[:-1], cdf)

y_eq = y_eq.reshape(y_channel.shape)
yiq_image[:, :, 0] = y_eq
rgb_image = color.yiq2rgb(yiq_image)
io.imsave("lena_B_equalizado.png", rgb_image)

plt.figure(2)
_ = plt.hist(rgb_image[:, :, 0].ravel(), bins=256, color='red')
_ = plt.hist(rgb_image[:, :, 1].ravel(), bins=256, color='Green')
_ = plt.hist(rgb_image[:, :, 2].ravel(), bins=256, color='Blue')
plt.show()
