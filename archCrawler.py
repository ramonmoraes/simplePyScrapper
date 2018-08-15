from Crawler import Crawler

class ArchCrawler(Crawler):
    URL = 'https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks'

    def __init__(self):
        super().__init__(self.URL)

    def get_title(self):
        return 'title'
    
    def get_text(self):
        return 'text'

    def get_img(self):
        return 'img'

arch = ArchCrawler()
print(arch.get_snippet())