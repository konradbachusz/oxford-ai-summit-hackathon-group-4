import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import requests
from io import BytesIO


# Visualize the data
def show_sample_images(train_images, sample_size=10):
    """
    Displays a sample of images from the Fashion MNIST training dataset.

    Parameters:
    - train_images: numpy array of training images.
    - train_labels: numpy array of training labels.
    - class_names: list of class names corresponding to the labels.
    - sample_size: number of images to display (default is 10).
    """
    plt.figure(figsize=(10, 10))
    for i in range(sample_size):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)

    plt.show()


#Plot confusion matrix
def plot_confusion_matrix(model, test_images, test_labels, class_names):
    """
    Plots a confusion matrix using the predictions from a Keras model.

    Parameters:
    - model: trained Keras model.
    - test_images: numpy array of test images.
    - test_labels: numpy array of true labels for the test images.
    - class_names: list of class names corresponding to the labels.
    """
    # Get the model's predictions
    predictions = model.predict(test_images)
    predicted_labels = np.argmax(predictions, axis=1)
    true_labels = np.argmax(test_labels, axis=1)

    # Compute the confusion matrix
    cm = confusion_matrix(true_labels, predicted_labels)

    # Plot the confusion matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.title('Confusion Matrix')
    plt.show()



processor = AutoImageProcessor.from_pretrained("harshp8l/Fashion-Product-Images")
model = AutoModelForImageClassification.from_pretrained("harshp8l/Fashion-Product-Images")


# Function to load, display and predict the class of an image
def classify_image(image_url):
    """
    Loads an image from a URL, displays it, and predicts the class using a Hugging Face model.

    Parameters:
    - image_url: URL of the image to be classified.
    """
    # Load image from the URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Display the image
    plt.imshow(image)
    plt.axis('off')  # Hide the axis
    plt.show()

    # Preprocess the image and prepare it for the model
    inputs = processor(images=image, return_tensors="pt")

    # Predict the class of the image
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()

    # Retrieve the class name using the predicted class index
    class_name = model.config.id2label[predicted_class_idx]
    print(f"\nPredicted class: {class_name}")
