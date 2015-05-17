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
    Class to manage RDF data from Fuseki Server
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
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX owl: <http://www.w3.org/2002/07/owl#>
        PREFIX schema: <http://schema.org/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX georss: <http://www.georss.org/georss/>
        SELECT * WHERE {{
          ?cs       a   schema:CafeOrCoffeeShop ;
                    :id {id} ;
                    rdfs:label              ?name ;
                    foaf:phone              ?phone ;
                    schema:openingHours     ?openhr ;
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

        try:
            results = self.sparql_q.query().convert()
        except Exception:
            msg = "DBPedia might be under maintenance."
            print(msg)
            return msg

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
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
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

    def get_all_products(self, lang='en'):
        """
        Retrieves all the products names
        :return: All the products names and ids
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX schema: <http://schema.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbr: <http://dbpedia.org/resource/>
        SELECT DISTINCT ?prod_uri ?name WHERE {{
          ?m        a               dbr:Menu ;
                    schema:Product  ?prod_uri .
          ?prod_uri rdfs:label      ?name ;

          FILTER (lang(?name)='{lang}')
        }}
        """.format(lang=lang))

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        products = []

        for result in results["results"]["bindings"]:
            product = dict(id=result['prod_uri']['value'].split('/')[-1],
                           name=result['name']['value'])
            products.append(product)

        return products

    def get_all_coffee_places(self):
        """
        Retrieves all the coffee places names
        :return: All the coffee places names and ids
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX : <http://starkbucks.es/>
        PREFIX schema: <http://schema.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?id ?name WHERE {
          ?cp   a           schema:CafeOrCoffeeShop ;
                :id         ?id ;
                rdfs:label  ?name .
        }
        """)

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        coffee_places = []

        for result in results["results"]["bindings"]:
            coffee_place = dict(id=result['id']['value'],
                           name=result['name']['value'])
            coffee_places.append(coffee_place)

        return coffee_places

    def _get_next_id(self):
        """
        Get next coffee place id to write
        :return: Next id
        """
        self.sparql_q.resetQuery()
        self.sparql_q.setQuery("""
        PREFIX : <http://starkbucks.es/>
        PREFIX schema: <http://schema.org/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT (MAX(?id) as ?max) WHERE {{
          ?cs       a   schema:CafeOrCoffeeShop ;
                    :id ?id .
        }}
        """)

        self.sparql_q.setReturnFormat(JSON)
        results = self.sparql_q.query().convert()

        result = results["results"]["bindings"]

        if len(result) == 1:  # Must be just one result
            next_id = int(result[0]['max']['value']) + 1
            return next_id

        return None

    def create_coffee_place(self, id_products, name, phone, openhr, country,
                            lat, lng, email, locality, street, postal, code):
        """
        Create new coffee place and its menu
        :return: Message of status
        """
        next_id = self._get_next_id()

        subquery_menu = ''
        for id in id_products:
            subquery_menu += 'schema:Product  :{} '.format(id)
            if id != id_products[-1]:
                subquery_menu += ';\n'
            else:
                subquery_menu += '.'

        self.sparql_u.resetQuery()
        self.sparql_u.method = 'POST'
        query = """
        PREFIX : <http://starkbucks.es/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX dc: <http://purl.org/dc/elements/1.1/>
        PREFIX schema: <http://schema.org/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        PREFIX georss: <http://www.georss.org/georss/>
        INSERT DATA {{
            :cp{next_id}    :id {next_id} ;
            a schema:CafeOrCoffeeShop ;
            dc:subject :starkbucks ;
            rdfs:label "{name}" ;
            foaf:phone {phone} ;
            schema:openingHours "{openhr}" ;
            dbo:country dbr:{country} ;
            georss:point "{lat} {lng}" ;
            schema:email "{email}" ;
            schema:address [
                schema:streetAddress "{street}" ;
                schema:addressLocality dbr:{locality} ;
                schema:postalCode "{postal}" ;
                schema:addressCountry "{code}"
            ] ;
            schema:menu :m{next_id} .


            :m{next_id}  a  dbr:Menu ;
            {subquery}
        }}
        """.format(next_id=next_id, name=name, phone=phone,
                   openhr=openhr, country=country, lat=lat,
                   lng=lng, email=email, street=street,
                   locality=locality, postal=postal, code=code,
                   subquery=subquery_menu)

        self.sparql_u.setQuery(query)

        try:
            self.sparql_u.query()
            msg = "Coffee place id={} created.".format(next_id)
            print(msg)
            return msg
        except Exception:
            msg = "Something wrong happened creating a new coffee place."
            print(msg)
            return msg

    def delete_coffee_place(self, id):
        self.sparql_u.resetQuery()
        self.sparql_u.method = 'POST'
        self.sparql_u.setQuery("""
        PREFIX : <http://starkbucks.es/>
        DELETE {{ :cp{id} ?p  ?o . }}
        WHERE {{ :cp{id} ?p  ?o . }}
        """.format(id=id))

        try:
            self.sparql_u.query()
        except Exception:
            msg = "Something wrong happened deleting an existing coffee place."
            print(msg)
            return msg


        self.sparql_u.setQuery("""
        PREFIX : <http://starkbucks.es/>
        DELETE {{ :m{id}  ?p  ?o . }}
        WHERE {{ :m{id}  ?p  ?o . }}
        """.format(id=id))

        try:
            self.sparql_u.query()
            msg = "Coffee place id={} deleted.".format(id)
            print(msg)
            return msg
        except Exception:
            msg = "Something wrong happened deleting the coffee place menu."
            print(msg)
            return msg

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



