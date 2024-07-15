import os


def path(value):
    current_directory = os.getcwd()
    parent_directory = os.path.dirname(current_directory)
    image_directory = os.path.join(parent_directory, 'resources')
    return str(os.path.abspath(os.path.join(image_directory, value)))
