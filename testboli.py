import numpy as np
import os
import cv2

def put_mask(img_path,output_fold):

    # 1.读取图片
    image = cv2.imread(img_path)
    print(image.shape)
    # 2.获取标签
    # 标签格式　bbox = [xl, yl, xr, yr]
    bbox = [300,400,600,700]

    # 3.画出mask
    zeros = np.zeros((image.shape), dtype=np.uint8)

    zeros_mask1 = cv2.rectangle(zeros, (bbox[0], bbox[1]), (bbox[2], bbox[3]),
                    color=(47,79,79), thickness=-1 ) #thickness=-1 表示矩形框内颜色填充
    # zeros_mask2 = cv2.circle(zeros, (300, 550), 50, (47,79,79), -1)

    # zeros_mask = np.array(zeros_mask1) + np.array(zeros_mask2)
    zeros_mask = np.array(zeros_mask1)
    cv2.rectangle(zeros_mask, (310, 410), (590, 690), (169, 169, 169), 10)

    # try:
    	# alpha 为第一张图片的透明度
    alpha = 1
    # beta 为第二张图片的透明度
    beta = 0.9
    gamma = 0
    # cv2.addWeighted 将原始图片与 mask 融合
    mask_img = cv2.addWeighted(image, alpha, zeros_mask, beta, gamma)
    cv2.imwrite(os.path.join(output_fold,'mask_img.jpg'), mask_img)

    # img = cv2.imread(img_path)
    # cropped = img[zeros_mask.shape]  # 裁剪坐标为[y0:y1, x0:x1]
    # # cv2.rectangle(cropped, (0, 0), (1100, 1100), (248,248,255), 10)
    # cv2.rectangle(cropped, (0, 0), (1100, 1100), (47, 79, 79), 40)
    # cv2.imwrite("G:/pythondealPic/cut.jpg", cropped)
    # except:
    #     print('异常')



put_mask(img_path = 'G:/pythondealPic/originalPic1.jpg', output_fold='G:/pythondealPic/')
