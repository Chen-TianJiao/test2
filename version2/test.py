
import cv2

srcImage = cv2.imread("G:/pythondealPic/originalPic1.jpg")

logo = cv2.imread("G:/pythondealPic/mask2x.png")
# 使用numpy数组切片，获取ROI(region of interest)，也就是感兴趣区域
imgeROI = srcImage[350:350+logo.shape[0], 800:800+logo.shape[1]]

cv2.addWeighted(imgeROI, 0.8, logo, 0.2, 0, imgeROI)
# 竟然等价以下
# srcImage[350:350+logo.shape[1], 800:800+logo.shape[0]] = cv2.addWeighted(imgeROI, 0.5, logo, 0.3, 0)
#将混合后的文件，重新保存为dota-logo.jpg
cv2.imwrite("G:/pythondealPic/qqw.jpg", srcImage)

# cv2.imshow("AddWeight Image", srcImage)
cv2.waitKey(0)