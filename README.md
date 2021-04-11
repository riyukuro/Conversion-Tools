# Tachiyomi Backup To Hakuneko DB
Converts a legacy Tachiyomi backup to a Hakuneko database file. NOTE: Some sources will have to be manually changed/entered &amp; Chapters read is not kept.

# Issues:
- Due to the name differences used in Tachiyomi's Extensions and Hakuneko's sources, matching them is not always accurate and would cause more issues hence why some need to be manually changed. (`Hakuneko-connector-list.json` has a list of Hakuneko Connecter:Connector Key pairs for easier matching, however does not include the templates folder so not all of the entries are in there. In cases where you can't find a match inside of the file you can search the website inside of Hakuneko and hover over it and it will give you the connector name and key)
  - *Note: Hakuneko-connector-list.json can be generated with the `HakuNeko-Connectors-Keys.py` file.*

- Due to the way Hakuneko handles chapter bookmarks it requires a chapter-name which can't be gotten from the Tachiyomi legacy backup. Even with chapter names I would sometimes run into issues where it would ignore the entry in hakuneko.chaptermarks.

# Usage:
- Clone or download the zip of the repository.
- inside of the directory; run `python3 TachiToHakuDB.py` in command prompt/terminal
- It will ask for the location of your tachiyomi legacy backup, if it's placed inside of the same folder you should be able to just put the name, otherwise get the path. (ie. `C:/users/riyu/downloads/tachiyomi_*date*.json`)
- It will create a `hakuneko.bookmarks` file.
- At this point I would reccomend opening the json file inside of a text editor and using 'Find and Replace' to change source names to match hakuneko's connectors.
  - *Note: From my expierence only the key connector's name matters. However this may cause issues elsewhere.*
- After you finish editing the file you can find the location of the hakuneko config folder at https://hakuneko.download/docs/install/#user-data and then you can move and replace your existing `hakuneko.bookmarks`
  - **NOTE:** *Anything inside of your pre-existing bookmarks file will be lost if you replace it. You can move the file to somewhere else or add .backup at the end of the name to keep it.*
