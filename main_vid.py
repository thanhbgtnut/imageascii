# #pip install opencv-python
# import cv2
# import time
# import numpy as np
# import os
# # image = cv2.imread(r"C:\Users\thanh\Desktop\anhdomixi.jpg", 1)
#
# vid = cv2.VideoCapture(0)
# while True:
#     _, image = vid.read()
#     new_w = int(image.shape[1]/3)
#     new_h = int(image.shape[0]/3)
#     image = cv2.resize(image, (new_w, new_h))
#     image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#     charmap =" .,:;ox#1O"
#     # with open("anhdo.txt", 'w', encoding='utf-8') as f:
#     cv2.imshow("tao", image)
#     sim = ''
#     for i, row in enumerate(image):
#         for j, col in enumerate(row): # 0 - 255 - > 0-9
#             c = int((255 - col)*10 / 256)
#             # f.write(charmap[c])
#             sim+=charmap[c]
#         sim += '\n'
#     # os.system('cls')
#     print(sim)
#     cv2.waitKey(24)
#         #     print(charmap[c], end='')
#         # print(charmap[c], end='')
#         # print('\n', end='')
#         # # f.write('\n')
#         # time.sleep(0.1)
#     # f.close()
# # cv2.imshow("anhdotay", src)
# # cv2.waitKey(999)



import cv2
import time
image = cv2.imread(r"B:\bigdata\DATA_DETECT\16.jpg", 1)

new_w = int(image.shape[1]/2)
new_h = int(image.shape[0]/2)
image = cv2.resize(image, (new_w, new_h))
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
charmap =" .,:;ox#1O"
with open("anhdo.txt", 'w', encoding='utf-8') as f:
    for i, row in enumerate(image):
        s = ''
        for j, col in enumerate(row): # 0 - 255 - > 0-9
            c = int((255 - col)*10 / 256)
            s +=charmap[c]
        print(s)
        f.write(s+'\n')
        time.sleep(0.1)
f.close()
# cv2.imshow("anhdotay", src)
# cv2.waitKey(999)



