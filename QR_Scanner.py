import cv2
import numpy as np
import time
import webbrowser
from pyzbar.pyzbar import decode

# Initialize the webcam (0 is the default camera, change if needed)
cap = cv2.VideoCapture(0)

def QR_Scanner():
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
    
        # Decode any QR codes in the frame
        decoded_objects = decode(frame)
    
        # Loop through all decoded objects
        for obj in decoded_objects:
            # Draw a rectangle around the QR code
            points = obj.polygon
            if len(points) == 4:
                pts = points
            else:
                # If the shape of the QR code is not a quadrilateral, we approximate
                pts = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
    
            # Draw the bounding box
            cv2.polylines(frame, [np.int32(pts)], True, (0, 255, 0), 3)
    
            # Get the data from the QR code
            qr_data = obj.data.decode('utf-8')
    
            # Put the decoded text on the screen
            cv2.putText(frame, qr_data, (obj.rect[0], obj.rect[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            # Executes QR code data depending on the associated tag
            if qr_data.split(':')[0].lower() == "txt":
                print(qr_data[4:])
            elif qr_data.split(':')[0].lower() == "exe":
                exec(qr_data[4:])
            # elif qr_data.split(':')[0] == "pic":
            #     with open('image.png', 'wb') as file:
            #         file.write(qr_data[4:])
            elif qr_data.split(':')[0].lower() == "url":
                webbrowser.open(qr_data[4:])
                
            # Pauses the program for 1 second 
            time.sleep(1)

        # Display the resulting frame
        cv2.imshow("QR Code Scanner", frame)
    
        # Break the loop if 'q' is pressed or the window is closed
        if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty("QR Code Scanner", cv2.WND_PROP_VISIBLE) < 1:
            # Release the capture and close the window
            cap.release()
            cv2.destroyAllWindows()
            break

QR_Scanner()