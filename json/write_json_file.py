import imp
from generate_json_object_from_string import generate_json_object_from_string


def write_json_file(file_name, string):
    """
    Writes a string to a file.
    """
    json_object = generate_json_object_from_string(string)
    with open(file_name, 'w') as f:
        f.write(json_object)
