<html>
    <head>
    % include('head.tpl', title='New - Starkbucks')
    </head>
    <body>
        <header>
            <h1>Starkbucks</h1>
        </header>
        <h2>New Coffee Place</h2>
        <form action="/new" method="post">
            <p>Name: <input name="name" type="text" /></p>
            <p>Phone: <input name="phone" type="text" /></p>
            <p>Opening hours: <input name="openhr" type="text" placeholder="Format Mo-Su 09:00-22:00" /></p>
            <p>Country: <input name="country" type="text" placeholder="DBPedia link i.e: Spain"/></p>
            <p>Latitude: <input name="lat" type="text" /></p>
            <p>Longitude: <input name="lng" type="text" /></p>
            <p>Email: <input name="email" type="email" /></p>
            <p>Locality: <input name="locality" type="text" placeholder="DBPedia link i.e: Oviedo" /></p>
            <p>Street Address: <input name="street" type="text" /></p>
            <p>Postal code: <input name="postal" type="text" /></p>
            <p>Country code: <input name="code" type="text" placeholder="Format ES, UK ..."/></p>
            <h3>Choose menu products</h3>
            % for product in products:
            <input name="{{product['name']}}" value="{{product['id']}}" type="checkbox" /> {{product['name']}}<br>
            % end
            <br><input value="Save" type="submit" />
        </form>
    </body>
</body>

