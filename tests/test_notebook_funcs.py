import numpy as np

from src.notebook_funcs import (
    show_sample_images,
    plot_confusion_matrix,
    classify_image
)


def test_show_sample_images():
    # Define test inputs
    sample_size = 5  # Adjust the sample size as needed
    train_images = np.random.rand(sample_size, 28, 28)

    # Call the function
    show_sample_images(train_images, sample_size)


def test_plot_confusion_matrix():
    # Define test inputs
    # Mock a model
    class MockModel:
        @staticmethod
        def predict(test_images):
            # Mock predictions
            num_classes = 10
            num_samples = len(test_images)
            return np.random.rand(num_samples, num_classes)

    test_images = np.random.rand(100, 28, 28)
    test_labels = np.random.randint(10, size=(100, 10))
    class_names = ['class_' + str(i) for i in range(10)]

    # Call the function
    plot_confusion_matrix(MockModel(), test_images, test_labels, class_names)


def test_classify_image():
    image_url = 'https://clobbercartelz.com/cdn/shop/files/7A3AD657-B9ED-48E6-97AF-85870FA7DC41.jpg'

    # Call the function
    classify_image(image_url)
