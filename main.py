from utils.generate_formatted_string_from_json_string import generate_formatted_string_from_json_string
from utils.read_file import read_file
from utils.generate_json_object_from_fromatted_string import generate_json_object_from_fromatted_string


formatted_string = "DATA:12,123,312"

print(generate_json_object_from_fromatted_string(formatted_string))
json_string = read_file("test.json")


print(generate_formatted_string_from_json_string(json_string))
