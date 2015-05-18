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
                    <div itemscope itemtype="http://schema.org/Product" class="row product">
                        <h3 itemprop="name">{{product.name}}</h3>
                        <img itemprop="image" src={{product.photo}} alt="{{product.name}} photo" height='300px'>
                        <br><br>
                        <p itemprop="description">{{product.description}}</p>
                        <div itemprop="offers" itemscope itemtype="http://schema.org/Offer">
                            <p class="price"><span itemprop="price">{{product.price}}</span> <span itemprop="priceCurrency">{{product.currency}}</span></p>
                        </div>
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
