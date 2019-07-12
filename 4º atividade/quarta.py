import cv2 as cv
import argparse as arg
import numpy as np
argument = arg.ArgumentParser()
argument.add_argument('image')
img = vars(argument.parse_args())
if __name__ == '__main__':

    # Leitura de imagem
    img = cv.imread(img['image'],cv.IMREAD_COLOR)
    
    # Intervalo de erro
    threshold = 60
    
    #-------------------------------------- Cores ------------------------------------- #
    colors = [[29,37,218],[10,120,25],[0,195,248],[221,147,0],[183,132,142],[230,64,204]]
    #         Red         Green       Yellow      Blue        Purple         Pink    
    
    for i in range(6):
        window = 'Region {}'.format(i+1)
        
        # Calculando o BGR minímo
        minB = colors[i][0] - threshold
        minG = colors[i][1] - threshold
        minR = colors[i][2] - threshold

        # Calculando o BGR máximo
        maxB = colors[i][0] + threshold
        maxG = colors[i][1] + threshold
        maxR = colors[i][2] + threshold

        # Arrays de máximo e mínimo
        minBGR = np.array([minB,minG,minR])
        maxBGR = np.array([maxB,maxG,maxR])
        
        maskBGR = cv.inRange(img, minBGR, maxBGR)
        
        resultBGR = cv.bitwise_and(img, img, mask = maskBGR)
            
        cv.imshow(window,resultBGR)
    cv.waitKey(0)
    cv.destroyAllWindows()