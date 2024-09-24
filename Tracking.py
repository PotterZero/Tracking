import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Open the default camera
video_cam = cv2.VideoCapture(0)

# Check if the camera is accessible
if not video_cam.isOpened():
    print("Camera không hoạt động")
    exit()

# Main loop to capture frames from the camera
while True:
    ret, frame = video_cam.read()

    if ret:
        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=2)

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the number of detected faces on the frame
        text = f"Có {len(faces)} đối tượng trong khung hình"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show the video feed with detected faces
        cv2.imshow("Kết quả", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close all windows
video_cam.release()
cv2.destroyAllWindows()
