import os
import json
import random

with open("via_region_data.json") as f:
    annotation = json.load(f)

print(annotation.keys())
val = random.sample(annotation.keys(), 15)

val_dict = {}
for key in val:
    file_name = key.split("jpg")[0] + 'jpg'
    os.rename(file_name, 'val/' + file_name)
    val_dict.update({key: annotation[key]})
    del annotation[key]

print("val_dict")
print(val_dict)
print("annotation")
print(annotation)

with open('val/via_region_data.json', 'w') as fp:
    json.dump(val_dict, fp)

with open('via_region_data_.json', 'w') as fp:
    json.dump(annotation, fp)