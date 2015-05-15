__author__ = 'mvidalgarcia'

from .persistence.rdf_dao import RDFDao


class Starkbucks:

    def run(self):
        rdfdao = RDFDao()
        rdfdao.restart_db()
        # rdfdao.example()
        # print(rdfdao.get_starkbucks_info().__dict__)
        # print(rdfdao.get_coffee_shops())
        coffee_shop = rdfdao.get_coffee_shop(1)
        print(coffee_shop.menu)
        products = rdfdao.get_menu_products(coffee_shop.menu)
        for product in products:
            print(product.__dict__)
