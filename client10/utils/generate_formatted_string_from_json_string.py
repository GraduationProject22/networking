import json


def generate_formatted_string_from_json_string(json_string):
    """
    Generates a formatted string from a json string.

    Parameters
    ----------
    json_string : str
        The json string to format.
    """
    json_object = json.loads(json_string)
    result_string = ""

    for key in json_object:
        result_string += key + "=" + str(json_object[key]) + ","

    return result_string[:-1] + "."
