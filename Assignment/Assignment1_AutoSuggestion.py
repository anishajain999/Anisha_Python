from collections import Counter
from typing import Counter
import json

para = input("Enter Paragraph: ").lower()
search = input("Enter Search string: ").lower()
p = para.split(" ")
# print(p)
l = []
for i in p:
    # print(i)
    if i.startswith(search):
        # print(i)
        l.append(i)
        # print(l)
duplicate_list = Counter(l)
# print(duplicate_list.most_common())
lst = duplicate_list.most_common()
# print((lst))
for l in range(3):
    print(lst[l])

# JSON 
json_string = json.dumps(duplicate_list, indent=4)

with open('mydata.json', 'w') as f:
    # f.seek(0)
    f.write(json_string)
# print(f)

with open('mydata.json','r') as f:
    json_object = json.loads(f.read())

print(json_object)