import cv2

# カメラを初期化
cap = cv2.VideoCapture(1)  # '0' はデフォルトカメラを指します

if not cap.isOpened():
    print("カメラを開けませんでした")
    exit()

# フレームを1つキャプチャ
ret, frame = cap.read()

if ret:
    # 画像を保存
    cv2.imwrite("captured_image.jpg", frame)
    print("写真を保存しました: captured_image.jpg")

# カメラを解放
cap.release()
cv2.destroyAllWindows()
