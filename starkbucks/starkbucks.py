__author__ = 'mvidalgarcia'

from bottle import route, run, view, request
from .persistence.rdf_dao import RDFDao

rdfdao = RDFDao()


def start():
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)


@route('/')
@view('index')
def index():
    return dict(starkbucks=rdfdao.get_starkbucks_info(),
                locals=rdfdao.get_coffee_shops())


@route('/coffeeplace/<id>')
@view('coffeeplace')
def coffeeplace(id):
    return rdfdao.get_coffee_shop(id).__dict__


@route('/menu/<id>')
@view('menu')
def menu(id):
    return dict(cp=request.params.cp,
                menu=rdfdao.get_menu_products(id))


