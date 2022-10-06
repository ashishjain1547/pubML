import json
from time import time
import os

input_text_file = os.listdir('file_input')[0]
input_text_file_path = os.path.join(os.getcwd(), 'file_input', input_text_file)


with open(input_text_file_path, encoding="utf-8") as f:
    lines = f.readlines()

# json_file_path = "BITS Contacts.json"
json_file_path = "MMV_H_Tower_Contacts.json"

with open(json_file_path, 'r') as j:
    num_to_name_dict = json.loads(j.read())

new_lines = []

for i in range(len(lines)):
    for k in num_to_name_dict.keys():
        if k in lines[i]:
            lines[i] = lines[i].replace(k, num_to_name_dict[k])

f = open("file_output/WhatsApp Chat_" + str(round(time())) + ".txt", 'w', encoding="utf-8")
f.writelines(lines)
f.close()
