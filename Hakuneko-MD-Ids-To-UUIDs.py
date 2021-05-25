import json
import requests

class main():
    legacy_mapping = 'https://api.mangadex.org/legacy/mapping'

    hakuneko = open('hakuneko.bookmarks', 'r')
    hakuneko_data = json.load(hakuneko)
    hakuneko.close()

    total_entries = len(hakuneko_data)
    count = 0

    for i in hakuneko_data:
        count += 1
        
        if i['key']['connector'] == 'mangadex':
            mangaid = i['key']['manga'].replace('/', '').replace('manga', '')
            data = {"type": "manga", "ids": [int(mangaid)]}
            post_data = json.loads(requests.post(legacy_mapping, json=data).text)
            for data in post_data: new_id = str(data['data']['attributes']['newId'])
            i['key']['manga'] = str(new_id)

        print(f'Progress: {count}/{total_entries}')

    hakuneko = open('hakuneko.bookmarks', 'w')
    json.dump(hakuneko_data, hakuneko, ensure_ascii=False, indent=4)
    hakuneko.close()
