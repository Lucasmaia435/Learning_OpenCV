from random import randint
import cv2 as cv
import argparse
import numpy as np

img = argparse.ArgumentParser()
img.add_argument('image')
imgs = vars(img.parse_args())

if __name__ == '__main__':

    img = cv.imread(imgs['image'],cv.IMREAD_COLOR)

    main_win = 'Resultados'
    cv.namedWindow(main_win, cv.WINDOW_KEEPRATIO)
    cv.resizeWindow('Resultados',800,600)
    height, width, _ = img.shape
    for i in range(0, height):
        for j in range(0, width):
            if np.any(img[i, j] == [104,56,35]) : 
                img[i, j] = [255,255,255]
    
    cv.imshow(main_win, img)
    cv.waitKey(0)
    cv.destroyAllWindows()
