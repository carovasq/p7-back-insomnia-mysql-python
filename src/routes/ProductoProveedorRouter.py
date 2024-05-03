from flask import Blueprint, request
from src.services.ProductoProveedorService import ProductoProveedorService
from src.models.productoProveedorModel import ProductoProveedor


main3 = Blueprint('productoProveedor_blueprint',__name__)

@main3.route('/',methods=['GET','POST'])
def get_productoProveedor():

  ID_Proveedor = request.json ['ID_Proveedor']
  ID_Producto = request.json ['ID_Producto']

  print(ID_Proveedor)
  print(ID_Producto)


  productoProveedor = ProductoProveedor(0, ID_Proveedor, ID_Producto)

  if request.method == 'GET':
    get_productoProveedor= ProductoProveedorService.get_productoProveedor()
    if get_productoProveedor:
      return 'Lista de Detalle producto actualizada'
    else:
      return 'No se pudo actualizar la Lista de Detalle product'

  elif request.method == 'POST':
    post_productoProveedor= ProductoProveedorService.post_productoProveedor(productoProveedor)
    if post_productoProveedor:
      return 'Detalle producto agregado con exito'
    else:
      return 'No se pudo agregar el Detalle producto'

@main3.route('/', methods=['PUT', 'DELETE'])
def actualizar_eliminar_productoProveedor():
    ID_Producto_Proveedor = request.json['ID_Producto_Proveedor']
    ID_Proveedor = request.json['ID_Proveedor']
    ID_Producto = request.json['ID_Producto']


    productoProveedor = ProductoProveedor(ID_Producto_Proveedor, ID_Proveedor, ID_Producto)
   
    if request.method == 'PUT':
       put_productoProveedor = ProductoProveedorService.put_productoProveedor(ID_Proveedor, productoProveedor)
       if put_productoProveedor:
           return 'Detalle producto editado correctamente'  
       else:
           return 'No se pudo editar el Detalle producto'
    
    elif request.method == 'DELETE':
        delete_productoProveedor = ProductoProveedorService.delete_productoProveedor(ID_Producto_Proveedor)
        if delete_productoProveedor:
            return 'Detalle producto eliminado correctamente'
        else:
            return 'No se pudo eliminar el Detalle producto'