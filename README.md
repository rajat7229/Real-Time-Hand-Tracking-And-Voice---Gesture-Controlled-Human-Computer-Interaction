# Real-time Hand Tracking and Speech Recognition for Human-Computer Interaction

## CONTENTS
- INTRODUCTION
- KEY FEATURES
- METHOD AND ALGORITHM
- APPLICATIONS
- FUTURE SCOPES
- CONCLUSION

## Introduction
- This project, a Gesture and Voice-Controlled Cursor Interface, combines computer vision and speech recognition technologies to create an innovative and intuitive method of interacting with a computer. 
- The system allows users to control the computer cursor using hand gestures and execute various commands through voice input.

## Key Features
**Hand Gesture Recognition:** Utilizes the Mediapipe library to detect and track hand gestures in real-time using the computer's webcam.
Calculates the movement of the index finger tip to control the on-screen cursor.

**Voice Command Recognition:** Implements the Speech Recognition library to capture voice commands through the computer's microphone.
Recognizes spoken commands, including "left click," "right click," "scroll up," "scroll down," "scroll right," and "scroll left."

**Cursor Movement Sensitivity:** Adjustable sensitivity factor for cursor movement, providing users with control over the responsiveness of the cursor to hand gestures.

**Accessibility and Hands-Free Interaction:** Designed with accessibility in mind, providing a hands-free and intuitive interface for individuals with mobility impairments or in situations where manual input is challenging.

**Real-Time Feedback:** Displays the live webcam feed with hand tracking and cursor movement, offering users immediate visual feedback.

**Open Source Technologies:** Built upon open-source libraries such as Mediapipe, SpeechRecognition, and Pynput, making it accessible for developers to explore and extend.

## METHOD AND ALGORITHM
**1. Hand Gesture Recognition:**

Method: 
The code uses the Mediapipe library, specifically the Hands module, for hand tracking and gesture recognition. Mediapipe provides pre-trained models for hand landmarks, which are used to detect and track key points on the hand, including fingertips.

Algorithm: 
The algorithm implemented in the Mediapipe library is based on a deep learning model trained for hand pose estimation. The model identifies the landmarks on the hand, such as the tip of the index finger, and tracks their positions in real-time.

**2. Voice Command Recognition:**

Method: 
The code utilizes the SpeechRecognition library to capture and recognize voice commands. The Google Web Speech API is used for speech recognition in this case.

Algorithm: 
The underlying algorithm involves processing the audio input from the computer's microphone and sending it to the Google Web Speech API for recognition. The API then returns the recognized text, representing the user's spoken command.

**3. Cursor Movement:**

Method: 
The cursor movement is controlled by the detected hand gestures. The code calculates the movement of the index finger tip in the webcam feed and uses this information to move the cursor on the computer screen.

Algorithm: 
The algorithm involves tracking the change in position of the index finger tip in consecutive frames. The movement is then scaled by a sensitivity factor to determine the amount by which the cursor should be moved.

**4. Mouse Actions Based on Voice Commands:**

Method: 
The code performs mouse actions based on recognized voice commands.

Algorithm: 
The algorithm checks for specific keywords in the recognized voice command, such as "left click," "right click," "scroll up," "scroll down," "scroll right," and "scroll left." Depending on the command, corresponding mouse actions (clicks or scrolls) are executed using the Pynput library.

**5. Concurrency and Threading:**

Method: 
The code uses threading to run the voice recognition process concurrently with the hand gesture and cursor control process.

Algorithm: 
Threading is implemented to separate the continuous voice recognition loop from the main loop responsible for hand gesture tracking and cursor control. This allows for responsive interaction by recognizing voice commands independently of the main loop.

**6. Real-Time Feedback:**

Method: 
The code provides real-time visual feedback by displaying the webcam feed with hand tracking and cursor movement.

Algorithm: 
 The algorithm continuously updates the display with the live webcam feed, drawing circles at the detected hand landmarks and showing the movement of the cursor in real-time.

**7. User Customization:**

Method: 
The code allows for customization of cursor movement sensitivity.

Algorithm: 
Users can adjust the sensitivity factor to control how responsive the cursor movement is to hand gestures. This customization involves scaling the calculated movement by the chosen sensitivity factor.

## APPLICATIONS
- **Gaming:** Gesture-based control can be applied in gaming scenarios, especially in VR gaming setups.
- **Accessibility Technology:** Enabling individuals with mobility impairments to control a computer using hand gestures and voice commands.
- **Hands-Free Computing:** In situations where manual input is not feasible or practical, such as in sterile environments or while cooking, this technology allows users to interact with a computer without physically touching any input devices.
- **Presentations and Demonstrations:** In presentations or live demonstrations where the presenter needs to control a computer while moving around or engaging with the audience.
- **Collaborative Work Environments:** Where multiple users are interacting with a shared display

## Future Scopes
- **Voice Command Extensibility:** Expand the supported voice commands to cover a wider range of actions and functionalities
- **Integration with AI Services:** Integrate the system with external AI services for natural language processing and context-aware commands. This could make the voice commands more versatile and flexible.
- **Multi-Gesture Support:** Extend the system to support a broader range of hand gestures, allowing users to perform a variety of actions beyond cursor movement and basic mouse commands.
- **Gesture Customization:** Introduce a customizable gesture mapping feature, allowing users to define their own gestures for specific actions. This level of customization can enhance the user experience and cater to individual preferences.

## CONCLUSION
In conclusion, the Python project ingeniously combines hand tracking, voice recognition, and mouse control, creating an interactive interface for intuitive computer interactions. Leveraging OpenCV, Mediapipe, and SpeechRecognition, the system responds to hand gestures and voice commands, promising a unique and versatile user experience with future potential for expanded functionalities and refinements.
