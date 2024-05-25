# tests.py

import numpy as np
from unittest.mock import patch, MagicMock

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

    # Assert that no exceptions are raised
    assert True


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

    # Assert that no exceptions are raised
    assert True


@patch('src.notebook_funcs.requests.get')
@patch('src.notebook_funcs.AutoImageProcessor.from_pretrained')
@patch('src.notebook_funcs.AutoModelForImageClassification.from_pretrained')
def test_classify_image(mock_model, mock_processor, mock_requests_get):
    # Mocking image URL and response
    image_url = 'data/Blackdress.png'
    mock_response = MagicMock()
    mock_response.content = b'mock_image_data'
    mock_requests_get.return_value = mock_response

    # Mocking image processor and model
    mock_processor.return_value = MagicMock()
    mock_model.return_value = MagicMock()

    # Mocking model outputs
    mock_logits = MagicMock()
    mock_logits.argmax.return_value = 1  # Mock predicted class index
    mock_outputs = MagicMock()
    mock_outputs.logits = mock_logits
    mock_model.return_value.return_value = mock_outputs

    # Mocking class names
    mock_config = MagicMock()
    mock_config.id2label = {0: 'T-shirt/top', 1: 'Trouser'}  # Mock class names
    mock_model.return_value.config = mock_config

    # Call the function
    classify_image(image_url)

    # Assert that the correct URL is fetched
    mock_requests_get.assert_called_once_with(image_url)

    # Assert that image processing is called
    mock_processor.assert_called_once()

    # Assert that model prediction is called
    mock_model.assert_called_once()

    # Assert that the correct class name is printed
    assert mock_logits.argmax.call_count == 1  # Ensure argmax is called
    assert mock_outputs.logits.argmax.call_count == 1  # Ensure argmax is called
