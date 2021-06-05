import src.config

app = src.config.app
app.testing = True
connex_app = src.config.connex_app
connex_app.add_api('swagger.yml', strict_validation=True)