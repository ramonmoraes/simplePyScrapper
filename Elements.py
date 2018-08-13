import requests
from bs4 import BeautifulSoup

class Elements():
    def __init__(self, html):
        self.soup = BeautifulSoup(html, 'html.parser')
    
    def find_all(self, query):
        splited_query = self.get_splited_query(query)

        node = splited_query[0]
        element_classes = " ".join(self.get_list_starting_with(splited_query, ".")).replace(".","")
        element_id = " ".join(self.get_list_starting_with(splited_query, "#")).replace("#", "")
        print(element_classes)
        if len(element_id) > 0:
            return self.soup.find_all(node, {'id': element_id[0]})
        return self.soup.find_all(node, {'class': element_classes})

    def get_splited_query(self, query):
        splited_query = query.replace(".", " .")
        return splited_query.replace("#", " #").split(" ")

    def find_one(self, query):
        if len(self.find_all(query)) == 0:
            return None
        return self.find_all(query)[0]

    def get_list_starting_with(self, list, starting_with):
        starting_with_list = []
        for list_item in list:
            if list_item.startswith(starting_with):
                    starting_with_list.append(list_item)
        return starting_with_list
    
html = requests.get('https://www.archdaily.com.br/br/899761/todays-rising-stars-in-design-metropolis-magazine-reveals-their-picks').text
css = Elements(html).find_all("h1.afd-title-big")
print(css)