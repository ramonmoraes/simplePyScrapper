from sys import argv

from scrapper.parser.ArchParser import ArchParser
from scrapper.Scrapper import Scrapper


if argv[1] == 'web':
    from view.__init__ import app
    app.run()
else:
    print('not web')
# url = 'https://archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

# scrapper = Scrapper(
#     ArchParser,
#     url,
#     False # Save
#     )
# scrapper.scrap(1)