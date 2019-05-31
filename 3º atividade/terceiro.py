import cv2 as cv
import argparse
import numpy as np
img = argparse.ArgumentParser()
img.add_argument('image')
img.add_argument('x1')
img.add_argument('x2')
img.add_argument('y1')
img.add_argument('y2')
imgs = vars(img.parse_args())

if __name__ == '__main__':

    img = cv.imread(imgs['image'],cv.IMREAD_COLOR)

    main_win = 'Resultados'
    cv.namedWindow(main_win, cv.WINDOW_KEEPRATIO)
    cv.resizeWindow('Resultados',800,600)
    for i in range(int(imgs['x1']), int(imgs['x2'])):
        for j in range(int(imgs['y1']),int(imgs['y2'])):
            img[i, j] = (255-img[i, j])
    cv.imshow(main_win, img)

    cv.waitKey(0)
    cv.destroyAllWindows()