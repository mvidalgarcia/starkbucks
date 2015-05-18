<html>
    <head>
    % include('head.tpl', title='Delete - Starkbucks')
    </head>
    <body>
        <div class='page-header'>
			<a href='/'>Starkbucks</a>
		</div>
        <h1>Delete a Coffee Place</h1>
        <form action="/delete" method="post">
            % for coffee_place in coffee_places:
                <p>
                    {{coffee_place['name']}} <a href="/delete/{{coffee_place['id']}}">Delete</a>
                </p>
            % end
        </form>
    </body>
</body>

