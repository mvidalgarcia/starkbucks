<html>
    <head>
        % include('head.tpl', title= 'Coffee Place - Starkbucks')
        <script src='https://api.tiles.mapbox.com/mapbox.js/v2.1.9/mapbox.js'></script>
        <link href='https://api.tiles.mapbox.com/mapbox.js/v2.1.9/mapbox.css' rel='stylesheet' />
        <style>
          #map { max-width:100%; height:50% }
        </style>
    </head>
    <body>
	    <div class='page-header'>
			<a href='/'>Starkbucks</a>
		</div>
	    <div class='container'>
	        <div class="col-xs-12 col-sm-6" id='map'></div>
	        <div itemscope itemtype="http://schema.org/CafeOrCoffeeShop" class='col-xs-12 col-sm-6'>
		        <div class="cafe-title" itemprop="name">{{name}}</div>
		        <div class="cafe-info">
			        <p itemprop="address">Address: {{street}}, {{locality}}, {{postal}}, {{country}}</p>
			        <p itemprop="openingHours">Schedule: {{open_hr}}</p>
			        <p itemprop="telephone">Telephone: {{phone}}</p>
			        <p itemprop="email">Contact: {{email}}</p>
		        </div>
		        <a class="show-btn" href="/menu/{{menu}}">Show menu</a>
		    </div>
	        <script>
	        L.mapbox.accessToken = 'pk.eyJ1IjoibXZpZGFsZ2FyY2lhIiwiYSI6IjRQME5YVlUifQ.BHfG2NF5m_sdBXLr_HOIiQ';
	        var map = L.mapbox.map('map', 'mapbox.streets')
	            .setView([{{lat}}, {{lng}}], 14);
	        L.marker([{{lat}}, {{lng}}]).addTo(map);
	        </script>
	     </div>
	    <footer>
		    <a href="/admin">Admin panel</a><br>
        	&copy 2015 Starkbucks · Marco Vidal García   
        </footer>
    </body>
</html>