import json
import requests

class main():
    legacy_mapping = 'https://api.mangadex.org/legacy/mapping'

    hakuneko = open('hakuneko.bookmarks', 'r')
    hakuneko_data = json.load(hakuneko)
    hakuneko.close()

    for i in hakuneko_data:
        if i['key']['connector'] != 'mangadex':
            continue
        else:
            mangaid = int(i['key']['manga'].replace('/', '').replace('manga', ''))
            data = {"type": "manga", "ids": [mangaid]}
            post_data = requests.post(legacy_mapping, json=data)
            f = json.loads(post_data.text)
            for z in f:
                new_id = str(z['data']['attributes']['newId'])
            i['key']['manga'] = f'/manga/{new_id}'
            print(i['key'])

    hakuneko = open('hakuneko.bookmarks', 'w')
    hakuneko.write(str(json.dump(hakuneko_data, hakuneko, indent=4)))
    hakuneko.close()
