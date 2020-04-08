import cv2

filename = "data/Robotic_Surgical_System_240.mp4"
vidcap = cv2.VideoCapture(filename)
frameTime = 10   # time of each frame in ms, you can add logic to change this value.
i=0
while (vidcap.isOpened()):
    try:
        success, frame_org = vidcap.read()
        if success != False:
            cv2.imshow('frame', frame_org)
            print(frame_org)
            i+=1
            print(i)
            key = cv2.waitKey(frameTime)
            if key & 0xFF == ord('q'):
                break
            elif key == ord('p'):
                cv2.waitKey(-frameTime)  # wait until any key is pressed
        else:
            break
    except Exception as e:
        print(e)
        break

vidcap.release()
cv2.destroyAllWindows()