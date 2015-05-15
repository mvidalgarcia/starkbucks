<a href="/">home</a>
% for product in menu:
    <h1>{{product.name}}</h1>
    <img src={{product.photo}} alt="{{product.name}} photo" width=300px>
    <p>{{product.price}} {{product.currency}}</p>
    <p>{{product.description}}</p>
% end
