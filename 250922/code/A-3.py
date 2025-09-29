import glob,os

import cv2, numpy as np


for a in glob.glob(r"C:\Users\l\Desktop\2-ImageProcessing\250922\data\*.jpg"):
    img=cv2.imread(a)

    if img is None:
        print("error")
        continue

    thumb=cv2.resize(img,(160,160))

    filename = os.path.basename(a)
    name_without_ext = os.path.splitext(filename)[0]
    output_path = f"../out/thumbs/{name_without_ext}.png"

    cv2.imwrite(output_path, thumb)
    print(f"已处理: {filename} -> {name_without_ext}.png")