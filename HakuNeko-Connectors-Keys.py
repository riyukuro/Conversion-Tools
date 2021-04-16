import json
import os

### Doesn't index templates
def connectors(directory):
    matched = []
    for file in os.listdir(directory):
        with open(directory + file, 'r') as f:
            for line in f:
                if 'super.id =' in line:
                    x = str(line).replace('        super.id = "', '').replace("        super.id = '", "").replace("';\n", '').replace('";\n', '')
                    matched.append(x)

    with open('Hakuneko-connector-list.json', 'w') as file:
        json.dump(matched, file, indent=4)

directory = '<Insert Directory Here>'

connectors(directory)
