import json


def write_json_file(file_name, string):
    """
    Writes a string to a file.
    """
    json_object = generate_json_object_from_string(string)
    with open(file_name, 'w') as f:
        f.write(json_object)


def generate_json_object_from_string(string):
    object = {}
    for item in string[:-1].split(","):
        key, value = item.split("=")
        object[key] = value
    return json.dumps(object)
