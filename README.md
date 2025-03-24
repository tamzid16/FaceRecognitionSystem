# FaceRecognitionSystem

A simple and efficient face recognition system built using Python, OpenCV, and the face_recognition library. This project enables the detection and recognition of faces from images and videos. The system trains itself by encoding faces from a dataset and then recognizes faces in real-time through video capture or image processing.

## Features

- **Face Encoding**: Collects face data from images and encodes it into a format suitable for recognition.
- **Real-time Face Recognition**: Recognizes faces from live video capture using your webcam.
- **Face Dataset Creation**: Allows users to capture and create a dataset for training the system.
- **User Identification**: Matches faces to user names based on the trained encodings.
- **Customizable**: Can be easily modified to include more functionality such as emotion recognition or multi-person detection.

## Technologies Used

- **Python**: The main programming language used.
- **OpenCV**: Used for handling image and video processing.
- **face_recognition**: A Python library built on top of dlib for face recognition.
- **Pickle**: Used for saving the encoded faces into a file for future recognition.
- **NumPy**: Used for array manipulations and handling face data.

## Software Requirements

- **Python**: Ensure you have Python 3.x installed.
- **Visual Studio Code (VSCode)**: A source-code editor that can help you write and manage the codebase efficiently.
- **Visual Studio (VS)**: A development environment for building C++ extensions that may be needed for the dlib library.
- **CMake**: A cross-platform tool used to manage the build process for the C++ components of the dlib library.

## Installing Dependencies

1. Install Python and other software mentioned above.
2. Clone the repository and install the necessary packages.

## Setting Up the Dataset

1. Collect the images you want to use for training the face recognition system.
2. Store the images in a directory (e.g., `dataset`).
3. Make sure each image is named with the user’s ID (e.g., `2001030_1.jpg`).

## Usage

### Train the System

The system can be trained by running a script that processes images and creates a model to store face encodings.

### Recognize Faces

Once the system is trained, you can run the face recognition process to perform real-time detection using a webcam.

## Example

After training the system with images, you can start recognizing faces in real-time using your webcam. The system will detect faces and match them to known encodings.

## Troubleshooting

- **No face detected**: Ensure that the images in the dataset are clear and contain only one person.
- **Low recognition accuracy**: Consider adding more images per person or adjusting face recognition parameters.

## Contributing

Feel free to fork the repository, submit issues, and create pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
