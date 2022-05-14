import cv2
import vlc
import time

def presenceMode(lowLight, pauseDelay, filePath, cap): 

    # Web Cam Brightness variable      
    # Min: 0, Max: 255, Increment:1 
    if lowLight.get() == 1:
        cap.set(10, 220)
    else:
        cap.set(10, 150)

    # Front Face classifier
    front_face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    
    # Upper Body classifier
    upper_body_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_upperbody.xml')

    # Used to record the time when we processed last frame
    prev_frame_time = 0

    # Used to record the time at which we processed current frame
    new_frame_time = 0

    # Get media file path
    media = vlc.MediaPlayer(filePath)
    media.play()

    # Timer variables for pause delay
    time_started = False 
    start_time = 0

    # Runs until q is pressed
    while True:
        # ret:   Returns false if webcam unavailable
        # frame: Image represented as numpy array
        ret, frame = cap.read()

        # Break if webcam unavailable
        if not ret:
            break

        # Convert image to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Font for fps
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Time when we finish processing for this frame
        new_frame_time = time.time()

        # Calculate the fps
        fps = int(1/(new_frame_time-prev_frame_time))
        prev_frame_time = new_frame_time

        # Convert the fps to string so that we can display it on frame
        fps = str(fps)

        # Put fps on frame
        cv2.putText(frame, fps, (0, 50), font, 2, (100, 255, 0), 3, cv2.LINE_AA)

        # Count of any detections found
        detection_count = 0

        """
        detectMultiScale 
        Detects objects of different sizes in the input image.

        :param image:           Matrix of the type CV_8U containing an image where objects are detected.
        :param scaleFactor:	    Parameter specifying how much the image size is reduced at each image scale.
        :param minNeighbors	    Parameter specifying how many neighbors each candidate rectangle should have to retain it.
        :return:                The detected objects are returned as a list of rectangles.
        """ 
        front_faces = front_face_cascade.detectMultiScale(gray, 1.3, 4)

        for (x, y, w, h) in front_faces:
            # Draw face rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
            detection_count += 1

        upper_body = upper_body_cascade.detectMultiScale(gray, 1.1, 2)
        for (x, y, w, h) in upper_body:
            # Draw body rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
            detection_count += 1

        # Display frame
        cv2.imshow('Camera Capture', frame)
        
        # If no eyes detected, and timer hasn't started, start timer        
        if detection_count == 0 and not time_started:
            start_time = time.time()
            time_started = True
        # If no eyes detected, timer started, and time elapsed greater than pause delay, pause video
        elif detection_count == 0 and time_started and time.time() - start_time > pauseDelay.get():
            start_time = 0
            time_started = False
            media.set_pause(1)
        # If eyes detected, and timer started, reset timer to 0
        elif detection_count > 0 and time_started:
            start_time = 0
            time_started = False


        # If media is paused and at least 1 eye detected, play video
        if not media.is_playing() and detection_count > 0:
            media.play()

        # q to quit
        if cv2.waitKey(1) == ord('q'):
            break

    # Release web camera resource    
    cap.release()
    # Destroy created windows
    cv2.destroyAllWindows()