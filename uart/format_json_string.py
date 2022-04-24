import json


def format_json_string(json_string):
    json_object = json.loads(json_string)
    result_string = ""

    for key in json_object:
        result_string += key + "=" + str(json_object[key]) + ","

    return result_string[:-1] + "."
