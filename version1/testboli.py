import numpy as np
import os
import cv2
import random

border_width = 10
mixed_img = "mixed_img.jpg"
cut_img = "cut_img.jpg"
cut_width = 300
randomLimit = [20, 70]

def get_mixed_picture(img_path, output_fold, bbox):
    # 1.读取图片
    image = cv2.imread(img_path)

    # 2.画出mask
    zeros = np.zeros((image.shape), dtype = np.uint8)
    print(bbox)
    zeros_mask1 = cv2.rectangle(zeros, (bbox[0], bbox[1]), (bbox[2], bbox[3]),
                                color=(47, 79, 79), thickness=-1)  # thickness=-1 表示矩形框内颜色填充

    zeros_mask2 = cv2.circle(zeros, (bbox[0], int(bbox[1] + cut_width/2)),
                             int(cut_width/4), color=(47, 79, 79), thickness =-1)
    zeros_mask = np.array(zeros_mask1) + np.array(zeros_mask2)
    cv2.rectangle(zeros_mask, (bbox[0] + border_width, bbox[1] + border_width),
                  (bbox[2] - border_width, bbox[3] - border_width), (169, 169, 169), border_width)

    try:
        # alpha 为第一张图片的透明度
        alpha = 1
        # beta 为第二张图片的透明度
        beta = 0.5
        gamma = 0
        # cv2.addWeighted 将原始图片与 mask 融合
        mask_img = cv2.addWeighted(image, alpha, zeros_mask, beta, gamma)
        cv2.imwrite(os.path.join(output_fold, mixed_img), mask_img)
    except:
        print('异常')


def get_screen_picture(img_path, output_fold, bbox):
    img = cv2.imread(img_path)
    cropped = img[bbox[1]:bbox[3], bbox[0]:bbox[2]]
    cv2.rectangle(cropped, (0, 0), (cut_width, cut_width), (105, 105, 105), border_width)
    cv2.imwrite(os.path.join(output_fold, cut_img), cropped)


def initData(img_path, bbox=[]):
    image = cv2.imread(img_path)
    minx = random.randint(randomLimit[0], randomLimit[1]) * (image.shape[0]) / 100
    maxx = minx + cut_width
    miny = random.randint(randomLimit[0], randomLimit[1]) * (image.shape[1]) / 100
    maxy = miny + cut_width
    bbox.append(int(minx))
    bbox.append(int(miny))
    bbox.append(int(maxx))
    bbox.append(int(maxy))

def main(img_path, output_fold, bbox=[]):
    initData(img_path, bbox)
    get_mixed_picture(img_path, output_fold, bbox)
    get_screen_picture(img_path, output_fold, bbox)


main(img_path='G:/pythondealPic/originalPic1.jpg', output_fold='G:/pythondealPic/', bbox=[])
