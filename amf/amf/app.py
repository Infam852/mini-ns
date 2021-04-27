from connexion import FlaskApp
from connexion.resolver import RestyResolver


app = FlaskApp(__name__, specification_dir='openapi/')
app.add_api('openapi.yml', resolver=RestyResolver('amf.routes'))
app = app.app
