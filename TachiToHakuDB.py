import json
def clean_backup(file_location):
    
    with open(file_location) as file:
        x = json.load(file)
    
    manga_list = list()

    extensions_dict = dict(s.split(':') for s in x['extensions'])
    random_list = []
    for i in range(len(extensions_dict)):
        extensions_dict_fixed = {'id': '', 'Source': ''}
        extensions_dict_fixed['id'] = list(extensions_dict.keys())[i]
        extensions_dict_fixed['Source'] = list(extensions_dict.values())[i]
        random_list.append(extensions_dict_fixed)
        
    for i in x['mangas']:
        manga = {'name': '', 'url': '', 'source': ''}
        manga['name'] = i['manga'][1]
        manga['url'] = i['manga'][0]

        for l in random_list:
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