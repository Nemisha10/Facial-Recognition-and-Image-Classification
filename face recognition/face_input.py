import cv2
import os


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")
 
img_counter = 0
 
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
 
    k = cv2.waitKey(1)
    if k == ord('q'):
        # ESC pressed
        print("Closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        
        img_name = "opencv_frame_{}.png".format(img_counter)
        path = "C:/Users/tessy/Desktop/Notes/SEM II/Multivariate Statistics/Project/face recognition/images/"
        cv2.imwrite(os.path.join(path , img_name), frame)
        #cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

        name = input("Enter your name : ")
        old_name = r"C:/Users/tessy/Desktop/Notes/SEM II/Multivariate Statistics/Project/face recognition/images/opencv_frame_{}.png".format(img_counter)
        new_name = r"C:/Users/tessy/Desktop/Notes/SEM II/Multivariate Statistics/Project/face recognition/images/{}.png".format(name)
        os.rename(old_name, new_name)

cam.release()
 
cv2.destroyAllWindows()