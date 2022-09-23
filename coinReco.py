import cv2
import numpy as np

deltas = [[-1, 0], [0, 1], [1, 0], [0, -1]]
rot = 0
pilha = []
mat = []


def marcador(img, i, j, direc, rot):
    flag = -1
    print(img[i][j])
    if (img[i][j] == 255):
        pilha.append([i, j])
        marcaCelula(i, j, rot, direc)
        while (pilha[0] != None):
            for x in range(4):
                g = i+direc[x][0]
                h = j+direc[x][1]
                print("#19" + g, h)
                if (img[g][h] == 255):
                    pilha.append([g, h])
                    marcaCelula(i, j, rot, direc)
                    i = g
                    j = h
                    flag = 1
                    break
            if (flag == -1):
                i, j = pilha.pop()


def marcaCelula(i, j, rot, direc):
    for x in range(4):
        g = i+direc[x][0]
        h = j+direc[x][1]
        print(i)
        print(j)
        print(g)
        print(h)
        if (mat[g][h] != 0 and mat[g][h] != 255):
            mat[i][j] = mat[g][h]
            break
        if (mat[i][j] == 255):
            rot += 20
            mat[i][j] = rot


roi = cv2.imread("coins.jpg")

gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 11, 1)
kernel = np.ones((3, 3), np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,
                           kernel, iterations=10)


for i, x in enumerate(closing):
    for j, y in enumerate(x):

        if y == 255:
            marcador(closing, i, j, deltas, rot)

# cv2.imshow("Adaptive Thresholding", closing)
# cv2.waitKey(0)

print(mat)
