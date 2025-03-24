import cv2
import face_recognition
import pickle
import os

dataset_path = 'dataset'
encoding_file = 'face_encodings.pkl'
face_encodings = []
face_names = []

# Ensure dataset directory exists
if not os.path.exists(dataset_path):
    print(f"Error: Dataset folder '{dataset_path}' not found.")
    exit()

# Load and encode faces
for file in os.listdir(dataset_path):
    image_path = os.path.join(dataset_path, file)
    image = face_recognition.load_image_file(image_path)

    encodings = face_recognition.face_encodings(image)

    if len(encodings) > 0:
        face_encodings.append(encodings[0])
        face_names.append(file.split('_')[0])

# Save encodings
data = {"encodings": face_encodings, "names": face_names}
try:
    with open(encoding_file, 'wb') as f:
        f.write(pickle.dumps(data))
    print("Face recognition model trained and saved!")
except Exception as e:
    print(f"Error saving encodings: {e}")
