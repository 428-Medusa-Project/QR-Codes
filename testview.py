import cv2
import numpy as np
import time
from urllib.parse import urlparse
from pyzbar.pyzbar import decode
import webview

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
                pts = cv2.convexHull(np.array([point for point in points], dtype=np.float32))

            # Draw the bounding box
            cv2.polylines(frame, [np.int32(pts)], True, (0, 255, 0), 3)

            # Get the data from the QR code
            qr_data = obj.data.decode('utf-8')
            #qr_type, payload = qr_data.split(':', 1)

            # Put the decoded text on the screen
            cv2.putText(frame, qr_data, (obj.rect[0], obj.rect[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Process the decoded QR code
            if qr_data.split(':')[0].lower() == "txt":
                print(qr_data[4:])
            elif qr_data.split(':')[0].lower() == "exe":
                exec(qr_data[4:])
            # if qr_data.split(':')[0].lower() == "js":
            #     # Create a WebView window and inject JavaScript
            #     print(f"JavaScript Payload: {payload}")
            #     window = webview.create_window('JavaScript Injection', 'http://localhost:5176/')
            #     webview.start(lambda: window.evaluate_js(payload))    
            else:
                parsed = urlparse(qr_data)
                if parsed.scheme in ["http", "https"]:
                    print(f"Opening URL in WebView: {qr_data}")
                    webview.create_window('QR Code URL', qr_data)
                    webview.start()  # Launch WebView

        # Display the resulting frame
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop if 'q' is pressed or the window is closed
        if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty("QR Code Scanner", cv2.WND_PROP_VISIBLE) < 1:
            cap.release()
            cv2.destroyAllWindows()
            break

QR_Scanner()
