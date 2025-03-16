from PIL import Image
import cv2
import numpy as np

def pixelate(image_path, pixel_size=16, color_palette=16):
    # 이미지 로드
    image = Image.open(image_path)

    # 작은 크기로 줄이기
    small_image = image.resize(
        (image.width // pixel_size, image.height // pixel_size), Image.NEAREST
    )

    # 다시 확대 (픽셀 느낌 강조)
    pixelated_image = small_image.resize(image.size, Image.NEAREST)

    # OpenCV로 색상 수 줄이기
    img_cv = np.array(pixelated_image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)

    # K-means를 사용한 색상 감소
    Z = img_cv.reshape((-1, 3))
    Z = np.float32(Z)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = color_palette
    _, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    result_image = res.reshape((img_cv.shape))

    # PIL 이미지로 변환
    pixel_art = Image.fromarray(cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB))

    # 결과 저장
    output_path = f"~/Downloads/{image_path}_pixel.png"
    pixel_art.save(output_path)
    return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Convert an image to pixel art style.")
    parser.add_argument("image_path", help="Path to the input image")
    parser.add_argument("--pixel_size", type=int, default=16, help="Size of each pixel block")
    parser.add_argument("--color_palette", type=int, default=16, help="Number of colors in the final image")
    args = parser.parse_args()
    pixelate(args.image_path, pixel_size=args.pixel_size, color_palette=args.color_palette)