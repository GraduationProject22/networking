from write_json_file import write_json_file
from read_file import read_file
from format_json_string import format_json_string

str = read_file("test.json")

#  This line will print: ip=192.168.50.56,s=025,a=3.
print(format_json_string(str))


# Writing string received from STM32 to a json file

str = "ip=192.168.50.56,s=025,a=3."

write_json_file("test2.json", str)
