import cv2
import os

if(not os.path.isdir("resized")):
  os.mkdir("resized")

for img_path in os.listdir("./img"):
  img = cv2.imread("img/" + img_path)
  height = img.shape[0]
  width = img.shape[1]
  ratio = max(height, width) / 600
  if ratio > 1:
    img = cv2.resize(img, (int(width/ratio), int(height/ratio)))
  cv2.imwrite("./resized/" + img_path, img)
