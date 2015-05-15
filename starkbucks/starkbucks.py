__author__ = 'mvidalgarcia'

from .persistence.rdf_dao import RDFDao


class Starkbucks:

    def run(self):
        rdfdao = RDFDao()
        # rdfdao.restart_db()
        # rdfdao.example()
        print(rdfdao.get_starkbucks_info().__dict__)
        # print(rdfdao.get_coffee_shops())
        # print(rdfdao.get_coffee_shop(1, 'es').__dict__)
