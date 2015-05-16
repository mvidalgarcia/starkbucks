<html>
    <head>
    % include('head.tpl', title='Home - Starkbucks')
    </head>
    <body>
        <header>
            <h1>{{starkbucks.name}}</h1>
        </header>
        <img src={{starkbucks.photo}} alt="{{starkbucks.name}} logo" width=300px>
        <h2>Our locals</h2>
        % for local in locals:
        <a href="coffeeplace/{{local['id']}}">{{local['name']}}</a>
        % end
    </body>
</body>

