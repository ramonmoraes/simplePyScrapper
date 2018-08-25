import json
import os

from scrapper.parser.ArchParser import ArchParser
from scrapper.Scrapper import Scrapper

scrapper = Scrapper(
    ArchParser,
    'https://archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'
    )
scrapper.scrap(1)
print(len(scrapper.parser_list))