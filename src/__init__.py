from flask import Flask;
from src.routes import ProveedorRouter
from src.routes import ProductoRouter
from src.routes import ProductoProveedorRouter


app= Flask(__name__)

def init_app(config):
  app.config.from_object(config)
  app.register_blueprint(ProductoRouter.main, url_prefix='/producto')
  app.register_blueprint(ProveedorRouter.main2,url_prefix='/proveedor')
  app.register_blueprint(ProductoProveedorRouter.main3,url_prefix='/productoProveedor')
  return app