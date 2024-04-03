import math


def detect_pinch(lm_list):
    # Check if hand landmarks list is not empty and contains at least landmarks for thumb and index finger
    if len(lm_list) >= 2:
        thumb_tip = lm_list[4][1:]
        index_tip = lm_list[8][1:]
        # Calculate the distance between the thumb and index finger tips
        distance = math.dist(thumb_tip, index_tip)
        # Define a threshold for the pinch gesture
        pinch_threshold = 30  # Adjust this threshold based on your preference
        # If the distance is smaller than the threshold, consider it a pinch
        if distance < pinch_threshold:
            return True
    return False
