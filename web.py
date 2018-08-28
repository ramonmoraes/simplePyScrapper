from sys import argv

from scrapper.parser.ArchParser import ArchParser
from scrapper.Scrapper import Scrapper
from server import app

@app.shell_context_processor
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
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