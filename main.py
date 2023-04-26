import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
from datetime import datetime

# Tesseract OCRのインストールパスを指定
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windowsの例

def capture_screenshot(bbox):
    # 指定された範囲のスクリーンショットを撮り、OpenCV形式に変換
    screenshot = ImageGrab.grab(bbox=bbox)
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return screenshot_cv

def extract_words(image):
    # OCRで画像からテキストを抽出
    text = pytesseract.image_to_string(image, lang='eng')
    # テキストを単語に分割
    words = text.split()
    return words

def print_formatted(words):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    unique_words = list(set(words))
    sorted_words = sorted(unique_words)

    print(f"\n{current_time} - Extracted words:")
    for word in sorted_words:
        print(f" - {word}")

def main():
    previous_words = set()

    # キャプチャ範囲を指定 (左上のX座標, 左上のY座標, 右下のX座標, 右下のY座標)
    capture_area = (500, 500, 800, 800)

    while True:
        # ゲーム画面のスクリーンショットを撮る
        screenshot = capture_screenshot(capture_area)

        # OCRでワードを抽出
        words = extract_words(screenshot)

        # 新しいワードがあれば整形して表示
        current_words = set(words)
        if current_words != previous_words:
            print_formatted(words)
            previous_words = current_words

        # 終了条件を定義（適宜変更）
        if "exit" in words:
            break

if __name__ == "__main__":
    main()
