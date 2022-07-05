import json


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
    json_object = {}
    for item in formatted_string.split("?"):
        if item[0] == "D":
            json_object["D"] = item.split(":")[1]
        else:
            json_object["W"] = item.split(":")[1]
    with open(file_name, 'w') as f:
        f.write(json.dumps(json_object))
