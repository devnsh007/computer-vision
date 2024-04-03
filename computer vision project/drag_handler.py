import pyautogui
import numpy as np
import pyautogui


def drag_if_possible(lmList, dragging, detector):
    # Assuming lmList is a list of landmark positions and dragging is a boolean indicating the current dragging state
    # detector is an instance of HandDetector to use its methods
    screenWidth, screenHeight = pyautogui.size()
    # Check if the index, middle, and thumb fingers are extended
    fingers = detector.fingersUp()
    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1:  # Index, Middle, and Thumb
        if not dragging:
            # Start dragging
            dragging = True
            pyautogui.mouseDown()

            # Continue dragging - move the mouse to the index finger's position
            # Get the index finger tip position
            index_finger_tip = lmList[8][1:]
            x_scaled = np.interp(index_finger_tip[0], [
                                0, 640], [0, screenWidth])
            y_scaled = np.interp(index_finger_tip[1], [
                                0, 480], [0, screenHeight])
            pyautogui.moveTo(x_scaled, y_scaled)
    else:
        if dragging:
            # Stop dragging
            pyautogui.mouseUp()
            dragging = False

    return dragging
