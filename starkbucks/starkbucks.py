__author__ = 'mvidalgarcia'

from bottle import route, run, view
from .persistence.rdf_dao import RDFDao

rdfdao = RDFDao()


def start():
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)


@route('/hello')
@view('index')
def index():
    return rdfdao.get_starkbucks_info().__dict__



    # rdfdao.restart_db()
    # rdfdao.example()
    # print(rdfdao.get_starkbucks_info().__dict__)
    # print(rdfdao.get_coffee_shops())
    # coffee_shop = rdfdao.get_coffee_shop(2)
    # print(coffee_shop.menu)
    # products = rdfdao.get_menu_products(coffee_shop.menu)
    # for product in products:
    #     print(product.__dict__)




