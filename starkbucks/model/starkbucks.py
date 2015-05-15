__author__ = 'mvidalgarcia'


class Starkbucks:
    def __init__(self, sparqldict):
        self.name = sparqldict["name"]["value"]
        self.photo = sparqldict["photo"]["value"]

