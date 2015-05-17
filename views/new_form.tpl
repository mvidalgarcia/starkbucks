<html>
    <head>
    % include('head.tpl', title='New - Starkbucks')
    </head>
    <body>
        <header>
            <h1><a href="/">Starkbucks</a></h1>
        </header>
        <h2>New Coffee Place</h2>
        <form action="/new" method="post">
            <p>Name: <input name="name" type="text" required/></p>
            <p>Phone: <input name="phone" type="text" required/></p>
            <p>Opening hours: <input name="openhr" type="text" placeholder="Format Mo-Su 09:00-22:00" required/></p>
            <p>Country: <input name="country" type="text" placeholder="DBPedia link i.e: Spain" required/></p>
            <p>Latitude: <input name="lat" type="text" required/></p>
            <p>Longitude: <input name="lng" type="text" required/></p>
            <p>Email: <input name="email" type="email" required/></p>
            <p>Locality: <input name="locality" type="text" placeholder="DBPedia link i.e: Oviedo" required/></p>
            <p>Street Address: <input name="street" type="text" required/></p>
            <p>Postal code: <input name="postal" type="text" required/></p>
            <p>Country code: <input name="code" type="text" placeholder="Format ES, UK ..." required/></p>
            <h3>Choose menu products</h3>
            % for product in products:
            <input name="{{product['name']}}" value="{{product['id']}}" type="checkbox" /> {{product['name']}}<br>
            % end
            <br><input value="Save" type="submit" />
        </form>
    </body>
</body>

