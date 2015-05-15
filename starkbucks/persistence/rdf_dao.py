__author__ = 'mvidalgarcia'

from SPARQLWrapper import SPARQLWrapper, JSON
from starkbucks.model.starkbucks import Starkbucks
from starkbucks.model.coffee_shop import CoffeeShop
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

    def get_coffee_shops(self):
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

        coffee_shops = []
        for result in results["results"]["bindings"]:
            coffee_shops.append({'name': result["name"]["value"],
                                 'id': result["id"]["value"]})
        return coffee_shops

    def get_coffee_shop(self, id, lang='en'):
        """
        Retrieves information about a café
        :param id: Coffee shop identifier
        :return: CoffeeShop object
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
        SELECT ?name ?phone ?coords ?email ?address ?country ?street ?postal ?locality WHERE {{
          ?cs       a   schema:CafeOrCoffeeShop ;
                    :id {id} ;
                    rdfs:label              ?name ;
                    foaf:phone              ?phone ;
                    georss:point            ?coords ;
                    schema:email            ?email ;
                    schema:address          ?address ;
                    dbo:country             ?country_uri .
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
            return CoffeeShop(result[0])

        return None

    def example(self):
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbp: <http://dbpedia.org/property/>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX db: <http://dbpedia.org/>

        SELECT * WHERE {
          ?x rdfs:label "Hot Chocolate" .
          ?x a ?choco_dbp
          SERVICE <http://dbpedia.org/sparql> {
            ?choco_dbp rdfs:comment ?res .
            FILTER (lang(?res)='en')}
        }
        LIMIT 10
        """)

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        print(results)

        for result in results["results"]["bindings"]:
            print(result["res"]["value"])

    def restart_db(self):
        # Empty database
        self.sparql_u.resetQuery()
        self.sparql_u.setQuery('CLEAR ALL')
        self.sparql_u.method = 'POST'
        self.sparql_u.query()

        # Populate database
        with open(path + "/data/db.sparql", "r") as file:
            db = file.read()

        self.sparql_u.setQuery(db)
        self.sparql_u.query()

        print('RDF Database restarted.')



