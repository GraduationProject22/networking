from utils.generate_formatted_string_from_json_string import generate_formatted_string_from_json_string
from utils.write_json_file import write_json_file
from utils.read_file import read_file
from utils.receive_from_uart import receive_from_uart
from time import sleep
#s = read_file("test.json")
# print(generate_formatted_string_from_json_string(s))
#s = "D:30.123456,31.123455,30.340000,+2.110000,-3.110000,30.150000,15.231000,20.514023,?"

# for i in range(len(s), 100):
#	s += '!'

#write_json_file("aya.json", s)

while True:
    receive_from_uart()
    sleep(1)
