import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
t=()
while True:
    sucess,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if faces==t:
        cv2.putText(img, "Not Detected", (30, 30), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)

    else:
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), 2)
            cv2.putText(img, "Detected", (x - 10, y - 10), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break