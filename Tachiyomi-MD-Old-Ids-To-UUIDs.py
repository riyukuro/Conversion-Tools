import requests as r
import json
json_backup = input('Input your file path to your Tachiyomi JSON Backup (ie. /home/riyu/Downloads/tachiyomi_backup.json):\n')

backup = open(json_backup, 'r')
backup_data = json.load(backup)
backup.close

count = 0
total_entries = len(backup_data['mangas'])

def get_manga_uuids(mangaid):
    manga_data = {"type": "manga", "ids": [int(mangaid)]}
    manga_post = json.loads(r.post('https://api.mangadex.org/legacy/mapping', json=manga_data).text)
    for i in manga_post: new_id = str(i['data']['attributes']['newId'])
    return new_id

chapter_uuid_list = []
def get_chapter_uuid(chapter_ids):
    chapter_data = {"type": "chapter", "ids": chapter_ids}
    chapter_post = json.loads(r.post('https://api.mangadex.org/legacy/mapping', json=chapter_data).text)
    for i in chapter_post:
        chapter_uuid_list.append(i['data']['attributes']['newId'])
    return chapter_uuid_list
   
for i in backup_data['mangas']:
    count += 1
    print(count,'/',total_entries)
    if i['manga'][2] == 2499283573021220255:
        manga_legacy_id = i['manga'][0].replace('/', '').replace('manga', '')
        new_uuid = get_manga_uuids(manga_legacy_id)
        i['manga'][0] = '/manga/' + new_uuid 

        chapter_id_list = []
        if 'chapters' in i:
            for x in i['chapters']:
                chapter_legacy_id = x['u'].replace('/api/chapter/', '')
                chapter_id_list.append(int(chapter_legacy_id))
            get_chapter_uuid(chapter_id_list)

            for y in range(0, len(chapter_uuid_list)):
                i['chapters'][y]['u'] = '/chapter/' + str(chapter_uuid_list[y])
            chapter_uuid_list = []

        if 'history' in i:
            history_chapter_ids = []
            for x in i['history']:
                history_chapter_ids.append(int(x[0].replace('/api/chapter/', '')))
            get_chapter_uuid(history_chapter_ids)

            for y in range(0, len(chapter_uuid_list)):
                i['history'][y][0] = '/chapter/' + str(chapter_uuid_list[y])
            chapter_uuid_list = []

new_backup = open('tachiyomi_new_uuids.json', 'w')
json.dump(backup_data, new_backup, ensure_ascii=False, indent=4)
new_backup.close()
