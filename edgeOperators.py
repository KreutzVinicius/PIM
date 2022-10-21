
from skimage import filters
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

#mage = imread('assets/Lua1_gray.jpg')
#image = imread('assets/chessboard_inv.png')
image = imread('assets/img02.jpg')
x, y = np.ogrid[:100, :100]


edge_sobel = filters.sobel(image)
edge_scharr = filters.scharr(image)
edge_prewitt = filters.prewitt(image)


fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=True,
                         figsize=(8, 8))
axes = axes.ravel()

axes[0].imshow(image, cmap=plt.cm.gray)
axes[0].set_title('Original image')

axes[1].imshow(edge_scharr, cmap=plt.cm.gray)
axes[1].set_title('Scharr')

axes[2].imshow(edge_sobel, cmap=plt.cm.gray, )
axes[2].set_title('Sobel')

axes[3].imshow(edge_prewitt, cmap=plt.cm.gray)
axes[3].set_title('Prewitt')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()
