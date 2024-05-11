import cv2
import numpy as np
import dlib

def process_image(image_path):
    """Reads an image from the given path and performs face detection."""

    # Load pre-trained face detector
    detector = dlib.get_frontal_face_detector()

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    detected_faces = detector(gray, 1)

    # Process each detected face
    for face_rect in detected_faces:
        # Get a random color for the bounding box
        color = random_color()

        # Draw a rectangle around the detected face
        cv2.rectangle(image, (face_rect.left(), face_rect.top()), (face_rect.right(), face_rect.bottom()), color, 2)

        # (Optional) Apply additional image processing techniques within the loop

    # Display the processed image
    cv2.imshow('Detected Faces', image)
    cv2.waitKey(0)  # Wait indefinitely until any key is pressed
    cv2.destroyAllWindows()

# Function to generate a random color for bounding boxes
def random_color():
    while True:
        color = (np.random.randint(0, 256, size=3)).tolist()
        if color[0] != color[1] and color[0] != color[2] and color[1] != color[2]:
            return tuple(color)

# Run the image processing function with a sample image
process_image('sample_image.jpg')  # Replace 'sample_image.jpg' with the path to your image
