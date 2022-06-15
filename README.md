# ejercicio_T-MOB


## Proyecto ejercicio_TMOB

### app_ejercicio

#### Funcionalidad:

Guardar datos en cache cuando existan actualizaciones en el modelo Redirect del proyecto y obtenerlos en formato JSON 

#### Base de datos :

MySQL proporcionada desde Heroku

#### Memoria cache:

Memcached proporcionada desde heroku

#### Modelos:

Redirect:
	key: CharField	
	url: URLField
	active: BooleanField
	updated_at: DateTimeField
	created_at: DateTimeField

Este modelo cuenta con un signal, el cual se ejecuta cuando se persisten datos del modelo Redirect. La finalidad de este signal es, tomar los campos key y url y almacenarlos en Memcached en formato JSON

*Mejora sugerida*: eliminar de la cache aquella key que sea eliminada de la base de datos (no implementado)


#### Views:

index:
Recibe por Get HTTP el parametro Key, busca en cache y devuelve un JSON con la key y su url. De no existir la key devuelve None.


### Heroku app:

URL: https://db-tmob.herokuapp.com/
URL TEST: https://db-tmob.herokuapp.com/?key=tmob 
URL ADMIN: https://db-tmob.herokuapp.com/admin 

Usuario: tmob  
Password: tmob_1234
