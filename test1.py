import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Khởi tạo video từ camera
cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)  # Đặt chiều rộng của video
cap.set(4, hs)  # Đặt chiều cao của video

# Kiểm tra xem camera có hoạt động không
if not cap.isOpened():
    print("Camera không thể truy cập!!!")
    exit()

# Khởi tạo bộ phát hiện khuôn mặt
detector = FaceDetector()
servoPos = [90, 90]  # Vị trí ban đầu của servo

while True:
    success, img = cap.read()  # Đọc khung hình từ camera

    if not success:
        print("Không thể lấy khung hình từ camera.")
        break

    # Phát hiện khuôn mặt và lấy bounding box
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        # Lấy tọa độ của khuôn mặt
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]

        # Vẽ vòng tròn và các đường thẳng chỉ vị trí của khuôn mặt
        cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
        cv2.putText(img, str(pos), (fx + 15, fy - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)  # Đường thẳng ngang (x)
        cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)  # Đường thẳng dọc (y)
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
        cv2.putText(img, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    else:
        # Khi không có khuôn mặt được phát hiện
        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)  # Đường thẳng ngang (x)
        cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)  # Đường thẳng dọc (y)

    # Hiển thị vị trí hiện tại của servo
    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # Hiển thị khung hình
    cv2.imshow("Image", img)

    # Kiểm tra xem người dùng có nhấn phím 'q' để thoát hay không
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng tất cả các cửa sổ
cap.release()
cv2.destroyAllWindows()
