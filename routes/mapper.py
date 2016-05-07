from routes import Mapper


map = Mapper()
map.connect(None, "/error/{action}/{id}", controller="error")
map.connect("home", "/", controller="main", action="index")

result = map.match('/error/myapp/4')
print result
