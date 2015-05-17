<html>
    <head>
        % include('head.tpl', title= 'Coffee Place - Starkbucks')
        <script src='https://api.tiles.mapbox.com/mapbox.js/v2.1.9/mapbox.js'></script>
        <link href='https://api.tiles.mapbox.com/mapbox.js/v2.1.9/mapbox.css' rel='stylesheet' />
        <style>
          body { margin:0; padding:0; }
          #map { width:40%; height:50% }
        </style>
    </head>
    <body>
        <header>
            <h1><a href='/'>Starkbucks</a></h1>
        </header>
        <h1>{{name}}</h1>
        <p>{{country}}</p>
        <p>{{phone}}</p>
        <p>{{lat}}</p>
        <p>{{lng}}</p>
        <p>{{email}}</p>
        <p>{{street}}
        <p>{{postal}}</p>
        <p>{{locality}}</p>
        <a href="/menu/{{menu}}">Show menu</p></a>
        <div id='map'></div>
        <script>
        L.mapbox.accessToken = 'pk.eyJ1IjoibXZpZGFsZ2FyY2lhIiwiYSI6IjRQME5YVlUifQ.BHfG2NF5m_sdBXLr_HOIiQ';
        var map = L.mapbox.map('map', 'mapbox.streets')
            .setView([{{lat}}, {{lng}}], 14);
        L.marker([{{lat}}, {{lng}}]).addTo(map);
        </script>
    </body>
</html>