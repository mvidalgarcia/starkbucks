__author__ = 'mvidalgarcia'

from bottle import route, run, view, post, request
from .persistence.rdf_dao import RDFDao

rdfdao = RDFDao()


def start():
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)



@route('/restart')
@view('restart')
def restart():
    return dict(msg=rdfdao.restart_db())

@route('/')
@view('index')
def index():
    return dict(starkbucks=rdfdao.get_starkbucks_info(),
                locals=rdfdao.get_coffee_places())


@route('/coffeeplace/<id>')
@view('coffeeplace')
def coffeeplace(id):
    return rdfdao.get_coffee_place(id).__dict__


@route('/menu/<id>')
@view('menu')
def menu(id):
    return rdfdao.get_menu_products(id)

@route('/new_form')
@view('new_form')
def new_form():
    return dict(products=rdfdao.get_all_products())


@post('/new')
def new():
    name = request.forms.get('name')
    phone = request.forms.get('phone')
    openhr = request.forms.get('openhr')
    country = request.forms.get('country')
    lat = request.forms.get('lat')
    lng = request.forms.get('lng')
    email = request.forms.get('email')
    locality = request.forms.get('locality')
    street = request.forms.get('street')
    postal = request.forms.get('postal')
    code = request.forms.get('code')
    id_products = []
    for product in rdfdao.get_all_products():
        id = request.forms.get(product['name'])
        if id is not None:
            id_products.append(request.forms.get(product['name']))

    # Save call
    msg = rdfdao.create_coffee_place(id_products, name, phone, openhr, country,
                                     lat, lng, email, locality, street, postal, code)

    return msg



