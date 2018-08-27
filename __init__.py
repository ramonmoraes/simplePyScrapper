from sys import argv

from scrapper.parser.ArchParser import ArchParser
from scrapper.Scrapper import Scrapper

# collection_name = argv[1] if len(argv) > 2 or 'snippets' 
# run_type = argv[2] if len(argv) > 3 or 'crawler'

# if run_type == 'web'::
from view.__init__ import app
app.run()
# else:
#     print('not web')
# url = 'https://archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

# scrapper = Scrapper(
#     ArchParser,
#     url,
#     False # Save
#     )
# scrapper.scrap(1)