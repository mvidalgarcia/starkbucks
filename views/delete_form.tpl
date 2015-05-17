<html>
    <head>
    % include('head.tpl', title='Delete - Starkbucks')
    </head>
    <body>
        <header>
            <h1><a href="/">Starkbucks</a></h1>
        </header>
        <h2>Delete a Coffee Place</h2>
        <form action="/delete" method="post">
            % for coffee_place in coffee_places:
                <p>
                    {{coffee_place['name']}} <a href="/delete/{{coffee_place['id']}}">Delete</a>
                </p>
            % end
        </form>
    </body>
</body>

