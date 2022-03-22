import numpy as np
import cv2

# Main Function
def main():

    # Web Cam Capture
    cap = cv2.VideoCapture(0)

    # Face classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Eye classifier
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

    # Runs until q is pressed
    while True:
        # ret:   Returns false if webcam unavailable
        # frame: Image represented as numpy array
        ret, frame = cap.read()

        # Convert image to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        
        """
        detectMultiScale 
        Detects objects of different sizes in the input image.

        :param image:           Matrix of the type CV_8U containing an image where objects are detected.
        :param scaleFactor:	    Parameter specifying how much the image size is reduced at each image scale.
        :param minNeighbors	    Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        :return:                The detected objects are returned as a list of rectangles.
        """ 
        faces = face_cascade.detectMultiScale(gray, 1.15, 5)


        for (x, y, w, h) in faces:
            # Draw face rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

            # Region of interest (face)
            roi_gray = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            # Detect eyes
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.15, 5)


            for (ex, ey, ew, eh) in eyes:
                # Draw eye rectangles
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

        # Display frame
        cv2.imshow('frame', frame)

        # q to quit
        if cv2.waitKey(1) == ord('q'):
            break

    # Release web camera resource    
    cap.release()
    # Destroy created windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()