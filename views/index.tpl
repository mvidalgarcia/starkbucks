<!DOCTYPE HTML>
<html>
    <head>
    % include('head.tpl', title='Starkbucks')
    </head>
    <body>
        <div class="container text-center">
            <br>
            <img class="logo" src="../static/images/logo.png" alt="{{starkbucks.name}} logo">
            <p class="slogan">Because the best coffee of the Seven Kingdoms of Westeros is from Winterfell.</p>
             <h4>Are you a Lannister? Get out of here! </h4>
            <div class="locals">
                <h3>Our Coffee Shops</h3>
                % for local in locals:
                    <div class="col-sm-3">
                        <a href="coffeeplace/{{local['id']}}">{{local['name']}}</a>
                    </div>
                % end
            </div>
            <footer>
                <a href="/admin">Admin panel</a><br>
                &copy 2015 Starkbucks · Marco Vidal García
            </footer>
        </div>
    </body>
</html>

