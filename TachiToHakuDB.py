import json
from difflib import SequenceMatcher

def clean_backup(file_location):
    
    with open(file_location) as file:
        x = json.load(file)

    with open('Hakuneko-connector-list.json') as f:
        z = json.load(f) 
    
    manga_list = list()

    extensions_dict_list = list()
    for l in x['extensions']:
        extensions_dict = {'id': '', 'Source': ''}
        line = l.split(':')
        extensions_dict['id'] = line[0]
        for p in range(len(z)):
            found = False
            matcher = SequenceMatcher(None, a=z[p], b=str(line[-1]).lower()).ratio()
            if matcher > 0.90:
                extensions_dict['Source'] = z[p]
                found = True
                break
            continue
        if found is False:
            user_input = input(f'Please enter the correct Hakuneko connector for the "{line[-1]}" extension: ')
            extensions_dict['Source'] = user_input
        extensions_dict_list.append(extensions_dict)

    for i in x['mangas']:
        manga = {'name': '', 'url': '', 'source': ''}
        manga['name'] = i['manga'][1]
        manga['url'] = i['manga'][0]

        for l in extensions_dict_list:
            if str(i['manga'][2]) == str(l['id']):
                manga['source'] = l['Source']
            
        manga_list.append(manga)
    return(manga_list)

def hakuneko_db_creator(backup):
    tachi_backup = clean_backup(backup)
    db_list = []

    for x in tachi_backup:
        db_dict = {'title': {'connector': '', 'manga': ''},'key': {'connector': '', 'manga': ''}}
        db_dict['title']['connector'] = x['source'].lower().replace(' ', '')
        db_dict['key']['connector'] = x['source'].lower().replace(' ', '').replace('.', '')
        db_dict['title']['manga'] = x['name']
        db_dict['key']['manga'] = x['url']
        db_list.append(db_dict)
        
    with open('hakuneko.bookmarks', 'w') as file:
        json.dump(db_list, file, indent=4)

class main():
    file_location = input('Tachiyomi Legacy Backup Location: ')
    hakuneko_db_creator(file_location)
