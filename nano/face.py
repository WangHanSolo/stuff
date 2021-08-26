import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
i = 0
pic_num = 0
while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display

    for face in faces:
        i+=1
        crop_im = img[face[1]:face[1] + face[3], face[0]:face[0] + face[2]]
        if i % 5 == 0:
            cv2.imwrite("han/han" + str(pic_num) + ".jpg",  crop_im)
            pic_num+=1
# Release the VideoCapture object
cap.release()