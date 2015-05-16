<html>
    <head>
    % include('head.tpl', title= 'Menu - Starkbucks')
    </head>
    <body>
        <header>
            <h1><a href='/'>Starkbucks</a></h1>
        </header>
        <h1>{{cp_name}} Menu</h1>
        % for product in products:
            <h2>{{product.name}}</h2>
            <img src={{product.photo}} alt="{{product.name}} photo" width=300px>
            <p>{{product.price}} {{product.currency}}</p>
            <p>{{product.description}}</p>
        % end
    </body>
</html>
