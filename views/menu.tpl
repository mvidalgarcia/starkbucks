<a href="/">home</a>
% if cp:
    <h1>{{cp}} Menu</h1>
% end
% for product in menu:
    <h2>{{product.name}}</h2>
    <img src={{product.photo}} alt="{{product.name}} photo" width=300px>
    <p>{{product.price}} {{product.currency}}</p>
    <p>{{product.description}}</p>
% end
