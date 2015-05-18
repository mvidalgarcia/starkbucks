__author__ = 'mvidalgarcia'


class CoffeePlace:
    def __init__(self, sparqldict):
        self.name = sparqldict["name"]["value"]
        self.phone = sparqldict["phone"]["value"]
        self.open_hr = sparqldict["open_hr"]["value"]
        self.lat = sparqldict["coords"]["value"].split()[0]
        self.lng = sparqldict["coords"]["value"].split()[1]
        self.email = sparqldict["email"]["value"]
        self.country = sparqldict["country"]["value"]
        self.street = sparqldict["street"]["value"]
        self.postal = sparqldict["postal"]["value"]
        self.locality = sparqldict["locality"]["value"]
        self.menu = sparqldict["menu"]["value"].split('/')[-1]
