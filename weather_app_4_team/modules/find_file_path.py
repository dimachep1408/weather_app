import os
import json

def find_path_to_file(name_file):
    path_to_file = __file__
    path_to_file = __file__.split("/")
    del path_to_file[-1]
    del path_to_file[-1]
    path_to_file = '/'.join(path_to_file)
    path_to_file = os.path.join(path_to_file, name_file)
    return path_to_file