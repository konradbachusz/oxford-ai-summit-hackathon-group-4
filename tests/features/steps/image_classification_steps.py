import sys
from io import StringIO

from behave import given, then

from src.notebook_funcs import classify_image



@given('I have passed an image of socks to the model')
def load_socks_image(context):
    context.image_url = 'https://media.loaf.com/image/upload/c_crop,h_857,w_1200,x_0,y_21/f_auto/q_auto/c_pad,h_786,w_1100/website/images/original/512789-sockins-sofa-sock-in-burnt-orange-stripe-full-sock-option-3.jpg'


@given('I have passed an image of shoes to the model')
def load_shoes_image(context):
    context.image_url = 'https://photos6.spartoo.co.uk/photos/245/24595191/24595191_1200_A.jpg'


@given('I have passed an image of a tracksuit to the model')
def load_tracksuit_image(context):
    context.image_url = 'https://clobbercartelz.com/cdn/shop/files/7A3AD657-B9ED-48E6-97AF-85870FA7DC41.jpg'


@then('it is classified as {category}')
def check_correct_category(context, category):

    stdout_capture = StringIO()
    sys.stdout = stdout_capture
    classify_image(context.image_url)
    sys.stdout = sys.__stdout__

    assert stdout_capture.getvalue() == f"\nPredicted class: {category}\n"
