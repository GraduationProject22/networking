import json


def generate_json_object_from_fromatted_string(formatted_string):
    """
    Generates a json object from a formatted string.

    Parameters
    ----------
    formatted_string : str
        The formatted string to convert to a json object.
    """
    object = {}
    for item in formatted_string[:-1].split("?"):
        key, value = item.split(":")
        object[key] = value
    return json.dumps(object)
