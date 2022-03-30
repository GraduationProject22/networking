import json


def generate_json_object_from_string(string):
    object = {}
    for item in string[:-1].split(","):
        key, value = item.split("=")
        object[key] = value
    return json.dumps(object)
