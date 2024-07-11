import os


def path(value):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    return str(os.path.abspath(os.path.join(current_directory, value)))
