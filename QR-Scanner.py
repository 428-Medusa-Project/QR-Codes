import cv2
import numpy as np
from pyzbar.pyzbar import decode

# Initialize the webcam (0 is the default camera, change if needed)
cap = cv2.VideoCapture(0)

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
        
        # Executes QR code
        exec(qr_data)

    # Display the resulting frame
    cv2.imshow("QR Code Scanner", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()
