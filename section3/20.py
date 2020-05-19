import json
import gzip

with gzip.open("jawiki-country.json.gz", 'rt') as data:
    for line in data:
        data_json = json.loads(line)
        if data_json['title'] == 'イギリス':
            print(data_json['text'])
            break