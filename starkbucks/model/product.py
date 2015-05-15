__author__ = 'mvidalgarcia'


class Product:
    def __init__(self, sparqldict):
        self.name = sparqldict["name"]["value"]
        self.price = sparqldict["price"]["value"]
        self.currency = sparqldict["currency"]["value"]
        self.photo = sparqldict["photo"]["value"]
        self.description = sparqldict["description"]["value"]