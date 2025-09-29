import cv2
import numpy as np

# 读取图片
img = cv2.imread('image/eye-3.jpeg')

# 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 加载眼睛检测器
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 检测眼睛
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(f"检测到 {len(eyes)} 只眼睛")

if len(eyes) >= 2:
    # 方法1：取最可能的两只眼睛（基于位置和大小）
    # 假设两只眼睛应该在相似的高度上，且大小相近
    eyes_list = list(eyes)

    # 按y坐标排序，找到在相似高度上的眼睛
    eyes_list.sort(key=lambda e: e[1])

    # 计算眼睛中心点
    centers = [(x + w / 2, y + h / 2, w, h) for (x, y, w, h) in eyes_list]

    # 找到y坐标最接近的两只眼睛
    selected_eyes = []
    min_y_diff = float('inf')

    for i in range(len(centers)):
        for j in range(i + 1, len(centers)):
            y_diff = abs(centers[i][1] - centers[j][1])
            # 如果y坐标差异小于眼睛高度的一半，认为是同一行的眼睛
            if y_diff < max(centers[i][3], centers[j][3]) / 2:
                if y_diff < min_y_diff:
                    min_y_diff = y_diff
                    selected_eyes = [eyes_list[i], eyes_list[j]]

    # 如果没有找到合适的两只眼睛，使用原始方法
    if not selected_eyes:
        selected_eyes = eyes_list[:2]

    # 取两只眼的并集区域
    x1 = min([x for x, y, w, h in selected_eyes])
    y1 = min([y for x, y, w, h in selected_eyes])
    x2 = max([x + w for x, y, w, h in selected_eyes])
    y2 = max([y + h for x, y, w, h in selected_eyes])

    print(f'打码区域坐标: x1={x1}, x2={x2}, y1={y1}, y2={y2}')

    # 创建随机噪声区域
    rec = np.random.randint(0, 256, (y2 - y1, x2 - x1, 3), dtype=np.uint8)
    img[y1:y2, x1:x2] = rec

    cv2.imshow("eye-covered", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("未检测到足够数量的眼睛")



#多图片生成并保存
# import cv2
# import numpy as np
# import os
# import glob
#
#
# # 定义眼睛检测函数
# def detect_and_cover_eyes(img_path, output_dir=None):
#     """检测图片中的眼睛并进行打码处理"""
#     # 读取图片
#     img = cv2.imread(img_path)
#     if img is None:
#         print(f"错误：无法读取图片 {img_path}")
#         return None
#
#     # 获取文件名（不含路径和扩展名）
#     filename = os.path.basename(img_path)
#     name, ext = os.path.splitext(filename)
#
#     # 转换为灰度图
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # 加载眼睛检测器
#     eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
#
#     if eye_cascade.empty():
#         print("错误：无法加载眼睛检测器")
#         return None
#
#     # 检测眼睛
#     eyes = eye_cascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(20, 20)
#     )
#
#     print(f"{filename}: 检测到 {len(eyes)} 个眼睛区域")
#
#     # 可视化检测结果
#     img_detection = img.copy()
#     for (x, y, w, h) in eyes:
#         cv2.rectangle(img_detection, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     if len(eyes) >= 2:
#         # 取前两只最大的眼睛（按面积排序）
#         eyes_sorted = sorted(eyes, key=lambda rect: rect[2] * rect[3], reverse=True)[:2]
#
#         # 取两只眼的并集区域
#         x1 = min([x for x, y, w, h in eyes_sorted])
#         y1 = min([y for x, y, w, h in eyes_sorted])
#         x2 = max([x + w for x, y, w, h in eyes_sorted])
#         y2 = max([y + h for x, y, w, h in eyes_sorted])
#
#         # 扩大区域以确保完全覆盖
#         padding = 10
#         x1 = max(0, x1 - padding)
#         y1 = max(0, y1 - padding)
#         x2 = min(img.shape[1], x2 + padding)
#         y2 = min(img.shape[0], y2 + padding)
#
#         print(f'{filename}: 打码区域坐标: x1={x1}, x2={x2}, y1={y1}, y2={y2}')
#
#         # 创建马赛克效果
#         mosaic_size = 10
#         region = img[y1:y2, x1:x2]
#
#         # 缩小再放大创建马赛克效果
#         h, w = region.shape[:2]
#         small = cv2.resize(region, (w // mosaic_size, h // mosaic_size))
#         mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)
#
#         img[y1:y2, x1:x2] = mosaic
#
#         # 保存处理后的图片
#         if output_dir:
#             output_path = os.path.join(output_dir, f"{name}_covered{ext}")
#             cv2.imwrite(output_path, img)
#             print(f"已保存处理后的图片: {output_path}")
#
#         return img
#     else:
#         print(f"{filename}: 未检测到足够数量的眼睛，跳过处理")
#         return None
#
#
# # 主程序
# def main():
#     # 方法1: 处理指定文件夹下的所有图片
#     input_folder = "image"  # 输入文件夹路径
#     output_folder = "output"  # 输出文件夹路径
#
#     # 创建输出文件夹（如果不存在）
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # 支持的图片格式
#     image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp', '*.tiff']
#
#     # 获取所有图片文件
#     image_files = []
#     for ext in image_extensions:
#         image_files.extend(glob.glob(os.path.join(input_folder, ext)))
#         image_files.extend(glob.glob(os.path.join(input_folder, ext.upper())))
#
#     print(f"找到 {len(image_files)} 个图片文件")
#
#     # 处理每个图片
#     for img_path in image_files:
#         print(f"\n处理图片: {img_path}")
#         result = detect_and_cover_eyes(img_path, output_folder)
#
#         # 显示处理结果（可选）
#         if result is not None:
#             cv2.imshow("处理结果", result)
#             cv2.waitKey(2000)  # 显示2秒
#
#     cv2.destroyAllWindows()
#
#     # 方法2: 处理指定文件列表
#     # 如果你有特定的文件列表，可以使用这种方式
#     # specific_files = [
#     #     "image/eye1.jpg",
#     #     "image/eye2.jpg",
#     #     "image/eye3.jpg"
#     # ]
#     #
#     # for img_path in specific_files:
#     #     print(f"\n处理图片: {img_path}")
#     #     detect_and_cover_eyes(img_path, output_folder)
#
#
# if __name__ == "__main__":
#     main()