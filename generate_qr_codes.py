import subprocess
import sys
import json

json_data = open(sys.argv[1])
places = json.load(json_data)
json_data.close()

for i, place in enumerate(places):
    subprocess.run([ "qrcode", place["id"], "-o", "{}/{}.png".format(sys.argv[2], place["id"]) ])
    print("{} of {}".format(i, len(places)))
