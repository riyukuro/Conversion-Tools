import json
import os

### Doesn't index templates
def connectors(directory):
    matched = []
    for file in os.listdir(directory):
        with open(directory + file, 'r') as f:
            for line in f:
                if 'super.id =' in line:
                    combined = {'Connector': '', 'Key': ''}
                    combined['Connector'] = str(os.path.basename(file)).replace('.mjs', '') #os.path.splitext(file)[0]
                    x = str(line).replace('        super.id = "', '').replace("        super.id = '", "").replace("';\n", '').replace('";\n', '')
                    combined['Key'] = x
                    matched.append(combined)

    with open('HN_Connector_Key_list.json', 'w') as file:
        json.dump(matched, file, indent=4)

directory = '<Insert Hakuneko Connectors Folder Here>'

connectors(directory)