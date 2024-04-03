import cv2
import pyautogui
import math
import time
import numpy as np
# Ensure all necessary imports are included
# Adjust this import based on your file structure
from HandDetector import HandDetector
# Adjust if ScrollHandler is in a different file
from scroll_module import scroll_if_possible
# Adjust based on your drag_handler implementation
from drag_handler import drag_if_possible
from click_detector import detect_pinch


def main():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    dragging = False
    screenWidth, screenHeight = pyautogui.size()

    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture image")
            break
        img = cv2.flip(img, 1)
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img)
        print(type(detector))

        if lmList:
            try:

             # Assuming drag_if_possible function takes specific parameters
                fingers = detector.fingersUp()
                print(f"Fingers up: {fingers}")  # Debugging print
                if fingers[1] == 1:  # Move cursor if exactly one finger is up
                    index_finger_tip = lmList[8][1:]
                    # Get the x, y coordinates of the index finger tip
                    thumb_finger_tip = lmList[4][1:]

                    print(f"Index Finger Position: {index_finger_tip}")
                    # Debugging print
                    print(f"printing the thumb postion{thumb_finger_tip}")
                    

                # Scale the finger position to the screen size
                    x_scaled = np.interp(index_finger_tip[0], [
                                         0, 640], [0, screenWidth])
                    y_scaled = np.interp(index_finger_tip[1], [
                                         0, 480], [0, screenHeight])
                    # Debugging print
                    print(f"Scaled Position: {x_scaled}, {y_scaled}")

                    try:
                        pyautogui.moveTo(x_scaled, y_scaled)
                    except pyautogui.FailSafeException:
                        print("Cursor movement failed - FailSafeException")

                drag_if_possible(lmList, dragging,detector)

                # Scroll functionality
                scroll_if_possible(lmList,detector)
                    # Your existing code for drag functionality and scroll functionality here
                if detect_pinch(lmList):
                    pyautogui.click()
            except Exception as e:
                print(f"An error occurred: {e}")
                break  # Or handle the error as appropriate
        else:
            print("No hand landmarks detected")

        # Display the image and handle the quit condition
        cv2.imshow("Image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting...")
            break
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 255), 2)

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
