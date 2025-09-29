import numpy as np,cv2
path= r"../data/test.jpg"
img=cv2.imdecode(np.fromfile(path,dtype=np.uint8),-1)
print(img)
cv2.imshow("ok",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("图像属性信息：")
print(f"shape (高度, 宽度, 通道数): {img.shape}")
print(f"size (总像素数): {img.size}")
print(f"dtype (像素数据类型): {img.dtype}")

save_path = "../out/result.png"
if cv2.imwrite(save_path, img):
    print(f"图片已成功保存至: {save_path}")
else:
    print("图片保存失败！请检查out目录权限")
