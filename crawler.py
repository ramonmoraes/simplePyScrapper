from scrapper.parser.MTVnews import MTVnews
from scrapper.Scrapper import Scrapper

url = 'http://www.mtv.com.br/noticias/x7j15z/clipe-novo-camila-cabello-e-dylan-sprouse-trabalham-em-projeto-misterioso'
scrapper = Scrapper(
    MTVnews,
    MTVnews.URL,
    # url,
    True # Save
    )
scrapper.scrap(1)
