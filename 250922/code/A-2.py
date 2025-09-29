import cv2
import numpy as np


def read_image_with_chinese_path(image_path):
    """
    读取包含中文路径的图片

    参数:
    image_path: 图片路径，可以包含中文

    返回:
    img: 读取到的图像，如果失败返回None
    """
    try:
        # 使用np.fromfile读取文件为字节流
        image_bytes = np.fromfile(image_path, dtype=np.uint8)

        # 检查是否成功读取到数据
        if len(image_bytes) == 0:
            print(f"错误: 文件为空或无法读取: {image_path}")
            return None

        # 使用cv2.imdecode解码字节流为图像
        img = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

        if img is None:
            print(f"错误: 无法解码图像: {image_path}")
            return None

        print(f"成功读取图像: {image_path}")
        print(f"图像尺寸: {img.shape}")
        return img

    except Exception as e:
        print(f"读取图像时发生异常: {e}")
        return None


# 测试代码
if __name__ == "__main__":
    # 替换为您的实际路径
    path = r"../data/测试图片.jpg"

    # 读取图像
    img = read_image_with_chinese_path(path)

    # 如果成功读取，显示图像
    if img is not None:
        cv2.imshow("中文路径图像", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("图像读取失败")