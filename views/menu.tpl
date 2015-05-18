<html>
    <head>
    % include('head.tpl', title= 'Menu - Starkbucks')
    </head>
    <body>
        <div class='page-header'>
			<a href='/'>Starkbucks</a>
		</div>
		<div class='container'>
		    <h1>{{cp_name}} Menu</h1>
		    % for product in products:
				<div class='col-xs-12'>
				<div class="row product">
		            <h3>{{product.name}}</h3>
		            <img src={{product.photo}} alt="{{product.name}} photo" height='300px'>
		            <br><br>
		            <p>{{product.description}}</p>
		            <p class="price">{{product.price}} {{product.currency}}</p>
		            <hr>
				</div>
				</div>
		    % end
		</div>
		<br><br>
	    <footer>
	        <a href="/admin">Admin panel</a><br>
	    	&copy 2015 Starkbucks · Marco Vidal García   
	    </footer>
    </body>
</html>
