from utils.generate_json_object_from_fromatted_string import generate_json_object_from_fromatted_string


def write_json_file(file_name, formatted_string):
    """
    Writes a formatted string to a json file.

    Parameters
    ----------
    file_name : str
        The name of the file to write to.
    formatted_string : str
        The formatted string to write to the file.
    """
    json_object = generate_json_object_from_fromatted_string(formatted_string)
    with open(file_name, 'w') as f:
        f.write(json_object)
