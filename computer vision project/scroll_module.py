import pyautogui


def scroll_if_possible(lmList, detector):
    if not lmList:
        return

    index_finger_tip_y = lmList[8][2]  # y-coordinate of the index finger tip
    fingers_up = detector.fingersUp()
    if fingers_up[0] == 1  and all(finger == 0 for finger in fingers_up[:]):
        pyautogui.scroll(200)
    elif all(finger==0 for finger in fingers_up[:]):
      # Adjust sensitivity if needed
        pyautogui.scroll(-200)


        
