import cv2
import mediapipe as mp
import math
import pyautogui
import threading
import speech_recognition as sr
from pynput.mouse import Controller, Button

# Initialize mouse controller
mouse = Controller()

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Set up the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Variables
prev_x, prev_y = 0, 0
voice_command = ""
voice_command_executing = False

# Sensitivity factor for cursor movement
sensitivity_factor = 5.0  # Adjust as needed

# Function to perform mouse actions based on voice commands
def perform_mouse_action(command):
    global voice_command_executing
    if "left click" in command or "next slide" in command:
        mouse.click(Button.left)
    elif "right click" in command:
        mouse.click(Button.right)
    elif "scroll up" in command:
        mouse.scroll(0, 8)
    elif "scroll down" in command:
        mouse.scroll(0, -8)
    elif "scroll right" in command:
        mouse.scroll(6, 0)
    elif "scroll left" in command:
        mouse.scroll(-6, 0)

    voice_command_executing = False

# Function to recognize voice commands using SpeechRecognition
def recognize_voice_command():
    global voice_command, voice_command_executing
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Say something:")
            try:
                audio = recognizer.listen(source)  # Adjust timeout as needed
                command = recognizer.recognize_google(audio).lower()
                print("You said:", command)
                voice_command = command
                perform_mouse_action(command)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

# Start voice recognition in a separate thread
voice_thread = threading.Thread(target=recognize_voice_command)
voice_thread.start()

while True:
    # Capture webcam feed
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to get hand landmarks
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get coordinates of the index finger tip
            x, y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1]), \
                   int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])

            # Display the cursor
            cv2.circle(frame, (x, y), 15, (0, 255, 0), -1)

            # Move the cursor based on the change in position with sensitivity factor
            move_x = (x - prev_x) * sensitivity_factor
            move_y = (y - prev_y) * sensitivity_factor
            pyautogui.moveRel(move_x, move_y)

            # Update previous position
            prev_x, prev_y = x, y

    # Access the last recognized command from the voice recognition thread
    if voice_command_executing:
        perform_mouse_action(voice_command)

    # Display the frame
    pyautogui.FAILSAFE = False
    cv2.imshow('Hand Tracking', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Wait for the voice recognition thread to finish
voice_thread.join()

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
