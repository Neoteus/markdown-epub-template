import os
import numpy as np
import cv2 as cv

def rec_crop(filename: str, debug=False):
    try:
        os.mkdir('output')
    except FileExistsError:
        pass
    if debug:
        filename_without_extension, ext = os.path.splitext(filename)
        try:
            os.mkdir('debug')
        except FileExistsError:
            pass
    img = cv.imread(filename)
    retval, bin_img = cv.threshold(img, thresh=254, maxval=255, type=cv.THRESH_BINARY)
    gray_bin_img = bin_img[:, :, 0]
    if debug:
        cv.imwrite(os.path.join('debug', f'{filename_without_extension}-bin{ext}'), gray_bin_img)
    contours, hierarchy = cv.findContours(gray_bin_img, mode=cv.RETR_EXTERNAL, method=cv.CHAIN_APPROX_NONE)
    if debug:
        i = 0
        while i < len(contours):
            contours_img = np.ones(img.shape) * 255
            for j in contours[i]:
                contours_img[j[0][1], j[0][0]] = 0
            cv.imwrite(os.path.join('debug', f'{filename_without_extension}-contours_{i}{ext}'), contours_img)
            i += 1
    left = contours[0][:,:,0].min()
    right = contours[0][:,:,0].max()
    top = contours[0][:,:,1].min()
    bottom = contours[0][:,:,1].max()
    cv.imwrite(os.path.join('output', filename), img[top:bottom, left:right])

for i in filter(lambda x: x.endswith('.png'), os.listdir()):
    rec_crop(i)
