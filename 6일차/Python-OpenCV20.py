import datetime
import cv2

capture = cv2.VideoCapture("d:/python_data/el4.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
record = False

while True:
    if(capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT)):
        capture.open("d:/python_data/el4.mp4")

    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)

    now = datetime.datetime.now().strftime("%d_%H-%M-%S")
    key = cv2.waitKey(33)

    # 단축키 esc
    if key == 27:
        break

    # ctrl+z
    elif key == 26:     
        print("캡쳐")
        cv2.imwrite("D:/1/" + str(now) + ".png", frame)

    # ctrl+x
    elif key == 24:
        print("녹화 시작")
        record = True
        video = cv2.VideoWriter("D:/1/" + str(now) + ".avi", fourcc, 20.0, (frame.shape[1], frame.shape[0]))

    #ctrl+c
    elif key == 3:
        print("녹화 중지")
        record = False
        video.release()
        
    if record == True:
        print("녹화 중..")
        video.write(frame)

capture.release()
cv2.destroyAllWindows()
