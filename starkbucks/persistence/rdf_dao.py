__author__ = 'mvidalgarcia'

from SPARQLWrapper import SPARQLWrapper, JSON
from starkbucks.model.starkbucks import Starkbucks
from starkbucks.model.coffee_place import CoffeePlace
from starkbucks.model.product import Product
import os

path = os.path.dirname(__file__)

ENDPOINT_QUERY = 'http://156.35.98.27:3030/DB/query'
ENDPOINT_UPDATE = 'http://156.35.98.27:3030/DB/update'


class RDFDao:
    """
    Class to retrieve RDF data from Fuseki Server
    """
    def __init__(self):
        self.sparql_q = SPARQLWrapper(ENDPOINT_QUERY)
        self.sparql_u = SPARQLWrapper(ENDPOINT_UPDATE)

    def get_starkbucks_info(self):
        """
        Retrieves basic info about company.
        :return: Company name and logo url
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>

        SELECT ?name ?photo WHERE {
          ?com  owl:sameAs      dbr:Starbucks ;
                rdfs:label      ?name ;
                foaf:depiction  ?photo
          }
        """)

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        result = results["results"]["bindings"]

        if len(result) == 1:  # Must be just one result
            result = result[0]
            return Starkbucks(result)

        return None

    def get_coffee_places(self):
        """
        Retrieves basic info about cafés.
        :return: Name and id
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX : <http://starkbucks.es/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?name ?id WHERE {
          ?cs   dc:subject  :starkbucks ;
                rdfs:label  ?name ;
                :id         ?id
          }
        """)

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        coffee_places = []
        for result in results["results"]["bindings"]:
            coffee_places.append({'name': result["name"]["value"],
                                 'id': result["id"]["value"]})
        return coffee_places

    def get_coffee_place(self, id, lang='en'):
        """
        Retrieves information about a café
        :param id: Coffee place identifier
        :return: CoffeePlace object
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX : <http://starkbucks.es/>
        PREFIX schema: <http://schema.org/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX georss: <http://www.georss.org/georss/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        SELECT ?name ?phone ?coords ?email ?address ?country ?street ?postal ?locality ?menu WHERE {{
          ?cs       a   schema:CafeOrCoffeeShop ;
                    :id {id} ;
                    rdfs:label              ?name ;
                    foaf:phone              ?phone ;
                    georss:point            ?coords ;
                    schema:email            ?email ;
                    schema:address          ?address ;
                    dbo:country             ?country_uri ;
                    schema:menu             ?menu .
          ?address  schema:streetAddress    ?street ;
                    schema:postalCode       ?postal ;
                    schema:addressLocality  ?locality_uri
          SERVICE <http://dbpedia.org/sparql> {{
            ?country_uri rdfs:label ?country .
            ?locality_uri rdfs:label ?locality .
            FILTER (lang(?country)='{lang}' && lang(?locality)='{lang}')
          }}
        }}
        """.format(id=id, lang=lang))

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        result = results["results"]["bindings"]

        if len(result) == 1:  # Must be just one result
            return CoffeePlace(result[0])

        return None

    def get_menu_products(self, menu, lang='en'):
        """
        Retrieves information about a café menu
        :param menu: Menu identifier
        :return: Set of Product objects
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX : <http://starkbucks.es/>
        PREFIX schema: <http://schema.org/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX georss: <http://www.georss.org/georss/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        SELECT * WHERE {{
          :{menu}   a               dbr:Menu ;
                    schema:Product  ?prod_uri .
          ?cp       schema:menu     :{menu} ;
                    rdfs:label      ?cp_name .
          ?prod_uri rdfs:label      ?name ;
                    schema:price    ?price ;
                    schema:priceCurrency    ?currency ;
                    foaf:depiction  ?photo ;
                    a               ?type_uri .
          FILTER (lang(?name)='{lang}')
          SERVICE <http://dbpedia.org/sparql> {{
            ?type_uri rdfs:comment ?description .
            FILTER (lang(?description)='{lang}')
          }}
        }}
        """.format(menu=menu, lang=lang))

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        coffee_place_name = results["results"]["bindings"][0]["cp_name"]["value"]

        products = set()
        for result in results["results"]["bindings"]:
            products.add(Product(result))

        return dict(cp_name=coffee_place_name, products=products)

    def restart_db(self):
        """
        Empties Fuseki database and populates it again with data in db.sparql
        """
        self.sparql_u.resetQuery()
        self.sparql_u.setQuery('CLEAR ALL')
        self.sparql_u.method = 'POST'
        self.sparql_u.query()

        # Populate database
        with open(path + "/data/db.sparql", "r") as file:
            db = file.read()

        self.sparql_u.setQuery(db)
        self.sparql_u.query()

        msg = 'RDF Database restarted.'
        return msg



