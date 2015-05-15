__author__ = 'mvidalgarcia'


class CoffeeShop:
    def __init__(self, sparqldict):
        self.name = sparqldict["name"]["value"]
        self.phone = sparqldict["phone"]["value"]
        self.lat = sparqldict["coords"]["value"].split()[0]
        self.lng = sparqldict["coords"]["value"].split()[1]
        self.email = sparqldict["email"]["value"]
        self.country = sparqldict["country"]["value"]
        self.street = sparqldict["street"]["value"]
        self.postal = sparqldict["postal"]["value"]
        self.locality = sparqldict["locality"]["value"]
