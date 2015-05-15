<h1>Hello {{starkbucks.name}}!</h1>
<img src={{starkbucks.photo}} alt="Starkbucks logo" width=300px>
<h2>Our locals</h2>
% for local in locals:
<a href="coffeeplace/{{local['id']}}">{{local['name']}}</a>
% end

