<!DOCTYPE HTML>
<html>
    <head>
    % include('head.tpl', title='Starkbucks')
    <link rel="stylesheet" type="text/css" href="../static/css/style.css">
    </head>
    <body>
        <div class="container text-center">
            <header>
                <br>
                <img class="logo" src="../static/images/logo.png" alt="{{starkbucks.name}} logo" width=300px>
                <h3>Because the best coffee of the Seven Kingdoms of Westeros is from Winterfell.</h3>
                 <h4>Are you a Lannister? Get out of here! </h4>
            </header>
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

