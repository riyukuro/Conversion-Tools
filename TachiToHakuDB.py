"""Converts Tachiyomi Legacy Backups to Hakuneko DB files"""
import json
from difflib import SequenceMatcher

def clean_backup(file_location):
    """This method cleans the Tachiyomi Legacy backup file to use in hakuneko_db_creator method"""
    
    with open(file_location) as file:
        backup = json.load(file)

    with open('Hakuneko-connector-list.json') as file2:
        connector_list = json.load(file2)

    manga_list = list()

    extensions_dict_list = list()
    for a in backup['extensions']:
        extensions_dict = {'id': '', 'Source': ''}
        line = a.split(':')
        extensions_dict['id'] = line[0]

        for b, connector in enumerate(connector_list):
            found = False
            matcher = SequenceMatcher(None, a=connector, b=str(line[-1]).lower()).ratio()
            if matcher > 0.90:
                extensions_dict['Source'] = connector_list[b]
                found = True
                break
            continue
        if found is False:
            user_input = input(f'Please enter the Hakuneko connector name for the "{line[-1]}" extension: ')
            extensions_dict['Source'] = user_input
        extensions_dict_list.append(extensions_dict)

    for c in backup['mangas']:
        manga = {'name': '', 'url': '', 'source': ''}
        manga['name'] = c['manga'][1]
        manga['url'] = c['manga'][0]

        for d in extensions_dict_list:
            if str(c['manga'][2]) == str(d['id']):
                manga['source'] = d['Source']
        manga_list.append(manga)
    hakuneko_db_creator(manga_list)

def hakuneko_db_creator(backup):
    """This method creates the hakuneko.bookmarks DB from the clean_backup method."""
    db_list = []

    for x in backup:
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
    clean_backup(file_location)
