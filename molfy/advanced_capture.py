import cv2 as cv
import timeit

cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')
cap = cv.VideoCapture(0)
if not cap.isOpened():
    exit()
while True:

    start_t = timeit.default_timer()
    ret, img = cap.read()
    if not ret:
        print("Can't read camera")
        break
    img = cv.resize(img,dsize=None,fx=1.0,fy=1.0)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    results = cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=5, minSize=(20,20))
    crop = None
    for box in results:
        x, y, w, h = box
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=2)
        crop = img[y+3:y+h-3,x+3:x+w-3]
    terminate_t = timeit.default_timer()
    FPS = 'fps' + str(int(1. / (terminate_t - start_t)))
    #cv.putText(img, FPS, (30, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)

    cv.imshow("cam",img)
    tmp=cv.waitKey(1)
    if tmp & 0xFF == ord('c'):
        img_captured = cv.imwrite('current.jpg',img)
        img_cropped = cv.imwrite('cropped.jpg',crop)

cap.release()
cv.destroyAllWindows()
