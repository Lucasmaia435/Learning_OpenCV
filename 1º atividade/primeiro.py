import cv2 as cv
import argparse

img = argparse.ArgumentParser()
img.add_argument('image')
imgs = vars(img.parse_args())
if __name__ == '__main__':

    img = cv.imread(imgs['image'],cv.IMREAD_COLOR)

    img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

    main_win = 'Imagem'
    cv.namedWindow(main_win, cv.WINDOW_KEEPRATIO)

    cv.imshow(main_win, img)
    cv.resizeWindow('Imagem',800,600)
    cv.waitKey(0)
    cv.destroyAllWindows()